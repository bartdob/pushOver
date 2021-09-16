import asyncio
import os
load_dotenv()

from tracardi_pushover.plugin import PushoverAction

init = dict(
    url='https://api.pushover.net/1/messages.json',
    token=os.getenv('APP_TOKEN'),
    user=os.getenv('USER_KEY'),
    message="Helllo"
)

payload = {}


async def main():
    plugin = await PushoverAction.build(**init)



asyncio.run(main())
