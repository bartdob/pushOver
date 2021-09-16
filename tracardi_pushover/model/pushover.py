import aiohttp
import urllib.parse
from pydantic.main import BaseModel


class PayModel(BaseModel):
    token: str
    user: str
    message: str


class Connection(BaseModel):
    url: str = 'https://api.pushover.net/1/messages.json'
    payloads: PayModel
    head: str = {"Content-type": "application/x-www-form-urlencoded"},
    result = urllib.parse.urlencode(payloads)

    async def connect(self):
        async with aiohttp.ClientSession() as session:
            await session.post(url=self.url, data=self.result, headers=self.head)
