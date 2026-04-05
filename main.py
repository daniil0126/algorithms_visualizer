from ui.main_window import MainWindow
from ui.controllers import Controller
from ui.algo_selection import AlgorithmSelection
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.main_window = MainWindow(self.root, None, None)
        self.algo_selection = AlgorithmSelection(self.root)
        self.controller = Controller(self.root)
    
    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = App()
    app.run()