import networkx as nx
from tkinter import messagebox

class ResourceAllocationGraph:
    def __init__(self):
        self.G = nx.DiGraph()

    def add_process(self, process):
        """Add a process node to the graph."""
        if process and process not in self.G.nodes:
            self.G.add_node(process, type='process')
            return True
        return False

    def add_resource(self, resource):
        """Add a resource node to the graph."""
        if resource and resource not in self.G.nodes:
            self.G.add_node(resource, type='resource')
            return True
        return False

    def request_resource(self, process, resource):
        """Add an edge from process to resource (request)."""
        if (process in self.G.nodes and resource in self.G.nodes and 
            not self.G.has_edge(process, resource)):
            self.G.add_edge(process, resource)
            return True
        return False

    def allocate_resource(self, process, resource):
        """Add an edge from resource to process (allocation)."""
        if (process in self.G.nodes and resource in self.G.nodes and 
            not self.G.has_edge(resource, process)):
            self.G.add_edge(resource, process)
            return True
        return False

    def remove_node(self, node):
        """Remove a node and its edges from the graph."""
        if node in self.G.nodes:
            self.G.remove_node(node)
            return True
        return False

    def remove_edge(self, process, resource):
        """Remove an edge between process and resource."""
        if self.G.has_edge(process, resource):
            self.G.remove_edge(process, resource)
            return True
        return False

    def check_deadlock(self, root):
        """Check for deadlock and display a message."""
        try:
            cycle_edges = nx.find_cycle(self.G, orientation="original")
            cycle = [(u, v) for u, v, _ in cycle_edges]
            messagebox.showerror("Deadlock Detected", f"Deadlock Cycle: {cycle}", parent=root)
            return cycle
        except nx.NetworkXNoCycle:
            messagebox.showinfo("No Deadlock", "No deadlock detected.", parent=root)
            return None

    def reset_graph(self):
        """Clear the entire graph."""
        self.G.clear()