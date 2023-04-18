import math

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

# Import the Tkinter library for the GUI
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()

# Set the window size and position
# root.geometry("800x600")
# root.resizable(False, False)

# Set the window title and background color
root.title("Shortest Path Finder - by Your Name")
root.configure(bg='lightgray')

# Define the font and size for the text and buttons
font_style = ("Arial", 18)

# Create a header label
header_label = tk.Label(root, text="Shortest Path Finder", font=font_style, bg='lightgray')
header_label.pack(pady=20)

# Create a label for the source input
source_label = tk.Label(root, text="Source:", font=font_style, bg='lightgray')
source_label.pack(side=tk.LEFT, padx=10, pady=10)

# Create an entry field for the source input
source_entry = tk.Entry(root, font=font_style, width=10)
source_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label for the destination input
destination_label = tk.Label(root, text="Destination:", font=font_style, bg='lightgray')
destination_label.pack(side=tk.LEFT, padx=10, pady=10)

# Create an entry field for the destination input
destination_entry = tk.Entry(root, font=font_style, width=10)
destination_entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button for submitting the inputs
submit_button = tk.Button(root, text="Submit", font=font_style, width=10, height=2)
submit_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button for clearing the inputs
def clear_inputs():
    source_entry.delete(0, tk.END)
    destination_entry.delete(0, tk.END)

clear_button = tk.Button(root, text="Clear", font=font_style, width=10, height=2, command=clear_inputs)
clear_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create a label for the key
key_label = tk.Label(root, text="Key: A=Harare, B=Bulawayo, C=Mutare, D=Gweru, E=Kwekwe, F=Masvingo, G=Chinhoyi, H=Mutoko, I=Hwange, J=Victoria Falls", font=font_style, bg='lightgray')
key_label.pack(pady=20)

# Define a function to handle the submit button click
def submit_inputs():
    start = source_entry.get().upper()
    end = destination_entry.get().upper()
    if start not in zimbabwe.vertices or end not in zimbabwe.vertices:
        result_label.config(text="Please enter valid source and destination")
    else:
        path, distance = zimbabwe.shortest_path(start, end)
        path_str = " -> ".join(path)
        result_label.config(text=f"Shortest path: {path_str} ({distance} km)")

# Assign the submit_inputs() function to the submit button
submit_button.config(command=submit_inputs)

# Create a label for displaying the results
result_label = tk.Label(root, text="", font=font_style, bg='lightgray')
result_label.pack(pady=20)

# Start the main event loop
root.mainloop()