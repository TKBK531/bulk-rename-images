
# Bulk Rename Images

Bulk Rename Images is a simple GUI application built with Python and Tkinter that allows users to rename and copy images in bulk. The application provides an easy-to-use interface to select source and destination folders, specify a main name and starting number for the renamed images, and track the progress of the renaming process.

## Description

Bulk Rename Images is a user-friendly application designed to simplify the process of renaming and copying multiple images at once. This tool is particularly useful for photographers, graphic designers, and anyone who needs to manage large collections of images efficiently.

The application provides a graphical user interface (GUI) built with Python's Tkinter library, allowing users to:

- Select a source folder containing the images to be renamed.
- Choose a destination folder where the renamed images will be saved.
- Specify a main name for the renamed images.
- Set a starting number for the sequence of renamed images.

As the renaming process progresses, a progress bar updates to show the current status, and upon completion, the application displays a success message and automatically opens the destination folder. If any errors occur during the process, an error message is displayed to inform the user.

This project aims to provide a simple yet powerful solution for bulk image renaming, making it easier to organize and manage image files.

## Features

- Select source and destination folders using a file dialog.
- Specify a main name and starting number for the renamed images.
- Track the progress of the renaming process with a progress bar.
- Display success or error messages upon completion.
- Automatically open the destination folder after the renaming process is complete.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `processing.py` module with the `bulk_rename_images` function

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bulk-rename-images.git
   cd bulk-rename-images
   ```

2. Ensure you have the required dependencies installed. If not, install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the `processing.py` module is in the same directory as the main script or properly referenced.

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. The GUI window will open. Follow these steps to rename images in bulk:

   - Click the "Browse" button next to the "Source Folder" field to select the folder containing the images you want to rename.
   - Click the "Browse" button next to the "Destination Folder" field to select the folder where the renamed images will be saved.
   - Enter the main name for the renamed images in the "Main Name" field.
   - Enter the starting number for the renamed images in the "Start Number" field.
   - Click the "Start" button to begin the renaming process.

3. The progress bar will update to show the progress of the renaming process. Once complete, a success message will be displayed, and the destination folder will open automatically.

## Project Structure

```plaintext
bulk-rename-images/
│
├── src/
│   ├── gui.py       # Contains the BulkRenameApp class that defines the GUI and its functionality.
│   └── processing.py  # Contains the bulk_rename_images function that performs the renaming and copying of images.
│
├── main.py        # Entry point to run the application.
├── requirements.txt  # Lists the required dependencies for the project.
└── README.md       # Project documentation.
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
