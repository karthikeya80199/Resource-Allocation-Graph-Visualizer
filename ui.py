import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx

class GraphVisualizer:
    def __init__(self, root, graph_logic):
        self.graph_logic = graph_logic
        self.root = root
        self.root.title("Resource Allocation Graph Visualizer")
        self.root.geometry("1100x700")
        self.root.configure(bg='#121212')
        self.create_ui()

    def create_ui(self):
        """Set up the main UI components."""
        # Left control panel
        self.control_frame = tk.Frame(self.root, bg='#1E1E1E', padx=10, pady=10, relief=tk.RIDGE, bd=2)
        self.control_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

        tk.Label(self.control_frame, text="Graph Visualizer", font=("Arial", 16, "bold"), 
                 bg='#1E1E1E', fg='#00FFFF').pack(pady=10)

        self.create_entries()
        self.create_buttons()

        # Graph display
        self.fig, self.ax = plt.subplots(figsize=(6, 6), facecolor='#121212')
        self.ax.set_facecolor('#181818')
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().configure(bg='#121212')
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=15, pady=15)

    def create_entries(self):
        """Create input fields for process and resource."""
        entry_style = {
            'bg': '#252525', 'fg': '#00FFFF', 'insertbackground': '#00FFFF', 'relief': 'flat',
            'font': ("Arial", 12), 'bd': 2, 'highlightthickness': 1, 'highlightbackground': '#00FFFF'
        }

        tk.Label(self.control_frame, text="Process:", font=("Arial", 10), bg='#1E1E1E', fg='#BBBBBB').pack(anchor="w", padx=5)
        self.process_entry = tk.Entry(self.control_frame, **entry_style)
        self.process_entry.pack(pady=5, padx=5, fill=tk.X)

        tk.Label(self.control_frame, text="Resource:", font=("Arial", 10), bg='#1E1E1E', fg='#BBBBBB').pack(anchor="w", padx=5)
        self.resource_entry = tk.Entry(self.control_frame, **entry_style)
        self.resource_entry.pack(pady=5, padx=5, fill=tk.X)

    def create_buttons(self):
        """Create buttons with hover effects."""
        btn_config = {
            'bg': '#00FFFF', 'fg': '#121212', 'font': ("Arial", 11, "bold"), 'relief': 'flat',
            'activebackground': '#0088AA', 'activeforeground': '#FFFFFF', 'width': 18,
            'padx': 5, 'pady': 6, 'cursor': 'hand2', 'bd': 0
        }

        buttons = [
            ("Add Process", self.add_process),
            ("Add Resource", self.add_resource),
            ("Request Resource", self.request_resource),
            ("Allocate Resource", self.allocate_resource),
            ("Remove Node", self.remove_node),
            ("Remove Edge", self.remove_edge),
            ("Check Deadlock", self.check_deadlock),
            ("Reset Graph", self.reset_graph),
            ("Save Graph", self.save_graph)
        ]

        for text, cmd in buttons:
            btn = tk.Button(self.control_frame, text=text, command=cmd, **btn_config)
            btn.pack(pady=6, padx=5, fill=tk.X)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#0088AA'))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#00FFFF'))

    def add_process(self):
        """Add a process and update the graph."""
        process = self.process_entry.get().strip()
        if self.graph_logic.add_process(process):
            self.draw_graph()
            self.process_entry.delete(0, tk.END)

    def add_resource(self):
        """Add a resource and update the graph."""
        resource = self.resource_entry.get().strip()
        if self.graph_logic.add_resource(resource):
            self.draw_graph()
            self.resource_entry.delete(0, tk.END)

    def request_resource(self):
        """Request a resource for a process and update the graph."""
        process = self.process_entry.get().strip()
        resource = self.resource_entry.get().strip()
        if self.graph_logic.request_resource(process, resource):
            self.draw_graph()

    def allocate_resource(self):
        """Allocate a resource to a process and update the graph."""
        process = self.process_entry.get().strip()
        resource = self.resource_entry.get().strip()
        if self.graph_logic.allocate_resource(process, resource):
            self.draw_graph()

    def remove_node(self):
        """Remove a node and update the graph."""
        node = self.process_entry.get().strip()
        if self.graph_logic.remove_node(node):
            self.draw_graph()
            self.process_entry.delete(0, tk.END)

    def remove_edge(self):
        """Remove an edge and update the graph."""
        process = self.process_entry.get().strip()
        resource = self.resource_entry.get().strip()
        if self.graph_logic.remove_edge(process, resource):
            self.draw_graph()

    def check_deadlock(self):
        """Check for deadlock and highlight cycle if present."""
        cycle = self.graph_logic.check_deadlock(self.root)
        self.draw_graph(highlight_cycle=cycle)

    def reset_graph(self):
        """Reset the graph and redraw."""
        self.graph_logic.reset_graph()
        self.draw_graph()
        self.process_entry.delete(0, tk.END)
        self.resource_entry.delete(0, tk.END)

    def save_graph(self):
        """Save the current graph as an image."""
        self.fig.savefig("resource_allocation_graph.png", dpi=300, bbox_inches='tight', facecolor='#121212')

    def draw_graph(self, highlight_cycle=None):
        """Draw the graph with nodes and edges."""
        self.ax.clear()
        if not self.graph_logic.G.nodes:
            self.canvas.draw()
            return

        pos = nx.spring_layout(self.graph_logic.G, seed=42)
        node_colors = ['#00FFFF' if self.graph_logic.G.nodes[n].get('type') == 'process' else '#FF4444' 
                       for n in self.graph_logic.G.nodes]
        edge_colors = ['#FF5555' if highlight_cycle and (u, v) in highlight_cycle else '#BBBBBB' 
                       for u, v in self.graph_logic.G.edges]

        nx.draw(self.graph_logic.G, pos, with_labels=True, ax=self.ax, node_color=node_colors, 
                edge_color=edge_colors, node_size=2800, font_size=12, font_weight='bold', 
                font_color='#121212', edgecolors='#FFFFFF', linewidths=2.5, arrowsize=20, 
                connectionstyle='arc3,rad=0.1')
        self.ax.set_facecolor('#181818')
        self.canvas.draw()