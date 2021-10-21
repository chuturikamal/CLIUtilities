import click

@click.group()
def cli():
    pass

@cli.command(name="movie")
def MovieTransfer():
    click.echo('Name Display')

def callCommands():
    cli()