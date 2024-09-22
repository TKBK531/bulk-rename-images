import os
import shutil


def bulk_rename_images():
    # Get user inputs
    # source_folder = r"E:\UOP\Ambalam\New folder (2)"
    # destination_folder = r"E:\UOP\Ambalam\New folder (2)\New folder"
    # main_name = "Documents"
    # start_number = 1

    source_folder_path = input("Enter the source folder path: ")
    source_folder = rf"{source_folder_path}"
    destination_folder_path = input("Enter the destination folder path: ")
    destination_folder = rf"{destination_folder_path}"
    main_name = input("Enter the main name for the images: ")
    start_number = int(input("Enter the starting number for the naming sequence: "))

    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # List all files in the source folder
    files = [
        f
        for f in os.listdir(source_folder)
        if os.path.isfile(os.path.join(source_folder, f))
    ]
    files.sort()  # Sort files to maintain order

    # Rename and copy files
    for index, file_name in enumerate(files):
        # Generate new name
        new_name = (
            f"{main_name}{start_number + index:05d}{os.path.splitext(file_name)[1]}"
        )
        # Copy file to destination folder with new name
        shutil.copy(
            os.path.join(source_folder, file_name),
            os.path.join(destination_folder, new_name),
        )

    print("Images have been renamed and copied successfully.")


if __name__ == "__main__":
    bulk_rename_images()
