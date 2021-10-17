import os
from exif import Image


def add_tz(image: Image, tz: str):
    """
    Change timezone of time_original to tz.
    """
    tz_tag = 'offset_time_original'
    if tz_tag in dir(image):
        image[tz_tag] = tz

    return image


def tz_to_metadata(in_dir: str, out_dir: str, tz: str, sort_by_name=True):
    """
    Set correct the timezone for all files in directory that contain timezone in metadata.
    It's not possible to set the attribute if it doesn't exist.
    """
    files = [f for f in os.listdir(in_dir) if f != '.DS_Store']
    if sort_by_name:
        files.sort()

    for i, file in enumerate(files):
        with open(os.path.join(in_dir, file), "rb") as f:
            image = Image(f)

        image = add_tz(image, tz)

        with open(os.path.join(out_dir, file), "wb") as f:
            f.write(image.get_file())


def diagnostics(directory: str):
    """
    Print diagnostics for the first 10 files in a directory.
    """
    files = [f for f in os.listdir(directory) if f != '.DS_Store']
    files.sort()
    for i, file in enumerate(files):
        if i < 10:
            with open(os.path.join(directory, file), "rb") as f:
                image = Image(f)
            print(f)
            print(image['datetime_original'])
            if 'offset_time_original' in dir(image):
                print(image['offset_time_original'])
            # print("\n".join(dir(image)))
            print()


if __name__ == '__main__':
    in_directory = '<your input dir>'
    out_directory = f"{in_directory}_tz"
    tz='+02:00'

    tz_to_metadata(in_directory, out_directory, tz)

    # Check the metadata of files in the output directory
    diagnostics(out_directory)
