import urllib.parse
import aiohttp
import asyncio

from tracardi.domain.resource import Resource
from tracardi.service.storage.driver import storage
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_pushover_webhook.model.pushover_payload import PushOverConfiguration, PushOverAuth


class PushoverAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'PushoverAction':
        config = PushOverConfiguration(**kwargs)
        source = await storage.driver.resource.load(config.source.id)
        return PushoverAction(config, source)

    def __init__(self, config: PushOverConfiguration, source: Resource):
        self.pushover_config = config
        self.source = PushOverAuth(**source.config)

    async def run(self, payload):
        async with aiohttp.ClientSession() as session:

            data = {
                "token": self.source.token,
                "user": self.source.user,
                "message": self.pushover_config.message
            }

            result = await session.post(url='https://api.pushover.net/1/messages.json',
                                        data=urllib.parse.urlencode(data),
                                        headers={"Content-type": "application/x-www-form-urlencoded"})
            return Result(port="payload", value={
                "status": result.status,
                "body": await result.json()
            })


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_pushover_webhook.plugin',
            className='PushoverAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
                "source": {
                    "id": None
                },
                "message": None
            }

        ),
        metadata=MetaData(
            name='Pushover webhook',
            desc='Connects to Pushover app.',
            type='flowNode',
            width=200,
            height=100,
            icon='pushover',
            group=["Connectors"]
        )
    )
