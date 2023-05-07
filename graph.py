import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
G = nx.Graph()

# Add nodes for 14 cities
cities = ['A', 'B', 'C', 'D', 'E', 'F', 'H', 'J', 'K', 'L', 'M', 'N', 'P']
G.add_nodes_from(cities)

# Define the edges between the cities
edges = [('A', 'C'),('A', 'H'),('A', 'K'),('A', 'D') , 
         ('B', 'E'),('B', 'J'),('B', 'M'),
         ('C', 'H'),('C', 'A'),
         ('D', 'E'),('D', 'A'),('D', 'M'),('D', 'N'),('D', 'E'),('D', 'J'),('D', 'F'),
         ('E', 'B'),('E', 'J'),('E', 'D'),('E', 'F'), 
         ('F', 'H'),('F', 'E'),('F', 'D'),
         ('H', 'C'),('H', 'F'),('H', 'A'),
         ('J', 'B'),('J', 'E'),('J', 'D'),('J', 'M'),
         ('K', 'A'),('K', 'C'),('K', 'L'),
         ('L', 'K'),('L', 'C'),
         ('M', 'B'),('M', 'D'),('M', 'J'),('M', 'N'),
         ('N', 'M'),('N', 'D'),('N', 'P'),
         ('P', 'D'),('P', 'N'),('P', 'C')]

# Add the edges to the graph
G.add_edges_from(edges)

# Draw the graph
nx.draw_networkx(G, with_labels=True)


# Show the plot
plt.show()