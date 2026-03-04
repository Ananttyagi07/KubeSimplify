import click

@click.group()
def cli():
    """KubeSimplify CLI"""
    pass


@cli.command()
def hello():
    """Test command"""
    print("Welcome to KubeSimplify ")


if __name__ == "__main__":
    cli()