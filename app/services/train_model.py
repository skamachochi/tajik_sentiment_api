import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)
import torch

data_path = "/Users/azamat/Desktop/sentiment API/dataset/train_data.csv"
test_data_path = "/Users/azamat/Desktop/sentiment API/dataset/testing_data.csv"

MODEL_NAME = "bert-base-multilingual-cased"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Load and prepare training data
data = pd.read_csv(data_path).dropna(subset=['Comment'])
data['label'] = data['Label'].map({"HAPPY": 1, "SAD": 0})

data_train, data_val = train_test_split(data, train_size=0.9)

train_dataset = Dataset.from_dict({"text": list(data_train['Comment']), "label": list(data_train['label'])})
val_dataset = Dataset.from_dict({"text": list(data_val['Comment']), "label": list(data_val['label'])})

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding=True, max_length=128)

train_dataset = train_dataset.map(tokenize, batched=True)
val_dataset = val_dataset.map(tokenize, batched=True)

# Load model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)

# Training
args = TrainingArguments(
    output_dir="./bert_output",
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    eval_strategy="epoch",
    save_strategy="no",
    logging_steps=50,
)

def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    return {"accuracy": round(accuracy_score(labels, preds), 2)}

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
)

trainer.train()

# Test on external dataset
test_data = pd.read_csv(test_data_path).dropna(subset=['review'])
test_data['label'] = test_data['label'].map({"positive": 1, "negative": 0})
test_dataset = Dataset.from_dict({"text": list(test_data['review']), "label": list(test_data['label'])})
test_dataset = test_dataset.map(tokenize, batched=True)

results = trainer.predict(test_dataset)
y_pred = results.predictions.argmax(-1)
print("Test accuracy:", round(accuracy_score(test_data['label'], y_pred), 2))
