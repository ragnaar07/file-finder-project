import tkinter as tk
from tkinter import filedialog, messagebox
from file_searcher import find_file

def search():
    filename = entry.get()
    directory = filedialog.askdirectory(title="Select Directory")
    if not filename or not directory:
        messagebox.showwarning("Warning", "Please enter a file name and directory.")
        return
    results = find_file(filename, directory)
    if results:
        messagebox.showinfo("Results", "\n".join(results))
    else:
        messagebox.showinfo("Results", "File not found.")

root = tk.Tk()
root.title("File Finder Tool")

tk.Label(root, text="Enter filename:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Search", command=search).pack(pady=10)
root.mainloop()

