import asyncio
import os
from dotenv import load_dotenv
from tracardi_pushover_webhook.plugin import PushoverAction

load_dotenv()


init = dict(
    token=os.getenv('API_TOKEN'),
    user=os.getenv('USER_KEY'),
    message="Test message"
)

payload = {}


async def main():
    plugin = PushoverAction(**init)
    result = await plugin.run(payload)
    print(result)

asyncio.run(main())