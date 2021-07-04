import os

import typer
from PIL import Image

from pymosaic_4k.config import OUTPUT_DIR

STAMP_WIDTH = 640
STAMP_HEIGHT = 360


def create_mosaic(folder: str) -> Image:
    stamps = []

    for image in os.listdir(folder):
        filepath = os.path.join(folder, image)
        stamps.append(Image.open(filepath, "r"))

    mosaic = Image.new(mode="RGB", size=(3840, 2160))

    with typer.progressbar(length=len(stamps), label="images pasted") as progress:
        for index, stamp in enumerate(stamps):
            mosaic.paste(
                stamp, ((index % 6) * STAMP_WIDTH, (index // 6) * STAMP_HEIGHT)
            )
            progress.update(1)
        typer.secho(
            f"Finished pasting {len(stamps)} images!", fg=typer.colors.BRIGHT_GREEN
        )

    return mosaic


def save_mosaic(filename: str, mosaic: Image) -> None:
    filepath = os.path.join(OUTPUT_DIR, f"{filename}.png")
    mosaic.save(filepath, "PNG")