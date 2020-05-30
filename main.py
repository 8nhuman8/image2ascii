from PIL import Image
import numpy as np
from argparse import ArgumentParser, Namespace

from json import load


class ImageSizeException(Exception): pass


def get_average_luminance(image: Image) -> float:
    image_array = np.array(image)
    width, height = image_array.shape
    return np.average(image_array.reshape(width * height))


def convert_image_to_ascii(image_path: str, cols: int, scale: float, more_levels: bool) -> list:
    with open('config.json', 'r') as json_file:
        data = load(json_file)
    gray_scale_level_10 = data['gray_scale_level_10']
    gray_scale_level_70 = data['gray_scale_level_70']

    image = Image.open(image_path).convert('L')

    image_width, image_height = image.size[0], image.size[1]
    print(f'Input image dims: {image_width}x{image_height}')

    tile_width = image_width / cols
    tile_height = tile_width / scale

    rows = int(image_height / tile_height)

    print(f'Cols: {cols}, rows: {rows}')
    print(f'Tile dims: {tile_width}x{tile_height}')

    if cols > image_width or rows > image_height:
        raise ImageSizeException('Image too small for specified cols')

    ascii_image = []
    for j in range(rows):
        y1 = int(j * tile_height)
        y2 = int((j + 1) * tile_height)

        if j == rows - 1:
            y2 = image_height

        ascii_image.append('')

        for i in range(cols):

            x1 = int(i * tile_width)
            x2 = int((i + 1) * tile_width)

            if i == cols - 1:
                x2 = image_width

            image_tile = image.crop((x1, y1, x2, y2))
            average_luminance = int(get_average_luminance(image_tile))

            if more_levels:
                gray_scale_value = gray_scale_level_70[int((average_luminance * 69) / 255)]
            else:
                gray_scale_value = gray_scale_level_10[int((average_luminance * 9) / 255)]

            ascii_image[j] += gray_scale_value

    return ascii_image


def parse_args() -> Namespace:
    parser = ArgumentParser(description='This program converts an image into ASCII art.')
    parser.add_argument('-i', '--in', metavar='PATH', dest='image_path',
                        type=str, required=True, help='Image path.')
    parser.add_argument('-s', '--scale', metavar='FLOAT', type=float, default=0.6,
                        help='Scale value.')
    parser.add_argument('-o', '--out', metavar='PATH', dest='out_txt_path',
                        type=str, default='out.txt',
                        help='The path of the output file.')
    parser.add_argument('-c', '--cols', metavar='INT', type=int, default=50,
                        help='The number of columns.')
    parser.add_argument('-ml', '--more-levels', action='store_true',
                        help='More grayscale levels will be used.')
    return parser.parse_args()


def create_ascii_image(args: Namespace) -> None:
    args = parse_args()

    ascii_image = convert_image_to_ascii(args.image_path, args.cols, args.scale, args.more_levels)

    with open(args.out_txt_path, 'w') as out_txt:
        for row in ascii_image:
            out_txt.write(row + '\n')

    print(f'ASCII art written to {args.out_txt_path}')


if __name__ == '__main__':
    args = parse_args()
    create_ascii_image(args)
