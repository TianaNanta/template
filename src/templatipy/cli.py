import typer
from rich import print

from templatipy.config import settings

app = typer.Typer(name="templatipy")


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


@app.command()
def version():
    print(f"Templatify [green]v{settings.VERSION}[/green]")
