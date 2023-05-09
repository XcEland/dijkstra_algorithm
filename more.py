import heapq
import tkinter as tk
from tkinter import ttk
import graphviz

# define the graph
graph = {
    'H': [('M', 292), ('C', 115), ('K', 213)],
    'B': [('M', 415), ('G', 164), ('W', 272)],
    'M': [('H', 292), ('B', 415), ('G', 153)],
    'G': [('B', 164), ('M', 153), ('K', 51)],
    'C': [('H', 115),('W', 383)],
    'K': [('H', 213), ('G', 51), ('W', 620)],
    'W': [('B', 272), ('K', 620), ('C', 383)]
}

# define the city names dictionary
city_names = {
    'H': 'Harare',
    'B': 'Bulawayo',
    'M': 'Masvingo',
    'G': 'Gweru',
    'C': 'Chinhoyi', 
    'K': 'Kwekwe',
    'W': 'Hwange'
}

# define a function to find the shortest path using Dijkstra's algorithm
def dijkstra(graph, start, end):
    # create a dictionary to store the distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # create a dictionary to store the previous node in the shortest path
    previous_nodes = {node: None for node in graph}
    
    # create a list to store the nodes that have not been visited
    nodes = [(0, start)]
    heapq.heapify(nodes)
    
    # loop until all nodes have been visited
    while nodes:
        # get the node with the smallest distance
        current_distance, current_node = heapq.heappop(nodes)
        
        # check if we've reached the end node
        if current_node == end:
            path = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.append(start)
            path.reverse()
            return path
        
        # check if we've already visited this node
        if current_distance > distances[current_node]:
            continue
        
        # update the distance to each neighboring node
        for neighbor, distance in graph[current_node]:
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(nodes, (new_distance, neighbor))
    
    # if we get here, there is no path between the start and end nodes
    return None

# define a function to display the graph using graphviz
def display_graph():
    # create a new directed graph
    dot = graphviz.Graph(graph_attr={'type': 'graph', 'layout': 'twopi', 'nodesep': '1.5', 'ranksep': '2'})

    # set node attributes
    dot.node_attr['fontname'] = 'Arial'
    dot.node_attr['fontsize'] = '12'
    dot.node_attr['fontcolor'] = 'red'

    # set edge attributes
    dot.edge_attr['fontname'] = 'Arial'
    dot.edge_attr['fontsize'] = '12'
    dot.edge_attr['fontcolor'] = 'black'

    # add nodes to the graph
    for node in graph:
        dot.node(node, label=city_names[node])

    # set to keep track of edges that have already been added
    added_edges = set()

    # add edges to the graph
    for node, edges in graph.items():
        for edge, weight in edges:
            if (edge, node) not in added_edges:  # check if edge has already been added
                dot.edge(node, edge, label=str(weight) + ' km')
                added_edges.add((node, edge))  # add edge to set

    # display the graph in the default viewer
    dot.view()

# create a GUI window
window = tk.Tk()
window.title("RouteGetter")

# create a label for the source city
source_label = tk.Label(window, text="Source:")
source_label.grid(row=0, column=0, padx=5, pady=5)

# create a Combobox widget for the source city
source_var = tk.StringVar()
source_var.set("")
source_combobox = ttk.Combobox(window, textvariable=source_var, values=list(city_names.values()))
source_combobox.grid(row=0, column=1, padx=5, pady=5)

# create a label for the destination city
dest_label = tk.Label(window, text="Destination:")
dest_label.grid(row=1, column=0, padx=5, pady=5)

# create a Combobox widget for the destination city
dest_var = tk.StringVar()
dest_var.set("")
dest_combobox = ttk.Combobox(window, textvariable=dest_var, values=list(city_names.values()))
dest_combobox.grid(row=1, column=1, padx=5, pady=5)

# define a function to update the Combobox value when the user types in it
def update_combobox(event):
    widget = event.widget
    text = widget.get()
    values = widget.cget("values")
    if text in values:
        return
    values = sorted(list(values) + [text])
    widget.configure(values=values)

# bind the update_combobox function to the Comboboxes
source_combobox.bind("<<ComboboxSelected>>", update_combobox)
dest_combobox.bind("<<ComboboxSelected>>", update_combobox)

# create a function to find the shortest path and display it
def find_path():
    source = None
    dest = None
    for key, value in city_names.items():
        if value == source_var.get():
            source = key
        if value == dest_var.get():
            dest = key
    if source is None or dest is None:
        return
    path = dijkstra(graph, source, dest)
    if path is not None:
        path_str = " -> ".join(city_names[node] for node in path)
        total_distance = 0
        for i in range(len(path)-1):
            for neighbor, distance in graph[path[i]]:
                if neighbor == path[i+1]:
                    total_distance += distance
        result_label.config(text=f"{path_str} (distance: {total_distance}km)")
        display_button.config(state=tk.NORMAL)
    else:
        result_label.config(text="No path found")
        display_button.config(state=tk.DISABLED)
        
# create a button to find the shortest path
find_button = tk.Button(window, text="Find Path", command=find_path)
find_button.grid(row=2, column=0, padx=5, pady=5)

# create a label to display the shortest path
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=1, padx=5, pady=5)

# create a button to display the graph
display_button = tk.Button(window, text="Display Graph", command=display_graph, state=tk.DISABLED)
display_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# start the GUI event loop
window.mainloop()