from pydantic_settings import BaseSettings , SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    #ollama settings
    OLLAMA_API_KEY: str | None = None
    OLLAMA_LOCAL_LLM: str | None = None
    OLLAMA_CLOUD_LLM: str | None = None
    ## Ollama embeddings settings
    OLLAMA_EMBEDDINGS_MODEL: str | None = None

    #Qdrant settings
    QDRANT_API_KEY: str | None = None
    QDRANT_HOST: str | None = None

    #Tavily settings
    TAVILY_API_KEY: str | None = None

    # Database settings
    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_USER: str | None = None
    DB_PASSWORD: str | None = None
    DB_NAME: str | None = None

    # Google Drive settings
    GOOGLE_DRIVE_FOLDER_ID: str | None = None
    GOOGLE_DRIVE_CREDENTIALS_PATH: str | None = None
    GOOGLE_DRIVE_TOKEN_PATH: str | None = None
    ## Qdrant google drive settings
    QDRANT_COLLECTION_NAME_GDRIVE: str | None = None
    QDRANT_DIMENSIONS_STORE: int | None = None

    # JWT settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

settings = Settings()