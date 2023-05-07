# Import modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import math
import heapq

# Create a dictionary to store the city names
city_names = {
    'A': 'Harare',
    'B': 'Bulawayo',
    'C': 'Mutare',
    'D': 'Masvingo',
    'E': 'Gweru',
    'F': 'Kwekwe',
    'G': 'Chinhoyi',
    'H': 'Kadoma',
    'J': 'Zvishavane',
    'K': 'Marondera',
    'L': 'Rusape',
    'M': 'Beitbridge',
    'N': 'Chiredzi',
    'P': 'Birchenough Bridge'
}

# Create the graph
graph = {
    'A': [('D', 295), ('G', 116), ('H', 142), ('K', 75)],
    'B': [('M', 323), ('J', 184), ('E', 162)],
    'C': [('P', 127), ('L', 92.6), ('K', 189)],
    'D': [('M', 290), ('N', 204), ('P', 170), ('J', 97.1), ('A', 295), ('F', 200), ('E', 183)],
    'E': [('B', 162), ('D', 183), ('F', 66), ('J', 119)],
    'F': [('E', 66), ('H', 74.2), ('D', 200)],
    'G': [('A', 116), ('H', 126)],
    'H': [('A', 142), ('G', 126), ('F', 74.2)],
    'J': [('B', 184), ('D', 97.1), ('E', 119), ('M', 335)],
    'K': [('A', 75), ('C', 189), ('L', 96)],
    'L': [('C', 92.6), ('K', 96)],
    'M': [('B', 323), ('D', 290), ('N', 246), ('J', 335)],
    'N': [('P', 197), ('M', 246), ('D', 204)],
    'P': [('C', 127), ('D', 170), ('N', 197)]
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
header_label = tk.Label(root, text="Find the Shortest Path Between Cities", font=("Arial", 24), bg="white")
header_label.pack(pady=20)

author_label = tk.Label(root, text="by Mcdonald Mpofu R199178D", font=("Arial", 18), bg="white")
author_label.pack()

# Create the source city label and combo box
source_label = tk.Label(root, text="Source City:")
source_label.pack(side=tk.LEFT, padx=10, pady=10)
source_var = tk.StringVar(root)
source_var.set('Harare')
source_combo = tk.ttk.Combobox(root, textvariable=source_var, values=list(city_names.values()))
source_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the destination city label and combo box
dest_label = tk.Label(root, text="Destination City:")
dest_label.pack(side=tk.LEFT, padx=10, pady=10)
dest_var = tk.StringVar(root)
dest_var.set('Bulawayo')
dest_combo = tk.ttk.Combobox(root, textvariable=dest_var, values=list(city_names.values()))
dest_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the button to find the shortest path
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
    else:
        result_label.config(text="No path found")

find_button = tk.Button(root, text="Calculate", command=find_shortest_path)
find_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(root, text="")
result_label.pack(side=tk.RIGHT, padx=10, pady=10)
root.mainloop()