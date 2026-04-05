from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import Base
from app.core.config import settings


engine = create_engine(settings.DATABASE_URL)

Session = sessionmaker(engine)

def get_db():
    db = Session()
    try: 
        yield db
    finally:
        db.close()