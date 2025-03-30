# Resource Allocation Graph Visualizer

## Overview
The **Resource Allocation Graph Visualizer** is an interactive tool that helps users visualize and analyze resource allocation in a system. It allows users to add processes and resources, create request and allocation edges, detect deadlocks, and interact with a visually appealing UI.

## Features
- **Add & Remove Nodes:** Easily add processes (`P1`, `P2`, etc.) and resources (`R1`, `R2`, etc.).
- **Request & Allocate Resources:** Create directed edges to represent resource requests and allocations.
- **Graph Visualization:** Displays the resource allocation graph dynamically with an updated UI.
- **Deadlock Detection:** Identifies cycles in the graph that indicate deadlocks.
- **Reset & Save Graph:** Reset the graph to start fresh or save the current graph as an image.

## Installation
To run the visualizer, follow these steps:

1. Ensure you have Python installed (Python 3.x recommended).
2. Install the required dependencies:
   ```sh
   pip install networkx matplotlib tkinter
   ```
3. Download or clone this repository.
4. Run the program:
   ```sh
   python resource_allocation_graph.py
   ```

## Usage
1. **Adding Nodes:** Enter a process (e.g., `P1`) or resource (`R1`) and click the respective button.
2. **Creating Edges:** Enter a process and a resource, then click "Request Resource" or "Allocate Resource."
3. **Deadlock Detection:** Click "Check Deadlock" to check for cycles.
4. **Graph Reset:** Use "Reset Graph" to clear everything.
5. **Save Graph:** Click "Save Graph" to store the visualization as an image.

## Example (Non-Deadlock Scenario)
1. **Processes:** `P1`, `P2`
2. **Resources:** `R1`, `R2`
3. **Edges:**
   - `P1 → R1` (Request)
   - `R1 → P2` (Allocation)
   - `P2 → R2` (Request)
   - `R2 → P1` (Allocation, but no cycle if resources are released)

This setup does **not** create a deadlock if resources are released appropriately.

## Technologies Used
- **Python** (Core logic)
- **Tkinter** (GUI)
- **NetworkX** (Graph handling)
- **Matplotlib** (Graph visualization)

## License
This project is open-source and can be modified as needed.

---

Enjoy visualizing your resource allocation! 🚀

