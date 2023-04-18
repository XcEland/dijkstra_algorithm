import tkinter as tk
import heapq

# Create a dictionary to store the city names
city_names = {
    'A': 'Harare',
    'B': 'Bulawayo',
    'C': 'Mutare',
    'D': 'Masvingo',
    'E': 'Gweru',
    'F': 'Kwekwe',
    'G': 'Chinhoyi'
}

# Create the graph
graph = {
    'A': [('B', 100), ('C', 50)],
    'B': [('A', 100), ('D', 200), ('E', 75)],
    'C': [('A', 50), ('D', 125)],
    'D': [('B', 200), ('C', 125), ('E', 75)],
    'E': [('B', 75), ('D', 75), ('F', 125), ('G', 200)],
    'F': [('E', 125), ('G', 75)],
    'G': [('E', 200), ('F', 75)]
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

# Create the label and dropdown menu for the source city
source_label = tk.Label(root, text="Source City:")
source_label.pack(side=tk.LEFT, padx=10, pady=10)

source_var = tk.StringVar(root)
source_var.set('Harare')  # Set the default value to Harare

source_menu = tk.OptionMenu(root, source_var, *city_names.values())
source_menu.pack(side=tk.LEFT, padx=10, pady=10)

# Create the label and dropdown menu for the destination city
dest_label = tk.Label(root, text="Destination City:")
dest_label.pack(side=tk.LEFT, padx=10, pady=10)

dest_var = tk.StringVar(root)
dest_var.set('Kwekwe')  # Set the default value to Kwekwe

dest_menu = tk.OptionMenu(root, dest_var, *city_names.values())
dest_menu.pack(side=tk.LEFT, padx=10, pady=10)

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
        result_label.config(text=f"Shortest path: {path_str}")
    else:
        result_label.config(text="No path found")

find_button = tk.Button(root, text="Find Shortest Path", command=find_shortest_path)
find_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the label to display the result
result_label = tk.Label(root, text="")
result_label.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()