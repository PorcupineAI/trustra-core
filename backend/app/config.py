from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    DATABASE_URL: str = Field(
        default="postgresql://user:pass@localhost/trustra",
        env="DATABASE_URL"
    )
    SECRET_KEY: str = Field(
        default="CHANGE_THIS_IN_PRODUCTION_AND_USE_ENV_VAR",
        env="SECRET_KEY"
    )
    WHATSAPP_TOKEN: Optional[str] = Field(None, env="WHATSAPP_TOKEN")
    WHATSAPP_PHONE_ID: Optional[str] = Field(None, env="WHATSAPP_PHONE_ID")
    
    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
