from tkinter import Button, Frame

class Controller:
    def __init__(self, root):
        self.root = root
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

    def start(self):
        print("Visualization started")
    
    def stop(self):
        print("Visualization stopped")
    
