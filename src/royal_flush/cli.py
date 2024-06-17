"""Console script for royal_flush."""
import royal_flush

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for royal_flush."""
    console.print("Replace this message by putting your code into "
               "royal_flush.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
