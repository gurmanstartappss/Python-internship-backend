from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str
    ADMIN_EMAIL: str
    COMPANY_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )