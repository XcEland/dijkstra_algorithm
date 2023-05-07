import heapq
import tkinter as tk
from tkinter import ttk

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        queue = [(0, start)]
        visited = set()
        previous = {}

        while queue:
            (cost, vertex) = heapq.heappop(queue)

            if vertex in visited:
                continue

            visited.add(vertex)

            if vertex == finish:
                path = []
                while vertex in previous:
                    path.append(vertex)
                    vertex = previous[vertex]
                path.append(start)
                path.reverse()
                return path, distances[finish]

            for neighbor, cost in self.vertices[vertex].items():
                if neighbor in visited:
                    continue
                new_cost = distances[vertex] + cost

                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    previous[neighbor] = vertex
                    heapq.heappush(queue, (new_cost, neighbor))

        return [], float('inf')

    def get_shortest_path(self, start, finish):
        path, distance = self.shortest_path(start, finish)
        if distance == float('inf'):
            return "No path found"
        else:
            return f"Shortest path: {' -> '.join(path)} ({distance:.2f} km)"

class Application:
    def __init__(self, graph):
        self.graph = graph
        self.window = tk.Tk()
        self.window.title("Shortest Path Finder")
        self.canvas_width = 600
        self.canvas_height = 600
        self.create_widgets()
        self.draw_graph()

    def create_widgets(self):
        # Start city dropdown
        self.start_label = ttk.Label(self.window, text="Start City")
        self.start_label.grid(column=0, row=0)
        self.start_var = tk.StringVar()
        self.start_var.set('Harare')
        self.start_dropdown = ttk.Combobox(self.window, textvariable=self.start_var)
        self.start_dropdown['values'] = list(self.graph.vertices.keys())
        self.start_dropdown.grid(column=1, row=0)

        # End city dropdown
        self.end_label = ttk.Label(self.window, text="End City")
        self.end_label.grid(column=0, row=1)
        self.end_var = tk.StringVar()
        self.end_var.set('Harare')
        self.end_dropdown = ttk.Combobox(self.window, textvariable=self.end_var)
        self.end_dropdown['values'] = list(self.graph.vertices.keys())
        self.end_dropdown.grid(column=1, row=1)

        # Find path button
        self.button = ttk.Button(self.window, text="Find Shortest Path", command=self.calculate_shortest_path)
        self.button.grid(column=0, row=2)
        
         # Clear button
        self.clear_button = ttk.Button(self.window, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(column=1, row=2)

         # Exit button
        self.exit_button = ttk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.grid(column=2, row=2)
        
        # Result label
        self.result_var = tk.StringVar()
        self.result_label = ttk.Label(self.window, textvariable=self.result_var)
        self.result_label.grid(column=1, row=4)

        # Canvas for drawing the graph
        self.canvas = tk.Canvas(self.window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(column=2, row=0, rowspan=3)

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
                self.canvas.create_line(x1, y1, x2, y2)

        # Draw the circles and labels for each city
        for i, city in enumerate(self.graph.vertices):
            x, y = self.get_coords(city)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="white")
            self.canvas.create_text(x, y - 20, text=city)

    def draw_path(self, start, end):
        # Get the shortest path
        path, _ = self.graph.shortest_path(start, end)

        # Draw the lines for the shortest path
        for i in range(len(path) - 1):
            x1, y1 = self.get_coords(path[i])
            x2, y2 = self.get_coords(path[i+1])
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

        # Draw the circles and labels for the cities in the shortest path
        for city in path:
            x, y = self.get_coords(city)
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")
            self.canvas.create_text(x, y - 20, text=city)

    def get_coords(self, city):
        # This is just a simple function to calculate the coordinates of each city
        index = list(self.graph.vertices.keys()).index(city)
        x = 50 + (index % 4) * 100
        y = 50 + (index // 4) * 100
        return x, y
    
    
    def run(self):
        self.window.mainloop()

# Define the graph
graph = Graph()

graph.add_vertex('Harare', {'Bulawayo': 440, 'Mutare': 260, 'Masvingo': 300, 'Gweru': 280})
graph.add_vertex('Bulawayo', {'Harare': 440, 'Mutare': 580, 'Masvingo': 430, 'Gweru': 230, 'Kwekwe': 270})
graph.add_vertex('Mutare', {'Harare': 260, 'Bulawayo': 580, 'Masvingo': 280, 'Gweru': 410, 'Chinhoyi': 360})
graph.add_vertex('Masvingo', {'Harare': 300, 'Bulawayo': 430, 'Mutare': 280, 'Gweru': 200})
graph.add_vertex('Gweru', {'Harare': 280, 'Bulawayo': 230, 'Mutare': 410, 'Masvingo': 200, 'Kwekwe': 100})
graph.add_vertex('Kwekwe', {'Bulawayo': 270, 'Gweru': 100})
graph.add_vertex('Chinhoyi', {'Mutare': 360})

# Create the application
app = Application(graph)

# Run the application
app.run()