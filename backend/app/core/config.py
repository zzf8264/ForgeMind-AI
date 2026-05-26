from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "development"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    postgres_url: str = "postgresql+psycopg://forgemind:forgemind@postgres:5432/forgemind"
    redis_url: str = "redis://redis:6379/0"
    qdrant_url: str = "http://qdrant:6333"
    cors_origins: list[str] = ["http://localhost:3000", "http://127.0.0.1:3000"]


settings = Settings()
