import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from collections import Counter

# === Maximum degree of the graph ===
def calculate_max_degree(graph):
    """
    Calculate the maximum degree of a graph.

    Args:
        graph (networkx.Graph): The input graph.
    
    Returns:
        int: The maximum degree of the graph.
    """
    max_degree = max(graph.degree())
    return max_degree[1]

# === NetworkX conversion ===
def convert_adj_list_to_networkx(adj_list):
    """
    Converts a graph represented as an adjacency list (dictionary) 
    into a NetworkX graph.

    Args:
        adj_list (dict): A dictionary where the keys are nodes and the 
                         values are lists of neighboring nodes.

    Returns:
        networkx.Graph: A NetworkX graph representing the same structure 
                        as the input adjacency list.

    Example:
        >>> adj_list = {
        ...     0: [1, 2],
        ...     1: [0],
        ...     2: [0]
        ... }
        >>> nx_graph = convert_adj_list_to_networkx(adj_list)
        >>> list(nx_graph.edges())
        [(0, 1), (0, 2)]
    """
    # Use NetworkX's from_dict_of_lists method to convert
    nx_graph = nx.from_dict_of_lists(adj_list)
    return nx_graph

def plot_degree_distribution(G):
    """
    Plots the degree distribution of a graph.

    Args:
        G (networkx.Graph): The input graph.

    This function calculates the degree distribution of the input graph and plots it as a bar chart.
    The x-axis represents the degree, and the y-axis represents the number of vertices with that degree.
    """
    degree_count = {}
    for node in G.nodes():
        degree = G.degree(node)
        if degree in degree_count:
            degree_count[degree] += 1
        else:
            degree_count[degree] = 1

    # Sort degrees and their counts
    degrees, counts = zip(*sorted(degree_count.items()))
    
    # Plot
    plt.bar(degrees, counts, width=0.8, color='skyblue', edgecolor='black')
    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Number of Vertices")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(degrees)  # Ensure all degrees are visible
    plt.show()

def count_induced_paths_length_2(graph):
    """
    Counts the number of induced paths of length 2 in the graph.

    Args:
        graph (networkx.Graph): The input graph.

    Returns:
        int: The number of induced paths of length 2.
    """
    count = 0
    for node in graph.nodes:
        # Get neighbors of the current node
        neighbors = list(graph.neighbors(node))
        
        # Iterate over all pairs of neighbors
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                neighbor1 = neighbors[i]
                neighbor2 = neighbors[j]
                
                # Check if there is no edge between neighbor1 and neighbor2
                if not graph.has_edge(neighbor1, neighbor2):
                    count += 1

    return count
