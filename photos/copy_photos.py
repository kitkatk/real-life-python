from os import listdir, path
import shutil


def copy_files_by_name(source_dir: str, subset_def_dir: str, output_dir: str):
    """
    Real life scenario:
    - Suppose you have two versions of photos - high quality and low quality, each in its folder,
    and the filenames are the same in both.
    - Suppose you created a subset of the high quality photos in a third folder, e.g. for an album.
    - You found out the album would be too large.
    - Now want to create the same subset of the low quality photos.

    This scripts selects files from a folder that have the same filenames as files in another folder.

    :param source_dir: directory containing all photos
    :param subset_def_dir: directory containing the subset you already created
    :param output_dir: directory for saving the photos selected from source_dir
    """

    for f in listdir(subset_def_dir):
        original = path.join(source_dir, f)
        target = path.join(output_dir, f)
        shutil.copyfile(original, target)


if __name__ == '__main__':
    source = '<your source dir>'
    subset_def = '<your selection dir>'
    output = '<output dir>'

    copy_files_by_name(source, subset_def, output)
