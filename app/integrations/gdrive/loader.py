from app.core.config import settings

from langchain_googledrive import GoogleDriveLoader


# load gdrive (folder method) loader
def load_gdrive_loader(folder_id: str) -> GoogleDriveLoader:
    # define credetials and token path
    credentials_path = settings.GOOGLE_DRIVE_CREDENTIALS_PATH
    token_path = settings.GOOGLE_DRIVE_TOKEN_PATH
    
    loader = GoogleDriveLoader(
        folder_id=folder_id,
        credentials_path=credentials_path,
        token_path=token_path,
    )
    return loader