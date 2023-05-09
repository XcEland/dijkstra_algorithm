import networkx as nx
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

# Define the graph
G = nx.Graph()

# Add nodes (cities) to the graph with alphabetical labels
G.add_node('A', name='Los Angeles')
G.add_node('B', name='Houston')
G.add_node('C', name='New York')
G.add_node('D', name='San Francisco')
G.add_node('E', name='Chicago')
G.add_node('F', name='Miami')
G.add_node('G', name='Seattle')
G.add_node('H', name='Boston')

# Add edges (distances) between the cities in kilometers
G.add_edge('A', 'B', weight=2346)
G.add_edge('A', 'C', weight=3939)
G.add_edge('A', 'D', weight=614)
G.add_edge('B', 'C', weight=2271)
G.add_edge('B', 'D', weight=1346)
G.add_edge('B', 'E', weight=1625)
G.add_edge('C', 'E', weight=1144)
G.add_edge('C', 'F', weight=2143)
G.add_edge('D', 'G', weight=1296)
G.add_edge('E', 'F', weight=1373)
G.add_edge('E', 'G', weight=2780)
G.add_edge('F', 'H', weight=1539)
G.add_edge('G', 'H', weight=3830)

# Define the fixed positions of the nodes
pos = {'A': (0, 0),
       'B': (3, 0),
       'C': (6, 0),
       'D': (1, 1),
       'E': (5, 1),
       'F': (6, 2),
       'G': (3, 3),
       'H': (7, 3)}

# Draw the graph with city names as labels
def draw_graph(path=None):
    labels = nx.get_node_attributes(G, 'name')
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=12)
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=14)
    if path:
        edges = [(path[n], path[n+1]) for n in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, width=4, edge_color='r')
    plt.axis('off')
    plt.show()

# Define the function to compute the shortest path and draw the graph
def find_shortest_path(source, dest):
    path = nx.dijkstra_path(G, source, dest)
    distance = nx.dijkstra_path_length(G, source, dest)
    path_str = ' -> '.join(nx.get_node_attributes(G, 'name')[n] for n in path)
    shortest_distance_label.config(text=f"Shortest Distance: {distance} km")
    path_followed_label.config(text=f"Path Followed: {path_str}")
    draw_graph(path)

# Define the GUI interface
def on_select(event):
    source = source_var.get()
    dest = dest_var.get()
    find_shortest_path(source, dest)

# Create the root window and widgets
root = Tk()
root.title("Shortest Path Finder")
root.geometry("400x200")
source_label = Label(root, text="Source city:")
source_label.pack(pady=5)
source_var = StringVar()
source_dropdown = ttk.Combobox(root, textvariable=source_var, values=list(G.nodes), state="readonly")
source_dropdown.pack()
source_dropdown.current(0)
dest_label = Label(root, text="Destination city:")
dest_label.pack(pady=5)
dest_var = StringVar()
dest_dropdown = ttk.Combobox(root, textvariable=dest_var, values=list(G.nodes), state="readonly")
dest_dropdown.pack()
dest_dropdown.current(1)
find_button = Button(root, text="Find Shortest Path", command=lambda: find_shortest_path(source_var.get(), dest_var.get()))
find_button.pack(pady=10)
shortest_distance_label = Label(root, text="")
shortest_distance_label.pack()
path_followed_label = Label(root, text="")
path_followed_label.pack()

# Bind the dropdowns to the on_select function
source_dropdown.bind("<<ComboboxSelected>>", on_select)
dest_dropdown.bind("<<ComboboxSelected>>", on_select)

# Start the GUI event loop
root.mainloop()