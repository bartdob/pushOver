from pydantic import BaseModel


class PushOverPayload(BaseModel):
    token: str
    user: str
    message: str
