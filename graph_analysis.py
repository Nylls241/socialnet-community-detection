# === Graph analysis ===

def calculate_max_degree(graph):
    """
    Calculate the maximum degree of a graph.

    This function determines the highest number of neighbors (connections)
    that any node in the graph has.

    Args:
        graph (dict): A dictionary representing the graph, where keys are nodes
                      and values are lists of neighboring nodes.

    Returns:
        int: The maximum degree of the graph.

    Example:
        >>> g = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
        >>> calculate_max_degree(g)
        3
    """
    # Use a generator expression to get the length of each node's neighbor list
    # Then find the maximum value among these lengths
    return max(len(neighbors) for neighbors in graph.values())
