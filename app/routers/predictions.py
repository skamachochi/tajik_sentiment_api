from fastapi import APIRouter, Depends, HTTPException
from app.core.security import get_current_user
from app.models.user import User, Prediction
from app.schemas import schemas
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.services.sentiment import predict_sentiment

router = APIRouter()

@router.post("/predict", response_model=schemas.PredictResponse)
def predict(request: schemas.PredictRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    
    result = predict_sentiment(request.text)
    label, confidence = result['label'], result['confidence']
    prediction = Prediction(
    user_id=current_user.id,
    input_text=request.text,
    label=label,
    confidence=confidence
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

@router.get("/predictions", response_model=list[schemas.PredictResponse])
def user_predictions(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    existing_predictions = db.query(Prediction).filter(Prediction.user_id == current_user.id).all()
    if not existing_predictions:
        raise HTTPException(status_code=404, detail='No prediction found for this user!')
    
    return existing_predictions