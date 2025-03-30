import tkinter as tk
from graph import ResourceAllocationGraph
from ui import GraphVisualizer

if __name__ == "__main__":
    root = tk.Tk()
    graph_logic = ResourceAllocationGraph()
    app = GraphVisualizer(root, graph_logic)
    root.mainloop()