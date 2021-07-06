# PyMosaic-4K

A simple python tool to create 4K mosaics.

Made to create a *3840x2160* mosaic from 36 *640x360* images.

## Requirements

- poetry

## Installation

- Clone the repository and `cd` into it
- `poetry install`

## Usage

- `poetry run mosaic FILENAME FOLDER`

with:

### Arguments

- `FILENAME`: the name of the file to be saved in `output`, will be a .png file
- `FOLDER`: the path to the folder containing the image to paste in the mosaic

### Options

- `--resize / --no-resize`: whether or not to resize the images, defaults to `True`

example:

- `poetry run mosaic sample-mosaic tests/sample`
- The result will be `output/sample-mosaic.png`
