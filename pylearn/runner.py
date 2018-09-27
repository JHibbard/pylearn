# External Libraries
import click


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'],
                        max_content_width=80)


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option()
@click.pass_context
def cli(ctx):
    pass


@cli.command('hello', help='print a greeting to the terminal')
def hello():
    click.echo('Hello World!')
