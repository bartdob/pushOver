import urllib.parse
import aiohttp
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_pushover_webhook.model.pushover_payload import PushOverPayload


class PushoverAction(ActionRunner):

    def __init__(self, **kwargs):
        self.pushover_payload = PushOverPayload(
            user=kwargs['user_key'],
            token=kwargs['api_token'],
            message=kwargs['message']
        )

    async def run(self, payload):
        print(self.pushover_payload.dict())
        async with aiohttp.ClientSession() as session:
            result = await session.post(url='https://api.pushover.net/1/messages.json',
                                        data=urllib.parse.urlencode(self.pushover_payload.dict()),
                                        headers={"Content-type": "application/x-www-form-urlencoded"})
            return Result(port="payload", value={
                "status": result.status,
                "body": await result.json()
            })


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='',
            className='pushover',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "api_token": None,
                "user_key": None,
                "message": None
            }

        ),
        metadata=MetaData(
            name='Pushover',
            desc='Connects to Pushover app.',
            type='flowNode',
            width=200,
            height=100,
            icon='pushover',
            group=["Connectors"]
        )
    )
