import heapq
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Define the Graph as a dictionary of dictionaries
graph = {
    'A': {'B': 350, 'C': 270},
    'B': {'A': 350, 'C': 200, 'D': 180, 'E': 240},
    'C': {'A': 270, 'B': 200, 'F': 300},
    'D': {'B': 180},
    'E': {'B': 240, 'G': 400},
    'F': {'C': 300},
    'G': {'E': 400},
}

# Define a function to find the shortest path between two cities
def find_shortest_path(graph, start, end):
    # Initialize the heap and visited set
    heap = [(0, start)]  # A heap to store the vertices and their distance
    visited = set()     # A set to store the visited vertices
    
    # Initialize the distances dictionary
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Loop until the heap is empty
    while heap:
        # Pop the smallest item from the heap
        (current_distance, current_vertex) = heapq.heappop(heap)

        # If we have already visited this vertex, continue to the next iteration
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Update distances and add unvisited neighbors to the heap
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    # Return the shortest path as a list of vertices
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = min(
            [(vertex, distances[vertex]) for vertex in graph[current_vertex] if vertex in visited],
            key=lambda x: x[1])[0]
    path.insert(0, start)
    
    # Return the shortest path and its distance
    return path, distances[end]

# Test the function by finding the shortest path between 'Harare' (A) and 'Chinhoyi' (G)
start_city = 'A'
end_city = 'G'
city_key = {'A': 'Harare', 'B': 'Bulawayo', 'C': 'Mutare', 'D': 'Gweru', 'E': 'Masvingo', 'F': 'Bindura', 'G': 'Chinhoyi'}
shortest_path, distance = find_shortest_path(graph, start_city, end_city)

# Print the results
start_city_name = city_key[start_city]
end_city_name = city_key[end_city]
print(f"The shortest path from {start_city_name} to {end_city_name} is {shortest_path}, with a distance of {distance} kilometers.")





#Define the Graph as a dictionary of dictionaries
graph = {
    'A': {'B': 350, 'C': 270},
    'B': {'A': 350, 'C': 200, 'D': 180, 'E': 240},
    'C': {'A': 270, 'B': 200, 'F': 300},
    'D': {'B': 180},
    'E': {'B': 240, 'G': 400},
    'F': {'C': 300},
    'G': {'E': 400},
}

# Define a function to find the shortest path between two cities
def find_shortest_path(graph, start, end):
    # Initialize the heap and visited set
    heap = [(0, start)]  # A heap to store the vertices and their distance
    visited = set()     # A set to store the visited vertices
    
    # Initialize the distances dictionary
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    
    # Loop until the heap is empty
    while heap:
        # Pop the smallest item from the heap
        (current_distance, current_vertex) = heapq.heappop(heap)

        # If we have already visited this vertex, continue to the next iteration
        if current_vertex in visited:
            continue

        # Mark the current vertex as visited
        visited.add(current_vertex)

        # Update distances and add unvisited neighbors to the heap
        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    # Return the shortest path as a list of vertices
    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = min(
            [(vertex, distances[vertex]) for vertex in graph[current_vertex] if vertex in visited],
            key=lambda x: x[1])[0]
    path.insert(0, start)
    
    # Return the shortest path and its distance
    return path, distances[end]

# Define a function to find the shortest path between two cities based on user input
def find_shortest_path_ui(start_city, end_city):
    # Convert city names to corresponding vertices in the graph
    vertices_key = {v: k for k, v in city_key.items()}
    start_vertex = vertices_key[start_city]
    end_vertex = vertices_key[end_city]
    
    # Find the shortest path and its distance
    shortest_path, distance = find_shortest_path(graph, start_vertex, end_vertex)
    
    # Convert vertex names back to city names
    shortest_path_city = [city_key[vertex] for vertex in shortest_path]
    
    # Print and return the results
    print(f"The shortest path from {start_city} to {end_city} is {shortest_path_city}, with a distance of {distance} kilometers.")
    return shortest_path_city

# Define a list of cities to use as a drop-down menu for the user interface
cities = ['Harare', 'Bulawayo', 'Mutare', 'Gweru', 'Masvingo', 'Bindura', 'Chinhoyi']

# Define a dictionary to convert between city names and vertices
city_key = {'A': 'Harare', 'B': 'Bulawayo', 'C': 'Mutare', 'D': 'Gweru', 'E': 'Masvingo', 'F': 'Bindura', 'G': 'Chinhoyi'}

# Define the user interface
# @interact(start=Dropdown(options=cities, description='Start city: '), 
#           end=Dropdown(options=cities, description='End city: '))
# def shortest_path_ui(start, end):
#     shortest_path_city = find_shortest_path_ui(start, end)
#     return shortest_path_city

# Create the Tkinter GUI
root = tk.Tk()
root.title("Shortest Distance between Zimbabwean Cities")

# Create the source city label and combo box
source_label = tk.Label(root, text="Source City:")
source_label.grid(row=0, column=0, padx=5, pady=5)
source_var = tk.StringVar() 
source_var.set('A')
source_combo = tk.OptionMenu(root, source_var, *list(city_key.keys()))
source_combo.grid(row=0, column=1, padx=5, pady=5)

# Create the destination city label and combo box
destination_label = tk.Label(root, text="Destination City:")
destination_label.grid(row=1, column=0, padx=5, pady=5)
destination_var = tk.StringVar()
destination_var.set('B')
destination_combo = tk.OptionMenu(root, destination_var, *list(city_key.keys()))
destination_combo.grid(row=1, column=1, padx=5, pady=5)

# Create the calculate button
# calculate_button = tk.Button(root, text="Calculate", command=calculate_distance)
# calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()