from generate_graph import generate_random_graph

if __name__ == "__main__":
    # --- Generate a random graph ---
    num_vertices = 10
    random_graph = generate_random_graph(num_vertices)

    print("Random graph:", random_graph)