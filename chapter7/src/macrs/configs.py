from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

print(Path(__file__).resolve().parent.parent.parent / ".env")


class Settings(BaseSettings):
    OPENAI_API_KEY: str
    OPENAI_MODEL: str
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).resolve().parent.parent.parent / ".env"),
        extra="ignore",
    )
