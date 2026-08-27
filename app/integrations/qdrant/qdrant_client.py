from qdrant_client import QdrantClient
from app.core.config import settings

qdrant_api_key = settings.QDRANT_API_KEY
qdrant_host = settings.QDRANT_HOST

def get_qdrant_client() -> QdrantClient:
    """
    Get a Qdrant client instance.

    Returns:
        QdrantClient: An instance of the Qdrant client.
    """
    return QdrantClient(
        url=qdrant_host,
        api_key=qdrant_api_key
    )

qdrant_client = get_qdrant_client()


