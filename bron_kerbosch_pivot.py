import networkx as nx
import random

def bron_kerbosch_pivot(R, P, X, graph):
    """
    Bron-Kerbosch algorithm with pivot for finding maximal cliques in a graph.

    Args:
        R (set): Current clique being constructed.
        P (set): Potential nodes that can extend the clique.
        X (set): Nodes already processed.
        graph (networkx.Graph): The graph being analyzed.

    Yields:
        set: A maximal clique.
    """
    if not P and not X:
        yield R
    else:
        # Choose a pivot (heuristic: a vertex from P ∪ X with the most neighbors in P)
        pivot = next(iter(P.union(X)))
        for v in P - set(graph.neighbors(pivot)):
            yield from bron_kerbosch_pivot(
                R.union({v}),
                P.intersection(graph.neighbors(v)),
                X.intersection(graph.neighbors(v)),
                graph
            )
            P.remove(v)
            X.add(v)

def find_maximal_cliques(graph):
    """
    Finds all maximal cliques in a graph using Bron-Kerbosch algorithm with pivot.

    Args:
        graph (networkx.Graph): The input graph.

    Returns:
        list[set]: A list of maximal cliques (each represented as a set of nodes).
    """
    return list(bron_kerbosch_pivot(set(), set(graph.nodes), set(), graph))

# --- Example Usage ---
if __name__ == "__main__":
    # Small graph example
    G_small = nx.Graph()
    G_small.add_edges_from([
        (1, 2), (1, 3), (2, 3),  # Clique: {1, 2, 3}
        (3, 4), (4, 5)           # Clique: {4, 5}
    ])

    print("Maximal cliques in the small graph:")
    for clique in find_maximal_cliques(G_small):
        print(clique)

    # Random graph example (from first part)
    def generate_random_graph(num_nodes, edge_probability):
        G = nx.Graph()
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() < edge_probability:
                    G.add_edge(i, j)
        return G

    G_large = generate_random_graph(100, 0.05)  # Adjust size and probability for testing
    cliques = find_maximal_cliques(G_large)

    print(f"\nNumber of maximal cliques in the large graph: {len(cliques)}")
    print("Sample of maximal cliques:")
    for clique in cliques[:5]:  # Print only the first 5 cliques for brevity
        print(clique)
