import os

import typer

from pymosaic_4k.logic import mosaic as mosaic_logic

app = typer.Typer()


@app.command()
def create_mosaic(filename: str, folder: str):

    if not os.path.isdir(folder):
        typer.secho(
            f'"{folder}" is not a folder, exiting', err=True, fg=typer.colors.BRIGHT_RED
        )
        raise typer.Exit(code=1)

    image = mosaic_logic.create_mosaic(folder=folder)
    mosaic_logic.save_mosaic(filename=filename, mosaic=image)
