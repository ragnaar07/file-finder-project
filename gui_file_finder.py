import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import time
from file_searcher import find_file


class FileFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔍 File Finder Tool")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Title
        tk.Label(
            root, text="File Finder Tool", font=("Arial", 18, "bold"), fg="#2c3e50"
        ).pack(pady=10)

        # Filename Entry
        tk.Label(root, text="Enter filename:", font=("Arial", 12)).pack(pady=5)
        self.filename_entry = tk.Entry(root, width=50, font=("Arial", 11))
        self.filename_entry.pack(pady=5)

        # Directory selection
        tk.Label(root, text="Search directory:", font=("Arial", 12)).pack(pady=5)
        frame = tk.Frame(root)
        frame.pack(pady=5)
        self.dir_var = tk.StringVar()
        self.dir_entry = tk.Entry(frame, textvariable=self.dir_var, width=40, font=("Arial", 11))
        self.dir_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Browse", command=self.browse_directory).pack(side=tk.LEFT)

        # Search Button
        tk.Button(
            root,
            text="Start Search",
            command=self.start_search_thread,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=5,
        ).pack(pady=15)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="indeterminate")
        self.progress.pack(pady=10)

        # Results Box
        tk.Label(root, text="Search Results:", font=("Arial", 12)).pack(pady=5)
        self.results_box = tk.Text(root, height=8, width=65, wrap="word", state="disabled", bg="#ecf0f1")
        self.results_box.pack(pady=5)

        # Timer Label
        self.timer_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
        self.timer_label.pack(pady=5)

    def browse_directory(self):
        folder = filedialog.askdirectory(title="Select Directory")
        if folder:
            self.dir_var.set(folder)

    def start_search_thread(self):
        thread = threading.Thread(target=self.search_file)
        thread.start()

    def search_file(self):
        filename = self.filename_entry.get().strip()
        directory = self.dir_var.get().strip() or "/"

        if not filename:
            messagebox.showwarning("Warning", "Please enter a file name.")
            return

        # Reset previous results
        self.results_box.config(state="normal")
        self.results_box.delete(1.0, tk.END)
        self.results_box.config(state="disabled")

        self.progress.start()
        start_time = time.time()

        try:
            results = find_file(filename, directory)
        except PermissionError:
            messagebox.showerror("Error", "Permission denied while searching.")
            self.progress.stop()
            return

        elapsed = round(time.time() - start_time, 2)
        self.timer_label.config(text=f"Search completed in {elapsed} seconds.")

        self.progress.stop()

        self.results_box.config(state="normal")
        if results:
            for path in results:
                self.results_box.insert(tk.END, f"➡️ {path}\n")
        else:
            self.results_box.insert(tk.END, "❌ File not found.")
        self.results_box.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = FileFinderApp(root)
    root.mainloop()
