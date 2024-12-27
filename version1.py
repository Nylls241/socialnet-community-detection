import random

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
    graph = {i: [] for i in range(num_vertices)}
    
    # Randomly choose a probability p
    p = random.uniform(0.01, 0.99)  # Ensure 0 < p < 1
    
    # Loop through all pairs (i, j) with i < j
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.random() <= p:  # Create an edge with probability p
                # Add the edge (i, j)
                graph[i].append(j)
                graph[j].append(i)
    
    return graph
