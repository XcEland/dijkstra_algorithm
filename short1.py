import heapq
import tkinter as tk

# Define the graph as a dictionary with vertices as keys and a list of tuples as values
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('C', 3), ('E', 5)],
    'C': [('E', 1), ('F', 6)],
    'D': [('E', 8), ('G', 6)],
    'E': [('F', 4), ('H', 4)],
    'F': [('H', 1), ('I', 7)],
    'G': [('H', 9), ('J', 8)],
    'H': [('I', 2), ('J', 3)],
    'I': [('J', 5)]
}

# Define a dictionary for city names
city_names = {
    'A': 'City A',
    'B': 'City B',
    'C': 'City C',
    'D': 'City D',
    'E': 'City E',
    'F': 'City F',
    'G': 'City G',
    'H': 'City H',
    'I': 'City I',
    'J': 'City J'
}

def dijkstra(graph, start, end):
    # Initialize distances and visited nodes
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()
    # Initialize heap
    heap = [(0, start)]
    # Traverse the graph using Dijkstra's algorithm
    while heap:
        (current_distance, current_vertex) = heapq.heappop(heap)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for (neighbour, weight) in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(heap, (distance, neighbour))
    # Return shortest distance and path
    shortest_distance = distances[end]
    path = [end]
    while end != start:
        for (vertex, weight) in graph[end]:
            if distances[vertex] == distances[end] - weight:
                path.append(vertex)
                end = vertex
    path.reverse()
    return (shortest_distance, path)

# Create the Tkinter GUI
root = tk.Tk()
root.title("Shortest Distance between Zimbabwean Cities")

# Define the function to calculate the shortest distance and display the result
def calculate_distance():
    source = source_var.get()
    destination = destination_var.get()
    shortest_distance, path = dijkstra(graph, source, destination)
    result_label.config(text=f"The shortest distance from {city_names[source]} to {city_names[destination]} is {shortest_distance} km via {' -> '.join([city_names[city] for city in path])}")

# Create the source city label and combo box
source_label = tk.Label(root, text="Source City:")
source_label.grid(row=0, column=0, padx=5, pady=5)
source_var = tk.StringVar()
source_var.set('A')
source_combo = tk.OptionMenu(root, source_var, *list(city_names.keys()))
source_combo.grid(row=0, column=1, padx=5, pady=5)

# Create the destination city label and combo box
destination_label = tk.Label(root, text="Destination City:")
destination_label.grid(row=1, column=0, padx=5, pady=5)
destination_var = tk.StringVar()
destination_var.set('B')
destination_combo = tk.OptionMenu(root, destination_var, *list(city_names.keys()))
destination_combo.grid(row=1, column=1, padx=5, pady=5)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_distance)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Create the result label
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()