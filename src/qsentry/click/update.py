import click


from .main import (
    add_common_options,
    common_options,
    main,
)
from ..commands import ProjectsCommand


@main.group(invoke_without_command=True)
def update(*args, **kwargs):
    """Update a resource such as a client key"""
    pass


@update.command()
@add_common_options(common_options)
@click.option(
    "--project",
    required=True,
    help="""The project slug""",
)
@click.option(
    "--id",
    "key_id",
    required=True,
    help="""The id of the client key to be updated""",
)
@click.option(
    "--data",
    required=True,
    help="""The JSON data used to update the key""",
)
def client_key(**kwargs):
    """Update a client key."""
    ProjectsCommand(**kwargs).update_key(
        kwargs["project"], kwargs["key_id"], kwargs["data"]
    )
