import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import os

class SignalStudioApp:
    def __init__(self, root):
        self.root = root
        self.df = None
        self._build_ui()

    def _build_ui(self):
        self.root.title("BIOSYNEX SIGNAL STUDIO")
        self.root.geometry("1200x700")
        self.root.minsize(1000, 650)
        self.root.configure(bg="#f3f6fa")

        self._configure_styles()

        header = ttk.Frame(self.root, padding=(22, 18, 22, 12))
        header.pack(side="top", fill="x")
        header.configure(style="Header.TFrame")

        title_label = ttk.Label(
            header,
            text="BIOSYNEX SIGNAL STUDIO",
            font=("Segoe UI", 18, "bold"),
            foreground="#0d4f6c"
        )
        title_label.pack(anchor="w")

        subtitle_label = ttk.Label(
            header,
            text="Biomedical signal review and dataset inspection",
            font=("Segoe UI", 10),
            foreground="#537188"
        )
        subtitle_label.pack(anchor="w", pady=(4, 0))

        body = ttk.Frame(self.root, padding=(18, 10, 18, 18))
        body.pack(fill="both", expand=True)

        self.left_panel = ttk.Frame(body, width=260, padding=(12, 12, 12, 12), style="Nav.TFrame")
        self.left_panel.pack(side="left", fill="y")
        self.left_panel.pack_propagate(False)
        self._build_left_panel()

        self.middle_panel = ttk.Frame(body, width=300, padding=(12, 12, 12, 12), style="Content.TFrame")
        self.middle_panel.pack(side="left", fill="y", padx=(10, 0))
        self.middle_panel.pack_propagate(False)
        self._build_middle_panel()

        self.right_panel = ttk.Frame(body, padding=(12, 12, 12, 12), style="Content.TFrame")
        self.right_panel.pack(side="left", fill="both", expand=True, padx=(10, 0))
        self._build_right_panel()

    def _build_left_panel(self):
        ttk.Label(
            self.left_panel,
            text="Navigation",
            font=("Segoe UI", 12, "bold"),
            foreground="white"
        ).pack(anchor="w", pady=(0, 12))

        ttk.Button(
            self.left_panel,
            text="Open Signal",
            command=self.open_signal,
            style="Primary.TButton"
        ).pack(fill="x", pady=(0, 8))

        ttk.Label(
            self.left_panel,
            text="Status",
            font=("Segoe UI", 11, "bold"),
            foreground="white"
        ).pack(anchor="w", pady=(20, 6))

        self.status_var = tk.StringVar(value="Ready to load a signal file.")
        status_label = ttk.Label(
            self.left_panel,
            textvariable=self.status_var,
            foreground="white",
            wraplength=220,
            justify="left"
        )
        status_label.pack(anchor="w")

    def _build_middle_panel(self):
        card = ttk.Frame(self.middle_panel, padding=(10, 10, 10, 10), style="Card.TFrame")
        card.pack(fill="x")

        ttk.Label(
            card,
            text="Dataset Information",
            font=("Segoe UI", 12, "bold"),
            foreground="#0d4f6c"
        ).pack(anchor="w")

        self.dataset_message = "No dataset loaded"
        self.dataset_message_var = tk.StringVar(value=self.dataset_message)
        self.dataset_info = tk.Label(
            card,
            textvariable=self.dataset_message_var,
            font=("Segoe UI", 10),
            fg="#090101",
            bg="white",
            justify="left",
            anchor="nw"
        )
        self.dataset_info.pack(fill="x", pady=(8, 0))
        self.update_dataset_info(self.dataset_message)

        ttk.Separator(self.middle_panel, orient="horizontal").pack(fill="x", pady=(12, 10))

        ttk.Label(
            self.middle_panel,
            text="Column Explorer",
            font=("Segoe UI", 12, "bold"),
            foreground="#0d4f6c"
        ).pack(anchor="w")

        self.column_listbox = tk.Listbox(
            self.middle_panel,
            font=("Segoe UI", 10),
            height=12,
            exportselection=False
        )
        self.column_listbox.pack(fill="both", expand=True, pady=(6, 0))
        self.column_listbox.bind(
            "<<ListboxSelect>>",
            self.on_column_selected
        )
    def _build_right_panel(self):
        workspace_title = tk.Label(
            self.right_panel,
            text="Signal Preview",
            font=("Segoe UI", 13, "bold"),
            fg="#0d4f6c",
            bg="white"
        )
        workspace_title.pack(fill="x", anchor="w")

        self.preview_frame = ttk.Frame(self.right_panel)
        self.preview_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.table = ttk.Treeview(self.preview_frame, show="headings", height=12)
        self.table.pack(side="left", fill="both", expand=True)

        scroll_y = ttk.Scrollbar(self.preview_frame, orient="vertical", command=self.table.yview)
        scroll_y.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=scroll_y.set)

        self._clear_table()

    def _configure_styles(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Header.TFrame", background="#f8fbfd")
        style.configure("Nav.TFrame", background="#1f3d5a")
        style.configure("Content.TFrame", background="#ffffff")
        style.configure("Card.TFrame", background="#f7faff")
        style.configure("Primary.TButton", background="#2f6f9f", foreground="white", padding=(10, 6))
        style.map("Primary.TButton", background=[("active", "#3b86b8")])

    def update_dataset_info(self, text):
        self.dataset_message = text
        self.dataset_message_var.set(text)
        self.root.update_idletasks()

    def _populate_column_explorer(self, columns):
        self.column_listbox.delete(0, tk.END)
        for column in columns:
            self.column_listbox.insert(tk.END, column)

    def on_column_selected(self, event):
        if self.df is None:
            return

        selection = self.column_listbox.curselection()
        if not selection:
            return

        column_name = self.column_listbox.get(selection[0])
        self.populate_table(self.df.head())
        self.populate_table(selected_df)

    def _clear_table(self):
        for row in self.table.get_children():
            self.table.delete(row)
        self.table["columns"] = []
        self.table.heading("#0", text="")

    def populate_table(self, df):
        self._clear_table()

        if df.empty:
            self.table["columns"] = ["Message"]
            self.table.heading("Message", text="Message")
            self.table.insert("", "end", values=["No rows available."])
            return

        columns = list(df.columns)
        self.table["columns"] = columns

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=140, anchor="w")

        for _, row in df.iterrows():
            values = [row[col] for col in columns]
            self.table.insert("", "end", values=values)

    def open_signal(self):
        file_path = filedialog.askopenfilename(
            title="Select a Signal File",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
        )

        if not file_path:
            return

        try:
            df = pd.read_csv(file_path, encoding="utf-8")
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file_path, encoding="latin-1")
            except Exception as exc:
                self.status_var.set(f"Could not read file: {exc}")
                self._clear_table()
                return

        print("CSV Loaded Successfully!")
        print(df.head())

        self.df = df

        

        filename = os.path.basename(file_path)
        
        print("Updating dataset info...")
        
        rows = len(df)
        columns = len(df.columns)
        missing = df.isnull().sum().sum()
        numeric = len(df.select_dtypes(include="number").columns)
        text = len(df.select_dtypes(include="object").columns)

        self.update_dataset_info(
            f"File: {filename}\n"
            f"Rows: {rows}\n"
            f"Columns: {columns}\n"
            f"Missing Values: {missing}\n"
            f"Numeric Columns: {numeric}\n"
            f"Text Columns: {text}"
        )
        print(self.dataset_info.cget("text"))

        self._populate_column_explorer(df.columns)
        self.populate_table(df.head())

        self.status_var.set("Dataset loaded successfully.")


if __name__ == "__main__":
    root = tk.Tk()
    app = SignalStudioApp(root)
    root.mainloop()
