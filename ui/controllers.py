from tkinter import Button, Frame
from ui.view import View
from alkoritms.sorting.bubbleSort import BubbleSort

class Controller:
    def __init__(self, root):
        self.is_running = False
        self.root = root
        self.view = View(self.root)
        self.create_widgets()

    def create_widgets(self):   
        button_frame = Frame(self.root, bg="white")
        button_frame.pack(pady=20)

        self.button_start = Button(
            button_frame,
            text="Start Visualization",
            foreground="black",
            font=("Arial", 12),
            command=self.start
        )
        self.button_start.pack(side="left", padx=10)

        self.button_stop = Button(
            button_frame,
            text="Stop Visualization",
            foreground="black",
            font=("Arial", 12),
            command=self.stop
        )
        self.button_stop.pack(side="left", padx=10)

    def animate(self, gen):
        if not self.is_running:
            return
        try:
            step = next(gen)
            self.view.draw_array(step[0], highlight_indices=step[1], state=step[2])
            self.root.after(1000, lambda: self.animate(gen))
        except StopIteration:
            self.is_running = False
            print("Visualization completed")

    def start(self):
        self.is_running = True
        arr = [5, 2, 9, 1, 5, 6]
        gen = BubbleSort.sort(arr)
        if self.is_running:
            self.animate(gen)
        print("Visualization started")
        
    def stop(self):
        self.is_running = False
        print("Visualization stopped")
    
