from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner


class pushOver(ActionRunner):


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='',
            className='pushover',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1.2',
            license="MIT",
            author="Bartosz Dobrosielski",
            init={
            }

        ),
        metadata=MetaData(
            name='Redshift connector',
            desc='Connects to redshift and reads data.',
            type='flowNode',
            width=200,
            height=100,
            icon='postgres',
            group=["Connectors"]
        )
    )
