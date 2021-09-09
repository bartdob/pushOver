import http.client, urllib
from dotenv import load_dotenv
import os
import aiohttp
import asyncio
import urllib.parse
load_dotenv()


def pushover():
    print("START")

    url = "https://api.pushover.net/1/messages.json"
    payload = {"token": os.getenv('APP_TOKEN'),
               "user": os.getenv('USER_KEY'),
               "message": "Helllo"}
    result = urllib.parse.urlencode(payload)
    head = {"Content-type": "application/x-www-form-urlencoded"}

    print(url, payload, result)

    async def main():
        print("START")
        async with aiohttp.ClientSession() as session:
            await session.post(url, data=result, headers=head)

    asyncio.run(main())

