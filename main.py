import click
from ks.commands import pods_command, diagnose_command

@click.group()
def cli():
    """KubeSimplify CLI - Simplify Kubernetes operations."""
    pass


@cli.command()
def hello():
    """Test command"""
    print("Welcome to KubeSimplify!")


@cli.command()
def pods():
    """Show pod health summary."""
    try:
        pods_command()
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('namespace')
@click.argument('pod_name')
def diagnose(namespace, pod_name):
    """Diagnose a specific pod."""
    try:
        diagnose_command(namespace, pod_name)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('name')
def generate(name):
    """Generate basic deployment YAML."""
    yaml = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
      - name: {name}
        image: nginx:latest
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: {name}
spec:
  selector:
    app: {name}
  ports:
  - port: 80
    targetPort: 80"""
    click.echo(yaml)


if __name__ == "__main__":
    cli()

