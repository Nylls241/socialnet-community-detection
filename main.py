from generate_graph import generate_random_graph
from graph_analysis import calculate_max_degree

if __name__ == "__main__":
    # --- Generate a random graph ---
    num_vertices = 3
    random_graph = generate_random_graph(num_vertices)

    print("Random graph:", random_graph)

    # --- Analysis of the generated graph ---
    print("Maximum degree:", calculate_max_degree(random_graph))