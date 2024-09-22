import os
import shutil


def bulk_rename_images(
    source_folder, destination_folder, main_name, start_number, progress_callback=None
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
        )
        if progress_callback:
            progress_callback(index + 1, total_files)
    print("Images have been renamed and copied successfully.")


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
    file_name, source_folder, destination_folder, main_name, new_index
):
    new_name = f"{main_name}{new_index:05d}{os.path.splitext(file_name)[1]}"
    shutil.copy(
        os.path.join(source_folder, file_name),
        os.path.join(destination_folder, new_name),
    )
