from os import path

from PIL import Image

from pymosaic_4k.logic import mosaic as mosaic_logic
from tests.config import ROOT_TEST_DIR

COLORS = [
    (0, 0, 255),
    (0, 255, 255),
    (0, 255, 0),
    (255, 0, 255),
    (255, 0, 0),
    (255, 255, 0),
]


def test_mosaic_creation():
    image: Image = mosaic_logic.create_mosaic(path.join(ROOT_TEST_DIR, "sample"))

    for y in range(0, 2160):
        for x in range(0, 3840):

            rgb = image.getpixel((x, y))
            expected = COLORS[y // 360]

            assert rgb == expected
