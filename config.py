from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Task Management API"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    database_url: str = "sqlite:///./tasks.db"
    
    class Config:
        env_file = ".env"


settings = Settings()
