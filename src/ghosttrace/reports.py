from rich.console import Console
from rich.table import Table


console = Console()


def generate_report(history):
    console.print("\n[bold cyan]GhostTrace Report[/bold cyan]\n")

    table = Table(show_header=True, header_style="bold magenta")

    table.add_column("Step")
    table.add_column("Operation")
    table.add_column("Shape")
    table.add_column("Timestamp")

    for index, snapshot in enumerate(history, start=1):
        table.add_row(
            str(index),
            snapshot["operation"],
            str(snapshot["shape"]),
            snapshot["timestamp"].strftime("%H:%M:%S"),
        )

    console.print(table)

    if len(history) >= 1:

        latest = history[-1]

        console.print("\n[bold green]Operation Timeline[/bold green]\n")

        for index, snapshot in enumerate(history, start=1):
            console.print(
                f"[cyan]{index}[/cyan]. {snapshot['operation']}"
            )