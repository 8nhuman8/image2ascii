# Image2ASCII
### A program that converts images into ASCII art

## Table of contents
- [Example](#example)
- [Usage](#usage)
- [Command-line arguments description](#command-line-arguments-description)
- [Credits and references](#credits-and-references)
- [License](#license)

## Example
| **'In' image** | **'Out' text file** |
| - | - |
| ![github_logo_image](README_files/github_logo_image.jpg) | ![github_logo_ascii_image](README_files/github_logo_ascii_image.png) |

## Usage
1. Upgrade required packages with `pip install -r requirements.txt --upgrade` (if you don't have one, it will be automatically installed).
2. Check out all the command-line parameters [below](#command-line-arguments-description).
3. Run the `main.py` with `python main.py -i [path to image you want to convert] [parameters you need]`.

## Command-line arguments description
```
usage: main.py [-h] -i PATH [-s FLOAT] [-o PATH] [-c INT] [-ml]

This program converts an image into ASCII art.

optional arguments:
  -h, --help            show this help message and exit
  -i PATH, --in PATH    Image path.
  -s FLOAT, --scale FLOAT
                        Scale value.
  -o PATH, --out PATH   The path of the output file.
  -c INT, --cols INT    The number of columns.
  -ml, --more-levels    More grayscale levels will be used.
```

## Credits and references
Grayscale levels values taken from the [Paul Bourke's site](http://paulbourke.net/dataformats/asciiart/).

## License
[Image2ASCII](https://github.com/8nhuman8/image2ascii) specific code is distributed under [MIT License](LICENSE).

Copyright (c) 2020 Artyom Bezmenov
