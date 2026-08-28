from langchain_qdrant import QdrantVectorStore
from app.integrations.gdrive.loader import load_gdrive_loader
from app.integrations.qdrant.qdrant_client import get_qdrant_client
from app.core.config import settings

qdrant_client = get_qdrant_client()

def load_gdrive_to_qdrant(folder_id: str):
    # Load Google Drive documents
    loader = load_gdrive_loader(folder_id)
    documents = loader.load()

    # Create a Qdrant vector store
    vector_store = QdrantVectorStore(
        client=qdrant_client,
        collection_name=settings.QDRANT_COLLECTION_NAME_GDRIVE,
        embedding=settings.OLLAMA_EMBEDDINGS_MODEL,
        distance="Cosine",
        vector_size=settings.QDRANT_DIMENSIONS_STORE,
    )

    # Add documents to the Qdrant vector store
    vector_store.add_documents(documents)