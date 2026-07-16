import tkinter as tk
from tkinter import filedialog
import pandas as pd



root = tk.Tk()
root.title("BIOSYNEX SIGNAL STUDIO")
root.geometry("1000x600")
root.minsize(800, 600)



header = tk.Frame(root, bg="white", height=70)
header.pack(side="top", fill="x")
header.pack_propagate(False)

title_label = tk.Label(
    header,
    text="BIOSYNEX SIGNAL STUDIO",
    font=("Arial", 20, "bold"),
    bg="white",
    fg="darkblue"
)
title_label.pack(pady=15)



body = tk.Frame(root)
body.pack(fill="both", expand=True)



left_panel = tk.Frame(
    body,
    width=250,
    bg="#E8E8E8"
)
left_panel.pack(side="left", fill="y")
left_panel.pack_propagate(False)



workspace = tk.Frame(
    body,
    bg="white"
)
workspace.pack(side="right", fill="both", expand=True)

# Temporary label
test_label = tk.Label(
    workspace,
    text="Workspace Ready",
    font=("Arial", 18),
    bg="white"
)
test_label.pack(pady=20)



def open_signal():
    file_path = filedialog.askopenfilename(
        title="Select a Signal File",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, encoding='latin-1')
            except Exception as e:
                test_label.config(text=f"Could not read file: {e}")
                return

        print("CSV Loaded Successfully!")
        print(df.head())


        
        preview_text = "\n".join(df.head().to_string(index=False).splitlines())
        test_label.config(text=preview_text)



open_button = tk.Button(
    left_panel,
    text="Open Signal",
    font=("Arial", 16),
    command=open_signal
)

open_button.pack(fill="x", padx=10, pady=10)



root.mainloop()