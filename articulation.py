import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec
import pandas as pd
def get_graph_from_user():
    graph = {}
    print("Enter the flight connections (format: 'A B 1' for a flight from A to B with cost 1). Type 'done' when finished:")
    
    while True:
        edge = input()
        if edge.lower() == 'done':
            break
        u, v, w = edge.split()
        w = int(w)
        
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        
        graph[u].append((v, w))
        graph[v].append((u, w))  # Assuming the graph is undirected
    
    return graph

graph = get_graph_from_user()

# Create a NetworkX graph
G = nx.Graph()
for node, edges in graph.items():
    for edge, weight in edges:
        G.add_edge(node, edge, weight=weight)

articulation_points = list(nx.articulation_points(G))
biconnected_components = list(nx.biconnected_components(G))

print("Articulation Points:")
print(articulation_points)
print("\nBiconnected Components:")
print([list(bc) for bc in biconnected_components])

fig = plt.figure(figsize=(12, 6))
gs = GridSpec(1, 2, width_ratios=[2, 1])

ax_graph = fig.add_subplot(gs[0])
ax_table = fig.add_subplot(gs[1])
pos = nx.spring_layout(G)

def update(num):
    ax_graph.clear()
    ax_table.clear()

    # Initially, no highlights
    colors = ['lightblue'] * len(G.nodes)

    if num < len(articulation_points):
        # Highlight articulation points one by one
        colors[list(G.nodes).index(articulation_points[num])] = 'red'
    elif num < len(articulation_points) + len(biconnected_components):
        # Highlight biconnected components one by one
        component = list(biconnected_components[num - len(articulation_points)])
        for node in component:
            colors[list(G.nodes).index(node)] = 'green'
    else:
       
        for ap in articulation_points:
            colors[list(G.nodes).index(ap)] = 'red'
        for bc in biconnected_components:
            for node in bc:
                colors[list(G.nodes).index(node)] = 'green'
    
    nx.draw(G, pos, node_color=colors, with_labels=True, ax=ax_graph)

    # Update the table
    if num < len(articulation_points):
        columns = ["Articulation Point"]
        data = [[ap] for ap in articulation_points[:num+1]]
    else:
        columns = ["Biconnected Component"]
        data = [[', '.join(map(str, bc))] for bc in biconnected_components[:num - len(articulation_points) + 1]]
    df = pd.DataFrame(data, columns=columns)
    ax_table.axis('tight')
    ax_table.axis('off')
    table = ax_table.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
ani = animation.FuncAnimation(fig, update, frames=len(articulation_points) + len(biconnected_components) + 1, repeat=False, interval=2000)
