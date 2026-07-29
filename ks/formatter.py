from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

def print_pod_table(pods):
    """Print pod summary table."""
    table = Table(title="Pod Health Summary", box=box.ROUNDED)
    table.add_column("Namespace", style="cyan")
    table.add_column("Pod Name", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("Restarts", justify="right")
    
    for pod in pods:
        status = pod.status.phase
        restarts = pod.status.container_statuses[0].restart_count if pod.status.container_statuses else 0
        table.add_row(pod.metadata.namespace, pod.metadata.name, status, str(restarts))
    
    console.print(table)

def print_diagnosis(pod_name, namespace, issues):
    """Print diagnosis."""
    console.print(f"\n[bold yellow]Diagnosis for {pod_name} in {namespace}:[/]")
    if issues:
        for issue in issues:
            console.print(f"[red]• {issue}[/]")
    else:
        console.print("[green]No issues detected.[/]")

