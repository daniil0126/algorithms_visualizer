from tkinter import ttk
from config import AVAILABLE_ALGORITHMS
class AlgorithmSelection:
    def __init__(self, root):
        self.root = root
        self.create_menu()
    
    def create_menu(self):
        algotithms = list(AVAILABLE_ALGORITHMS.keys())
        self.combobox = ttk.Combobox(values=algotithms, background="white", foreground="black", font=("Arial", 12))
        self.combobox.set("Select Algorithm")
        self.combobox.pack(pady=10)
    
