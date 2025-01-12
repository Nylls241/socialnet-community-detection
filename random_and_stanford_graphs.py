# === Random graph generation ===

import networkx as nx
import random
from graph_analysis import plot_degree_distribution, convert_adj_list_to_networkx

def generate_random_graph(num_vertices):
    """
    Generates a random undirected graph represented by an adjacency list.

    The graph is constructed by randomly creating edges between vertices. 
    The probability of an edge being created between any two vertices is determined by a 
    randomly chosen probability p (0 <= p <= 1).

    Args:
        num_vertices (int): The number of vertices in the graph.

    Returns:
        dict: A dictionary representing the adjacency list of the graph, where the keys are 
              vertices (from 0 to num_vertices - 1) and the values are lists of neighboring vertices.
    
    Example:
        >>> generate_random_graph(5)
        {0: [1, 3], 1: [0], 2: [], 3: [0], 4: []}
    """
    
    # Initialize an empty adjacency list for each vertex
    # This list adjacency represents a graph using lists where each vertex has a list of its directly connected neighbors, offering a space-efficient structure for sparse graphs.
    random_graph = {i: [] for i in range(num_vertices)}
    
    # Randomly choose a probability p
    p = random.uniform(0.01, 0.99)  # Ensure 0 < p < 1
    
    # Loop through all pairs (i, j) with i < j
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() <= p:  # Create an edge with probability p
                # Add the edge (i, j)
                random_graph[i].append(j)
                random_graph[j].append(i)
    
    return random_graph

def load_graph_from_file(filepath):
    """
    Load a graph from a text file into a NetworkX structure.

    Args:
        filepath (str): Path to the file containing the graph data. 
                        The file should have one edge per line, with two node IDs separated by a space.
    
    Returns:
        networkx.Graph: A NetworkX graph.
    """
    ST_graph = nx.Graph()
    with open(filepath, 'r') as file:  
        for line in file:  
            # Strip any whitespace or newline characters from the line and split it into two parts (node1 and node2)
            # Convert the split strings into integers using map(int, ...)
            node1, node2 = map(int, line.strip().split())  
            
            # Add an edge between node1 and node2 in the graph
            # This means node1 is connected to node2 in the network
            ST_graph.add_edge(node1, node2)

    return ST_graph

# Example usage
if __name__ == "__main__":
    # Create a sample graph
    G = convert_adj_list_to_networkx(generate_random_graph(5))  # Random graph with 100 nodes and edge probability 0.05
    plot_degree_distribution(G)