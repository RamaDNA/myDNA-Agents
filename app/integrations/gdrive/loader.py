from app.core.config import settings

from langchain_googledrive import GoogleDriveLoader

folder_id = settings.GOOGLE_DRIVE_FOLDER_ID
credentials_path = settings.GOOGLE_DRIVE_CREDENTIALS_PATH
token_path = settings.GOOGLE_DRIVE_TOKEN_PATH

# load gdrive (folder method) loader
def load_gdrive_loader(folder_id: str) -> GoogleDriveLoader:
    loader = GoogleDriveLoader(
        folder_id=folder_id,
        credentials_path=credentials_path,
        token_path=token_path,
    )
    return loader