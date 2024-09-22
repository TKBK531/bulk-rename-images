import os
import shutil
from PIL import Image


def bulk_rename_images(
    source_folder,
    destination_folder,
    main_name,
    start_number,
    target_format,
    progress_callback=None,
):
    create_destination_folder(destination_folder)
    files = list_files(source_folder)
    total_files = len(files)
    for index, file_name in enumerate(files):
        rename_and_copy_file(
            file_name,
            source_folder,
            destination_folder,
            main_name,
            start_number + index,
            target_format,
        )
        if progress_callback:
            progress_callback(index + 1, total_files)
    print("Images have been renamed, converted, and copied successfully.")


def create_destination_folder(destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)


def list_files(source_folder):
    files = [
        f
        for f in os.listdir(source_folder)
        if os.path.isfile(os.path.join(source_folder, f))
    ]
    files.sort()  # Sort files to maintain order
    return files


def rename_and_copy_file(
    file_name, source_folder, destination_folder, main_name, new_index, target_format
):
    new_name = f"{main_name}{new_index:05d}.{target_format}"
    source_path = os.path.join(source_folder, file_name)
    destination_path = os.path.join(destination_folder, new_name)

    # Check if the file is already in the target format
    if file_name.lower().endswith(f".{target_format}"):
        shutil.copy(source_path, destination_path)
    else:
        with Image.open(source_path) as img:
            img.convert("RGB").save(destination_path, target_format.upper())
