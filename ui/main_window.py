import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root

        self.root.title("Algorithms Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        self.label = tk.Label(
            self.root,
            text="Algorithms Visualizer",
            font=("Arial", 18),
            bg="grey"
        )
        self.label.pack(pady=20)