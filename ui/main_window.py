import tkinter as tk

class MainWindow:
    def __init__(self, root, controller, algo_selection):
        self.root = root
        self.algo_selection = algo_selection
        self.controller = controller

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