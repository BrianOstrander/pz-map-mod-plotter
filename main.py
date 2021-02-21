import sys, png
from pathlib import Path

CELL_EXTENSION = '.lotheader'
WIDTH = 75
HEIGHT = 75

def analyze_mod(path, export_path):
    maps_path = path.joinpath('media/maps')
    if not maps_path.is_dir():
        print('No valid maps found for mod {}'.format(path.name))
        return

    image_array = [[0 for y in range(HEIGHT)] for x in range(WIDTH)]

    for current_path in maps_path.iterdir():
        if current_path.is_dir():
            for current_file in current_path.iterdir():
                if current_file.name.endswith(CELL_EXTENSION):
                    coordinates = current_file.stem.split('_')
                    x = int(coordinates[0]) - 1
                    y = int(coordinates[1]) - 1

                    try:
                        image_array[y][x] = 255
                    except:
                        print('Out of range value: ( {} , {} )'.format(x, y))

    image_file = open(export_path.joinpath('{}.png'.format(path.name)), 'wb')
    image = png.Writer(WIDTH, HEIGHT)

    image.write(image_file, image_array)
    image_file.close()

def main():
    root_path = Path(sys.path[0])
    resource_path = root_path.joinpath('mods')

    if not resource_path.exists():
        print('Unable to find mods directory')
        return

    export_path = root_path.joinpath('exports')

    if not export_path.exists():
        export_path.mkdir()

    for path in resource_path.iterdir():
        if path.is_dir():
            analyze_mod(path, export_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()