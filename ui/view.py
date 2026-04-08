from tkinter import Frame, Label
from alkoritms.sorting.bubbleSort import BubbleSort

class View:
    def __init__(self, root):
        self.root = root
        self.array = []
        self.array_frame = Frame(self.root, bg="white")
        self.array_frame.pack(pady=20)
        self.state_frame = Frame(self.root, bg="white")
        self.state_frame.pack(pady=10)


    def draw_array(self, array, highlight_indices, state):
        if highlight_indices is None:
            highlight_indices = []

        for widget in self.array_frame.winfo_children():
            widget.destroy()

        for i, value in enumerate(array):
            color = "red" if i in highlight_indices else "black"
            label = Label(
                self.array_frame,
                text=str(value), 
                foreground="white", 
                bg=color,
                font=("Arial", 12), 
                width=6, 
                height=3, 
                borderwidth=1, 
                relief="solid",
                justify="center",
            )
            label.pack(side="left")

        self.update_state(state)

    def update_state(self, state):
        for widget in self.state_frame.winfo_children():
            widget.destroy()

        stateText = Label(self.state_frame, text=f"State: {state}", foreground="black", bg="white", font=("Arial", 12))
        stateText.pack()

    def sorting(self, array, highlight_indices=None, algo_state=None):
        if highlight_indices is None:
            highlight_indices = []
        
        self.draw_array(array, highlight_indices, algo_state)
        for state in BubbleSort.sort(array):
            self.draw_array(state[0], highlight_indices=state[1], algo_state=state[2])
            




