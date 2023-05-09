import heapq
import tkinter as tk
from tkinter import ttk
import os

import heapq
import tkinter as tk
from tkinter import ttk
import os

class Graph:
    def __init__(self):
        self.vertices = {}  # initialize an empty dictionary to store the vertices and their edges

    def add_vertex(self, name, edges):
        """
        Add a vertex to the graph with given name and edges.
        """
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        """
        Find the shortest path between the start and finish vertices in the graph using Dijkstra's algorithm.
        Returns a tuple consisting of the path as a list of vertex names and the total distance of the path.
        """
        distances = {vertex: float('inf') for vertex in self.vertices}  # initialize all distances to infinity
        distances[start] = 0  # set the distance of the starting vertex to 0
        queue = [(0, start)]  # create a priority queue with the starting vertex as the only element
        visited = set()  # initialize an empty set to keep track of visited vertices
        previous = {}  # initialize an empty dictionary to keep track of previous vertices on the path

        while queue:
            (cost, vertex) = heapq.heappop(queue)  # get the vertex with the smallest distance from the start

            if vertex in visited:  # if the vertex has already been visited, skip it
                continue

            visited.add(vertex)  # mark the vertex as visited

            if vertex == finish:  # if the finish vertex has been reached, return the path and distance
                path = []
                while vertex in previous:
                    path.append(vertex)
                    vertex = previous[vertex]
                path.append(start)
                path.reverse()
                return path, distances[finish]

            for neighbor, cost in self.vertices[vertex].items():  # for each neighbor of the current vertex
                if neighbor in visited:  # if the neighbor has already been visited, skip it
                    continue
                new_cost = distances[vertex] + cost  # calculate the new cost to reach the neighbor

                if new_cost < distances[neighbor]:  # if the new cost is less than the current distance to the neighbor
                    distances[neighbor] = new_cost  # update the distance to the neighbor
                    previous[neighbor] = vertex  # update the previous vertex on the path to the neighbor
                    heapq.heappush(queue, (new_cost, neighbor))  # add the neighbor to the priority queue

        return [], float('inf')  # if no path is found, return an empty path and infinity distance

    def get_shortest_path(self, start, finish):
        """
        Convenience method for calling the shortest_path method and returning a string representation of the result.
        """
        path, distance = self.shortest_path(start, finish)
        if distance == float('inf'):
            return "No path found"
        else:
            return f"Shortest path: {' -> '.join(path)} ({distance:.2f} km)"  # return the path and distance as a string

