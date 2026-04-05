from tkinter import ttk

class AlgorithmSelection:
    def __init__(self, root):
        self.root = root
        self.create_menu()
    
    def create_menu(self):
        algotithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"]
        self.combobox = ttk.Combobox(values=algotithms, background="white", foreground="white", font=("Arial", 12))
        self.combobox.set("Select Algorithm")
        self.combobox.pack(pady=10)
    
