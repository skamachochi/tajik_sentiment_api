# Tajik Sentiment Classifier API

A REST API for sentiment analysis of Tajik-language text, built with FastAPI and a fine-tuned multilingual BERT model.

## Features

- Classifies Tajik text as **positive** or **negative**
- JWT-based authentication
- User registration and login
- Prediction history stored per user
- Dockerized with PostgreSQL

## Tech Stack

- **FastAPI** — web framework
- **BERT** (`bert-base-multilingual-cased`) — fine-tuned on Tajik sentiment data
- **PostgreSQL** — database
- **SQLAlchemy** — ORM
- **Docker** — containerization

## Setup

### With Docker

```bash
docker-compose up --build
```

### Without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and get JWT token |
| POST | `/predict` | Classify sentiment of Tajik text |
| GET | `/predictions` | Get prediction history for current user |

## Example

```bash
curl -X POST http://localhost:8000/predict \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Ман аз кори имрӯза хурсандам."}'
```

Response:
```json
{"label": "positive", "confidence": 0.95}
```
