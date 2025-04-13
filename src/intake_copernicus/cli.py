"""Console script for intake_copernicus."""
import intake_copernicus

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for intake_copernicus."""
    console.print("Replace this message by putting your code into "
               "intake_copernicus.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
