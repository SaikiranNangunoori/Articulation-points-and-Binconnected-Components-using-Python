# Articulation-points-and-Binconnected-Components-using-Python
This project visualizes the critical connectivity in a flight network using *graph theory algorithms. It highlights **articulation points* (critical airports) and *biconnected components* (subgraphs that remain connected without any single point of failure).
Features:
- Takes user input to build a flight network.
- Identifies and displays:
  - Articulation Points – airports whose removal would disconnect the network.
  - Biconnected Components – maximal sets of nodes where the network stays connected even if one node is removed.
- Animates the graph step-by-step to visually demonstrate:
  - Critical nodes in red
  - Strongly connected sub-networks in green
- Uses matplotlib for animated visualization and networkx for graph analysis.
