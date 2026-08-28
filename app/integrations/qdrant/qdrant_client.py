from qdrant_client import QdrantClient
from app.core.config import settings

def get_qdrant_client() -> QdrantClient:
    qdrant_api_key = settings.QDRANT_API_KEY
    qdrant_host = settings.QDRANT_HOST

    return QdrantClient(
        url=qdrant_host,
        api_key=qdrant_api_key
    )


