from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="app/.env")
    DATABASE_URL: str
    SECRET_KEY: str
    MODEL_PATH: str

settings = Settings()