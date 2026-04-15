from pydantic import BaseModel

class FileResponse(BaseModel):
    file_id: str
    filename: str
    file_url: str
    size: int
