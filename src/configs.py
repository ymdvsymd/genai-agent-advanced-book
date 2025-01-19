from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    openai_api_base: str
    # openai_api_version: str
    openai_model: str