class Application:
    def __init__(self, graph):
        self.graph = graph
        self.window = tk.Tk()
        self.window.title("Shortest Path Finder")
        self.header_label = tk.Label(self.window, text="Find the Shortest Path Between Cities", font=("Arial", 24), bg="white")
        self.create_widgets()  # call the create_widgets method

        # Start city dropdown
        self.start_label = ttk.Label(self.window, text="Start City:")
        self.start_label.grid(column=0, row=0, padx=10, pady=10)
        self.start_var = tk.StringVar()
        self.start_var.set('Harare')
        self.start_dropdown = ttk.Combobox(self.window, textvariable=self.start_var, width=20)
        self.start_dropdown['values'] = list(self.graph.vertices.keys())
        self.start_dropdown.grid(column=1, row=0, padx=10, pady=10)

        # End city dropdown
        self.end_label = ttk.Label(self.window, text="End City:")
        self.end_label.grid(column=0, row=1, padx=10, pady=10)
        self.end_var = tk.StringVar()
        self.end_var.set('Harare')
        self.end_dropdown = ttk.Combobox(self.window, textvariable=self.end_var, width=20)
        self.end_dropdown['values'] = list(self.graph.vertices.keys())
        self.end_dropdown.grid(column=1, row=1, padx=10, pady=10)

        # Find path button
        self.button = ttk.Button(self.window, text="Show Shortest Path", command=self.calculate_shortest_path)
        self.button.grid(column=0, row=2, padx=10, pady=10)

        # Clear button
        self.clear_button = ttk.Button(self.window, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(column=1, row=2, padx=10, pady=10)

        # Exit button
        self.exit_button = ttk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.grid(column=1, row=3, padx=10, pady=10)
        
        # Define the function to execute the other Python file
        def execute_file():
            os.system('python other_file.py')

        # Generate graph
        self.graph_button = tk.Button(self.window, text='Execute Other File', command=execute_file)
        # self.graph_btn = ttk.Button(self.window, text='Graph', command=open_file)
        self.graph_button.grid(column=0, row=3, padx=10, pady=10)
        
        # Result label
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.window, textvariable=self.result_var, font=("Helvetica", 14))
        self.result_label.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

        # Canvas for drawing the graph
        self.canvas_width = 1000
        self.canvas_height = 700
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(column=2, row=0, rowspan=5, padx=10, pady=10)

        self.create_widgets()
        self.draw_graph()

    def create_widgets(self):
        # Title label
        self.title_label = ttk.Label(self.window, text="Shortest Path Finder", font=("Helvetica", 20, "bold"))
        self.title_label.grid(column=0, row=5, columnspan=3, pady=20)
        
    def calculate_shortest_path(self):
        start = self.start_var.get()
        end = self.end_var.get()

        # Draw the graph and highlight the shortest path
        self.draw_graph()
        self.draw_path(start, end)

        # Calculate the shortest path and display the result
        result = self.graph.get_shortest_path(start, end)
        self.result_var.set(result)

    def clear_inputs(self):
        self.start_var.set("")
        self.end_var.set("")
        self.result_var.set("")
        self.canvas.delete("all")

    def draw_graph(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Draw the edges between each city
        for city, edges in self.graph.vertices.items():
            for neighbor, cost in edges.items():
                x1, y1 = self.get_coords(city)
                x2, y2 = self.get_coords(neighbor)
                self.canvas.create_line(x1, y1, x2, y2, width=2)

        # Draw the circles and labels for each city
        for i, city in enumerate(self.graph.vertices):
            x, y = self.get_coords(city)
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white", width=2)
            self.canvas.create_text(x, y - 25, text=city, font=("Helvetica", 12))

    def draw_path(self, start, end):
        # Get the shortest path
        path, _ = self.graph.shortest_path(start, end)

        # Draw the lines for the shortest path
        for i in range(len(path) - 1):
            x1, y1 = self.get_coords(path[i])
            x2, y2 = self.get_coords(path[i+1])
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=5)

        # Draw the circles and labels for the cities in the shortest path
        for city in path:
            x, y = self.get_coords(city)
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red", width=2)
            self.canvas.create_text(x, y - 25, text=city, font=("Helvetica", 12))

    def get_coords(self, city):
        # This is just a simple function to calculate the coordinates of each city
        index = list(self.graph.vertices.keys()).index(city)
        x = 100 + (index % 4) * 150
        y = 100 + (index // 4) * 150
        return x, y
    
    
    def run(self):
        self.window.mainloop()

# Define the graph
graph = Graph()

graph.add_vertex('Beitbridge', {'Bulawayo': 323,'Chiredzi': 246, 'Masvingo': 290, 'Zvishavane':335 })
graph.add_vertex('Birchenough Bridge', {'Chiredzi':197, 'Masvingo':170, 'Mutare': 127 })
graph.add_vertex('Bulawayo', {'Beitbridge': 323, 'Gweru': 162, 'Zvishavane': 184})
graph.add_vertex('Chinhoyi', {'Harare': 116, 'Kadoma':126})
graph.add_vertex('Chiredzi', {'Beitbridge': 246,'Birchenough Bridge': 197, 'Masvingo': 204 })
graph.add_vertex('Gweru', {'Bulawayo': 162, 'Kwekwe': 66, 'Masvingo': 183, 'Zvishavane': 119})
graph.add_vertex('Harare', {'Chinhoyi': 116,'Kadoma': 142,  'Masvingo': 295, 'Marondera': 75})
graph.add_vertex('Kadoma', {'Chinhoyi': 126,'Harare': 142,  'Kwekwe': 74.2})
graph.add_vertex('Kwekwe', {'Gweru': 66, 'Kadoma': 74.2, 'Masvingo': 200})
graph.add_vertex('Masvingo', {'Beitbridge': 290,'Birchenough Bridge': 170, 'Chiredzi': 204, 'Gweru': 183, 'Harare': 295,   'Kwekwe': 200, 'Zvishavane': 97.1})
graph.add_vertex('Marondera', {'Harare': 75, 'Mutare': 186, 'Rusape': 96})
graph.add_vertex('Mutare', {'Birchenough Bridge': 127, 'Marondera': 186, 'Rusape': 92.6})
graph.add_vertex('Rusape', {'Marondera': 96, 'Mutare': 92.6})
graph.add_vertex('Zvishavane', {'Beitbridge': 335, 'Bulawayo': 184, 'Gweru': 119 ,'Masvingo': 97.1})

# Create the application
app = Application(graph)

# Run the application
app.run()