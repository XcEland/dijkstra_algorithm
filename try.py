# Import the Tkinter library for the GUI
import tkinter as tk
from tkinter import ttk
import math

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
    'I': 'Zvishavane',
    'J': 'Marondera'
}


class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        self.vertices[vertex] = {}
        
    def add_edge(self, start, end, weight):
        self.vertices[start][end] = weight
        self.vertices[end][start] = weight
        
    def shortest_path(self, start, end):
        distances = {}
        for vertex in self.vertices:
            distances[vertex] = math.inf
        distances[start] = 0
        
        visited = set()
        while len(visited) < len(self.vertices):
            current_vertex = None
            current_distance = math.inf
            for vertex in self.vertices:
                if vertex not in visited and distances[vertex] < current_distance:
                    current_vertex = vertex
                    current_distance = distances[vertex]
            visited.add(current_vertex)
            for neighbor, weight in self.vertices[current_vertex].items():
                global 
                distance
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
        
        path = [end]
        current_vertex = end
        while current_vertex != start:
            for neighbor, weight in self.vertices[current_vertex].items():
                if distances[neighbor] < distances[current_vertex]:
                    path.append(neighbor)
                    current_vertex = neighbor
                    break
        path.reverse()
        return path, distances[end]

# Create a graph of 10 cities in Zimbabwe
zimbabwe = Graph()
zimbabwe.add_vertex("A")
zimbabwe.add_vertex("B")
zimbabwe.add_vertex("C")
zimbabwe.add_vertex("D")
zimbabwe.add_vertex("E")
zimbabwe.add_vertex("F")
zimbabwe.add_vertex("G")
zimbabwe.add_vertex("H")
zimbabwe.add_vertex("I")
zimbabwe.add_vertex("J")
zimbabwe.add_edge("A", "B", 50)
zimbabwe.add_edge("A", "C", 70)
zimbabwe.add_edge("A", "D", 80)
zimbabwe.add_edge("B", "C", 30)
zimbabwe.add_edge("B", "E", 90)
zimbabwe.add_edge("C", "D", 20)
zimbabwe.add_edge("C", "F", 60)
zimbabwe.add_edge("D", "G", 110)
zimbabwe.add_edge("E", "H", 100)
zimbabwe.add_edge("F", "I", 40)
zimbabwe.add_edge("G", "J", 70)
zimbabwe.add_edge("H", "I", 50)
zimbabwe.add_edge("I", "J", 30)

# Create the main window
root = tk.Tk()

# Set the window size and position
root.geometry("800x600")
# root.resizable(False, False)

# Set the window title and background color
root.title("Shortest Path Finder - ")
root.configure(bg='lightgray')

# Define the font and size for the text and buttons
font_style = ("Arial", 18)

# Create a header label
header_label = tk.Label(root, text="Shortest Path Finder", font=font_style, bg='lightgray')
header_label.pack(pady=20)
#try 
# Create the source city label and combo box
source_label = tk.Label(root, text="Source City:")
source_label.pack(side=tk.LEFT, padx=10, pady=10)
source_entry = tk.StringVar(root)
source_entry.set('Harare')
source_combo = tk.ttk.Combobox(root, textvariable=source_entry, values=list(city_names.values()))
source_combo.pack(side=tk.LEFT, padx=10, pady=10)

# Create the destination city label and combo box
dest_label = tk.Label(root, text="Destination City:")
dest_label.pack(side=tk.LEFT, padx=10, pady=10)
destination_entry = tk.StringVar(root)
destination_entry.set('Bulawayo')
dest_combo = tk.ttk.Combobox(root, textvariable=destination_entry, values=list(city_names.values()))
dest_combo.pack(side=tk.LEFT, padx=10, pady=10)

#try/ 

# Define a function to handle the submit button click
def submit_inputs():
    start = None
    end = None
    
    # Get the source and destination cities from the dropdown menus
    for key, value in city_names.items():
        if value == source_entry.get():
            start = key
        if value == destination_entry.get():
            end = key
            
    # Find the shortest path and display it
    shortest_path = zimbabwe.shortest_path(start, end)
    if start not in zimbabwe.vertices:
        result_label.config(text="Please enter valid source")
    elif end not in zimbabwe.vertices:
        result_label.config(text="Please enter valid destination")
    elif start not in zimbabwe.vertices and end not in zimbabwe.vertices:
        result_label.config(text="Please enter valid source and destination")
    else:
        path, distance = shortest_path(start, end)
        path_str = " -> ".join(path)
        # path_str = ' -> '.join([city_names[vertex] for vertex in shortest_path])
        result_label.config(text=f"Shortest path: {path_str} ({distance} km)")

# Assign the submit_inputs() function to the submit button
submit_button = tk.Button(root, text="Find Shortest Path", command=submit_inputs)
submit_button.pack(side=tk.RIGHT, padx=10, pady=10)
submit_button.config(command=submit_inputs)
# Create a label for displaying the results
result_label = tk.Label(root, text="", font=font_style, bg='lightgray')
result_label.pack(side=tk.LEFT, pady=20)

# Start the main event loop
root.mainloop()