from ui.main_window import MainWindow
from ui.controllers import Controller
from ui.algo_selection import AlgorithmSelection
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        #меню кароче
        self.main_window = MainWindow(self.root)
        #а тууут главное окно, там уже все вместе хехеехехехх
        self.algo_selection=AlgorithmSelection(self.root)
        #контролер кароче
        self.controller = Controller(self.root)
        #а тут они кароче дружатся
        self.controller.algo_selection = self.algo_selection
        
    
    def run(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = App()
    app.run()
    #код говна которого я не могу описать словами, но он работает, так что пусть будет так