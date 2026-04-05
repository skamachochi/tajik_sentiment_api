import torch
import torch.nn.functional as F
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from app.core.config import settings

model = AutoModelForSequenceClassification.from_pretrained(settings.MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(settings.MODEL_PATH)
model.eval()

def predict_sentiment(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    
    with torch.no_grad():
        outputs = model(**inputs)
    
    probs = F.softmax(outputs.logits, dim=-1)
    pred = probs.argmax().item()
    confidence = probs.max().item()
    
    label = "positive" if pred == 1 else "negative"
    return {"label": label, "confidence": round(confidence, 2)}
