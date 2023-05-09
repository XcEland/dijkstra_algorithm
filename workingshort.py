import tkinter as tk
from tkinter import ttk
import math
import heapq

# Create a dictionary to store the city names
city_names = {
    'A': 'Harare',
    'B': 'Gweru',
    'C': 'Mutare',
    'D': 'Masvingo',
    'E': 'Bulawayo',
    'H': 'Beitbridge',
    'Z': 'Zvishavane'   
}

# Create the graph
graph = {
    'A': [('D', 295), ('C', 216), ('B', 227.6)],
    'B': [('C', 261), ('D', 183), ('E', 162), ('Z', 119), ('A', 227.6)],
    'C': [('A', 116), ('B', 261)],
    'D': [('B', 183), ('A', 295), ('H', 290), ('Z', 97.1)],
    'E': [('B', 162), ('Z', 184), ('H', 323)],
    'H': [('E', 323), ('D', 290), ('Z', 335)],
    'Z': [('B', 119), ('D', 97.1), ('E', 184), ('H', 335)]
}

# Define the dijkstra function
def dijkstra(graph, start, end):
    # ...
    # Create a dictionary to store the distance to each vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Create a dictionary to store the previous vertex in the path
    previous_vertices = {
        vertex: None for vertex in graph
    }

    # Create a priority queue to store vertices that need to be visited
    priority_queue = [(0, start)]

    while len(priority_queue) > 0:
        # Get the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If we have already found a shorter path to the end vertex, we can stop
        if current_vertex == end:
            path = []

            # Follow the previous_vertices dictionary to build the shortest path
            while previous_vertices[current_vertex] is not None:
                path.append(current_vertex)
                current_vertex = previous_vertices[current_vertex]

            # Add the start vertex to the path and return it in reverse order
            path.append(start)
            return path[::-1]

        # If we haven't reached the end vertex yet, visit its neighbors
        for neighbor, distance in graph[current_vertex]:
            global new_distance
            new_distance = current_distance + distance

            # If we have found a shorter path to the neighbor vertex, update its distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    # If we have visited all the vertices and haven't found the end vertex, there is no path
    return None

def find_shortest_path():
    start = None
    end = None

    # Get the source and destination cities from the dropdown menus
    for key, value in city_names.items():
        if value == source_var.get():
            start = key
        if value == dest_var.get():
            end = key

    # Find the shortest path and display it
    shortest_path = dijkstra(graph, start, end)
    if shortest_path:
        path_str = ' -> '.join([city_names[vertex] for vertex in shortest_path])
        result_label.config(text=f"Shortest path: {path_str} ({new_distance} km)")

        # Highlight the shortest path on the graph
        canvas.delete("highlight")
        for i in range(len(shortest_path) - 1):
            node1 = shortest_path[i]
            node2 = shortest_path[i+1]
            x1, y1 = node_coords[node1]
            x2, y2 = node_coords[node2]
            canvas.create_line(x1, y1, x2, y2, width=3, fill="blue", tags="highlight")
    else:
        result_label.config(text="No path found")
        canvas.delete("highlight")

# Create the GUI
root = tk.Tk()
root.title("Shortest Path Finder")

# Set the window size and position
root.geometry("800x600")
root.resizable(width=True, height=True)

# Set the background color
root.configure(bg="lightblue")

# Define the font and size for the text and buttons
font_style = ("Arial", 18)

# Add a header with the author's name
header_label = tk.Label(root, text="Shortest Path Between Cities", font=("Arial", 24), bg="white")
header_label.pack(pady=20)

# Create a frame to hold the input fields and buttons
frame = tk.Frame(root)
frame.pack(side=tk.TOP, pady=20)

# Create the source city label and combo box
source_label = tk.Label(frame, text="Start City:", font=font_style)
source_label.pack(side=tk.LEFT, padx=10, pady=10)
source_var = tk.StringVar(root)
source_var.set('Harare')
source_combo = tk.ttk.Combobox(frame, textvariable=source_var, values=list(city_names.values()), font=font_style)
source_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the destination city label and combo box
dest_label = tk.Label(frame, text="Destination City:", font=font_style)
dest_label.pack(side=tk.LEFT, padx=10, pady=10)
dest_var = tk.StringVar(root)
dest_var.set('Bulawayo')
dest_combo = tk.ttk.Combobox(frame, textvariable=dest_var, values=list(city_names.values()), font=font_style)
dest_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the button to find the shortest path
find_button = tk.Button(frame, text="Find Shortest Path", command=find_shortest_path, font=font_style)
find_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(root, text="", font=font_style, bg="white")
result_label.pack(pady=20)

# Create the canvas to draw the graph
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack(side=tk.BOTTOM, padx=20, pady=20)

author_label = tk.Label(root, text="Aisha Mazviita", font=("Arial", 18), bg="white")
author_label.pack()

# Create a dictionary to store the coordinates of the nodes
node_coords = {
    'A': (100, 100),
    'B': (200, 200),
    'C': (300, 100),
    'D': (100, 300),
    'E': (400, 200),
    'H': (500, 100),
    'Z': (500, 300)
}

# Draw the nodes of the graph
node_radius = 20
for node, coord in node_coords.items():
    x, y = coord
    canvas.create_oval(x - node_radius, y - node_radius, x + node_radius, y + node_radius, fill="lightgray")
    canvas.create_text(x, y, text=city_names[node], font=font_style)

# Draw the edges of the graph
for node, edges in graph.items():
    x1, y1 = node_coords[node]
    for edge, distance in edges:
        x2, y2 = node_coords[edge]
        canvas.create_line(x1, y1, x2, y2)

root.mainloop()