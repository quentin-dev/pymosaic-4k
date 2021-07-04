# PyMosaic-4K

A simple python tool to create 4K mosaics.

## Requirements

- poetry

## Installation

- Clone the repository and `cd` into it
- `poetry install`

## Usage

- `poetry run mosaic FILENAME FOLDER`

with:

- `FILENAME`: the name of the file to be saved in `output`, will be a .png file
- `FOLDER`: the path to the folder containing the image to paste in the mosaic

example:

- `poetry run mosaic sample-mosaic tests/sample`
- The result will be `output/sample-mosaic.png`
