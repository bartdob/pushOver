import http.client, urllib
import aiohttp
from dotenv import load_dotenv
import sys
import os
load_dotenv()


def pushover():
    print("START")
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": os.getenv('APP_TOKEN'),
                     "user": os.getenv('USER_KEY'),
                     "message": "hello world",
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    conn.getresponse()
    print("END PROGRAM")



# import aiohttp
# import asyncio
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:
#
#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])
#
#             html = await response.text()
#             print("Body:", html[:15], "...")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())