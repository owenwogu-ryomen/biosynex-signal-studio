import tkinter as tk

root = tk.Tk()
root.geometry("800x500")

frame = tk.Frame(root, bg="yellow")
frame.pack(fill="both", expand=True)

label = tk.Label(
    frame,
    text="HELLO BIOSYNEX",
    font=("Arial", 24)
)
label.pack(pady=50)

root.mainloop()