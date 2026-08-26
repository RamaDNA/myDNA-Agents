from tavily import TavilyClient
from app.core.config import settings
from langchain_core.tools import tool

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)

@tool
def tavily_search(query: str) -> str:
    """
    Search the web using Tavily API.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    try:
        response = tavily_client.search(
            query,
            num_results=5,
            search_type="web")
        return response
    except Exception as e:
        return f"Error occurred while searching: {str(e)}"
