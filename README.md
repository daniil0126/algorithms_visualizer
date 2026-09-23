# Algorithms Visualizer

A small desktop app (Python + Tkinter) that animates sorting algorithms step by step, to make the comparisons/swaps a textbook diagram usually hides actually visible.

## What it does

- Renders an array as bars/blocks on a canvas and steps through the algorithm one comparison or swap at a time.
- Uses a generator per algorithm (`yield state, indices, label`) so the animation loop stays decoupled from the algorithm's logic — the algorithm just yields its steps, the controller schedules them on a timer.
- Start / Stop controls via Tkinter buttons.

## Implemented

- Bubble Sort (`alkoritms/sorting/bubbleSort.py`)

More algorithms (selection sort, insertion sort, quicksort, a pathfinding one) are the natural next step — the generator-based step interface was designed so adding one doesn't touch the UI code.

## Run it

```bash
python main.py
```

Requires Python 3 with Tkinter (bundled with the standard CPython installer on macOS/Windows; on Linux install `python3-tk` separately).

## Structure

```
main.py                    # app entry point, wires up the Tkinter window
alkoritms/
  basic.py                 # shared algorithm helpers
  sorting/bubbleSort.py     # BubbleSort.sort() — generator that yields each step
ui/
  main_window.py           # root window setup
  algo_selection.py        # algorithm picker
  controllers.py           # Start/Stop buttons, drives the animation loop
  view.py                  # canvas drawing (bars, highlighted indices, state label)
```

## Why

Built to get a feel for algorithm behavior beyond Big-O notation — watching *where* a bubble sort spends its comparisons is a different kind of understanding than reading the pseudocode.
