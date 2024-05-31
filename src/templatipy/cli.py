from typing import Annotated

import copier
import typer
from rich import print

from templatipy.config import settings

app = typer.Typer(
    name="templatipy", help="Generate template for your python application"
)


@app.command()
def generate(
    template: Annotated[str, typer.Argument(help="The template type to be generated")],
    name: Annotated[str, typer.Option(prompt=True, help="Name of the project")],
):
    print(f"Generating {template} template into the project {name}...")
    copier.run_copy(f"gh:TianaNanta/{template}-template", ".")


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


def version_callback(value: bool):
    if value:
        print(f"Templatify [green]v{settings.VERSION}[/green]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show Templatify version information",
    )
): ...
