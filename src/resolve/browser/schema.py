from pydantic import BaseModel


class BrowserSchema(BaseModel):
    url: str
