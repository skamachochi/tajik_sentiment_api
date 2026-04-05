from pydantic import BaseModel

class UserRegister(BaseModel):
    email: str
    username: str
    password: str

class PredictRequest(BaseModel):
    text: str

class PredictResponse(BaseModel):
    label: str
    confidence: float

class UserOut(BaseModel):
    id: int
    email: str
    username: str

class UserLogin(BaseModel):
    email: str
    password: str
