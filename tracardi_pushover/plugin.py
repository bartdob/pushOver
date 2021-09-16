import json
from datetime import datetime, date
from typing import Optional

from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_pushover.model.pushover import Connection


class PushoverAction(ActionRunner):
    @staticmethod
    async def build(**kwargs) -> 'PushoverAction':
        plugin = PushoverAction(**kwargs)
        connection = Connection(**kwargs)

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
                "token": None,
                "user": None,
                "Message": None
            }

        ),
        metadata=MetaData(
            name='Pushover',
            desc='Connects to Pushover app.',
            type='flowNode',
            width=200,
            height=100,
            icon='#',
            group=["Connectors"]
        )
    )
