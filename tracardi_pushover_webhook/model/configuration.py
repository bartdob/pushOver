from pydantic import BaseModel


class Configuration(BaseModel):
    token: str
    user: str
    message: str
