import random

def select_random_probability():
    """
    Selects a random probability p in the range (0, 1).
    
    Returns:
        float: A random probability between 0 and 1 (exclusive).
    """
    return random.uniform(0.01, 0.99) # Ensure 0 < p < 1

def generate_random_graph(num_vertices):
    """
    Generates a random undirected graph based on a probability.
    
    Args:
        num_vertices (int): The number of vertices in the graph.
    
    Returns:
        list of tuples: Each tuple represents an edge between two vertices.
    """
    p = select_random_probability()
    edges = []
    
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() <= p: # Check if a random value is within probability p.
                edges.append((i, j))
    
    return edges

def store_as_adjacency_list(edges, num_vertices):
    """
    Stores edges in an adjacency list format.
    
    Args:
        edges (list of tuples): List of edges, where each edge is represented as a tuple (i, j).
        num_vertices (int): The number of vertices in the graph.
    
    Returns:
        dict: An adjacency list representation of the graph.
    """
    adjacency_list = {i: [] for i in range(num_vertices)}
    
    for (i, j) in edges:
        adjacency_list[i].append(j)
        adjacency_list[j].append(i)
    
    return adjacency_list
