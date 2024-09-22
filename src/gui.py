import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Entry, Button, Style, Frame, Combobox
import threading
import os
from .processing import bulk_rename_images


class BulkRenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk Rename Images")
        self.root.geometry("700x730")
        self.style = Style()
        self.style.configure("TLabel", font=("Poppins", 12), background="#f0f0f0")
        self.style.configure(
            "TButton", font=("Poppins", 12), background="#4CAF50", foreground="black"
        )
        self.style.configure("TEntry", font=("Poppins", 12), padding=10)
        self.root.configure(background="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Configure grid columns to stretch
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)

        # Title
        title_frame = Frame(self.root, padding="10", style="TFrame")
        title_frame.grid(row=0, column=0, columnspan=3, pady=10, sticky="ew")
        title_label = tk.Label(
            title_frame,
            text="Bulk Rename Images",
            font=("Poppins", 16, "bold"),
            background="#f0f0f0",
        )
        title_label.pack()

        # Source folder
        source_frame = Frame(self.root, padding="10", style="TFrame")
        source_frame.grid(row=1, column=0, columnspan=3, pady=5, sticky="ew")
        source_frame.columnconfigure(0, weight=1)
        self.source_folder_entry = Entry(source_frame)
        self.source_folder_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.source_folder_entry.insert(0, "Source Folder")
        Button(
            source_frame,
            text="Browse",
            command=lambda: self.browse_folder(self.source_folder_entry),
        ).grid(row=0, column=1, padx=10, pady=5)

        # Destination folder
        destination_frame = Frame(self.root, padding="10", style="TFrame")
        destination_frame.grid(row=2, column=0, columnspan=3, pady=5, sticky="ew")
        destination_frame.columnconfigure(0, weight=1)
        self.destination_folder_entry = Entry(destination_frame)
        self.destination_folder_entry.grid(
            row=0, column=0, padx=10, pady=5, sticky="ew"
        )
        self.destination_folder_entry.insert(0, "Destination Folder")
        Button(
            destination_frame,
            text="Browse",
            command=lambda: self.browse_folder(self.destination_folder_entry),
        ).grid(row=0, column=1, padx=10, pady=5)

        # Main name
        main_name_frame = Frame(self.root, padding="10", style="TFrame")
        main_name_frame.grid(row=3, column=0, columnspan=3, pady=5, sticky="ew")
        main_name_frame.columnconfigure(0, weight=1)
        self.main_name_entry = Entry(main_name_frame)
        self.main_name_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.main_name_entry.insert(0, "Main Name")

        # Start number
        start_number_frame = Frame(self.root, padding="10", style="TFrame")
        start_number_frame.grid(row=4, column=0, columnspan=3, pady=5, sticky="ew")
        start_number_frame.columnconfigure(0, weight=1)
        self.start_number_entry = Entry(start_number_frame)
        self.start_number_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.start_number_entry.insert(0, "Start Number")

        # Target format
        format_frame = Frame(self.root, padding="10", style="TFrame")
        format_frame.grid(row=5, column=0, columnspan=3, pady=5, sticky="ew")
        format_frame.columnconfigure(0, weight=1)
        tk.Label(format_frame, text="Target Format:", background="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.format_combobox = Combobox(
            format_frame, values=["jpg", "png", "webp", "jpeg"], state="readonly"
        )
        self.format_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        self.format_combobox.current(0)

        # Rename convention
        rename_convention_frame = Frame(self.root, padding="10", style="TFrame")
        rename_convention_frame.grid(row=6, column=0, columnspan=3, pady=5, sticky="ew")
        rename_convention_frame.columnconfigure(0, weight=1)
        tk.Label(
            rename_convention_frame, text="Rename Convention:", background="#f0f0f0"
        ).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.rename_convention_combobox = Combobox(
            rename_convention_frame,
            values=["main_name_index", "index_main_name"],
            state="readonly",
        )
        self.rename_convention_combobox.grid(
            row=0, column=1, padx=10, pady=5, sticky="ew"
        )
        self.rename_convention_combobox.current(0)

        # Progress bar
        progress_frame = Frame(self.root, padding="10", style="TFrame")
        progress_frame.grid(row=7, column=0, columnspan=3, pady=20, sticky="ew")
        self.progress_bar = Progressbar(
            progress_frame, orient=tk.HORIZONTAL, length=600, mode="determinate"
        )
        self.progress_bar.pack(fill="x")

        # Status label
        status_frame = Frame(self.root, padding="10", style="TFrame")
        status_frame.grid(row=8, column=0, columnspan=3, pady=5, sticky="ew")
        self.status_label = tk.Label(
            status_frame, text="", font=("Poppins", 10), background="#f0f0f0"
        )
        self.status_label.pack()

        # Start button
        start_button_frame = Frame(self.root, padding="10", style="TFrame")
        start_button_frame.grid(row=9, column=0, columnspan=3, pady=20, sticky="ew")
        Button(start_button_frame, text="Start", command=self.start_bulk_rename).pack()

    def browse_folder(self, entry):
        folder_selected = filedialog.askdirectory()
        entry.delete(0, tk.END)
        entry.insert(0, folder_selected)

    def start_bulk_rename(self):
        source_folder = self.source_folder_entry.get()
        destination_folder = self.destination_folder_entry.get()
        main_name = self.main_name_entry.get()
        start_number = self.start_number_entry.get()
        target_format = self.format_combobox.get()
        rename_convention = self.rename_convention_combobox.get()

        # Validate inputs
        if (
            not source_folder
            or not destination_folder
            or not main_name
            or not start_number
            or not target_format
            or not rename_convention
        ):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            start_number = int(start_number)
        except ValueError:
            messagebox.showerror("Error", "Start number must be an integer.")
            return

        self.progress_bar["value"] = 0
        self.progress_bar["maximum"] = 100
        self.status_label.config(text="Processing...")

        def progress_callback(current, total):
            self.progress_bar["value"] = (current / total) * 100
            self.root.update_idletasks()

        def run_bulk_rename():
            try:
                bulk_rename_images(
                    source_folder,
                    destination_folder,
                    main_name,
                    start_number,
                    target_format,
                    rename_convention,
                    progress_callback,
                )
                messagebox.showinfo(
                    "Success",
                    "Images have been renamed, converted, and copied successfully.",
                )
                os.startfile(destination_folder)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                self.status_label.config(text="")

        threading.Thread(target=run_bulk_rename).start()


def run_app():
    root = tk.Tk()
    app = BulkRenameApp(root)
    root.mainloop()
