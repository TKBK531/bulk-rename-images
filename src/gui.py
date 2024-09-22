import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar, Label, Entry, Button, Style, Frame
import threading
import os
from .processing import bulk_rename_images


class BulkRenameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bulk Rename Images")
        self.root.geometry("1050x680")
        self.style = Style()
        self.style.configure("TLabel", font=("Poppins", 12), background="#f0f0f0")
        self.style.configure(
            "TButton", font=("Poppins", 12), background="#4CAF50", foreground="black"
        )
        self.style.configure("TEntry", font=("Poppins", 12), padding=10)
        self.root.configure(background="#f0f0f0")
        self.create_widgets()

    def create_widgets(self):
        # Title
        title_frame = Frame(self.root, padding="10", style="TFrame")
        title_frame.grid(row=0, column=0, columnspan=3, pady=10)
        title_label = Label(
            title_frame,
            text="Bulk Rename Images",
            font=("Poppins", 16, "bold"),
            background="#f0f0f0",
        )
        title_label.pack()

        # Source folder
        source_frame = Frame(self.root, padding="10", style="TFrame")
        source_frame.grid(row=1, column=0, columnspan=3, pady=5, sticky="w")
        Label(source_frame, text="Source Folder:", background="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.source_folder_entry = Entry(source_frame, width=70)
        self.source_folder_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)
        Button(
            source_frame,
            text="Browse",
            command=lambda: self.browse_folder(self.source_folder_entry),
        ).grid(row=0, column=2, padx=10, pady=5)

        # Destination folder
        destination_frame = Frame(self.root, padding="10", style="TFrame")
        destination_frame.grid(row=2, column=0, columnspan=3, pady=5, sticky="w")
        Label(destination_frame, text="Destination Folder:", background="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.destination_folder_entry = Entry(destination_frame, width=70)
        self.destination_folder_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)
        Button(
            destination_frame,
            text="Browse",
            command=lambda: self.browse_folder(self.destination_folder_entry),
        ).grid(row=0, column=2, padx=10, pady=5)

        # Main name
        main_name_frame = Frame(self.root, padding="10", style="TFrame")
        main_name_frame.grid(row=3, column=0, columnspan=3, pady=5, sticky="w")
        Label(main_name_frame, text="Main Name:", background="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.main_name_entry = Entry(main_name_frame, width=70)
        self.main_name_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

        # Start number
        start_number_frame = Frame(self.root, padding="10", style="TFrame")
        start_number_frame.grid(row=4, column=0, columnspan=3, pady=5, sticky="w")
        Label(start_number_frame, text="Start Number:", background="#f0f0f0").grid(
            row=0, column=0, padx=10, pady=5, sticky="w"
        )
        self.start_number_entry = Entry(start_number_frame, width=70)
        self.start_number_entry.grid(row=0, column=1, padx=10, pady=5, ipady=5)

        # Progress bar
        progress_frame = Frame(self.root, padding="10", style="TFrame")
        progress_frame.grid(row=5, column=0, columnspan=3, pady=20)
        self.progress_bar = Progressbar(
            progress_frame, orient=tk.HORIZONTAL, length=1000, mode="determinate"
        )
        self.progress_bar.pack()

        # Status label
        status_frame = Frame(self.root, padding="10", style="TFrame")
        status_frame.grid(row=6, column=0, columnspan=3, pady=5)
        self.status_label = Label(
            status_frame, text="", font=("Poppins", 10), background="#f0f0f0"
        )
        self.status_label.pack()

        # Start button
        start_button_frame = Frame(self.root, padding="10", style="TFrame")
        start_button_frame.grid(row=7, column=0, columnspan=3, pady=20)
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

        # Validate inputs
        if (
            not source_folder
            or not destination_folder
            or not main_name
            or not start_number
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
                    progress_callback,
                )
                messagebox.showinfo(
                    "Success", "Images have been renamed and copied successfully."
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
