import random_and_stanford_graphs as rg
import graph_analysis as ga
import networkx as nx

def main_menu():
    graphs = []  # Store up to 5 graphs

    # Load Stanford graphs into the graph list at the start
    stanford_graph_files = [
        ("facebook_combined.txt", "Facebook Combined Graph"),
        ("email-Eu-core-department-labels.txt", "Email Eu-core Department Graph"),
        ("lastfm_asia_edges.txt", "LastFM Asia Graph")
    ]

    for file_path, description in stanford_graph_files:
        try:
            stanford_graph = rg.load_graph_from_file(file_path)
            graphs.append((stanford_graph, description))
            print(f"Loaded {description} from {file_path}.")
        except FileNotFoundError:
            print(f"File {file_path} not found. Skipping {description}.")

    while True:
        print("\nGraph Testing Menu")
        print("1. Generate Random Graph")
        print("2. Calculate Maximum Degree of a Stored Graph")
        print("3. View All Stored Graphs")
        print("4. Plot Degree Distribution of a Stored Graph")
        print("5. Count Induced Paths of Length 2 in a Stored Graph")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                if len(graphs) >= 8:  # Max 5 user-generated + 3 Stanford graphs
                    print("\nYou can only store up to 5 additional graphs. Please restart the program to reset.")
                else:
                    num_vertices = int(input("Enter the number of vertices: "))
                    random_graph = rg.generate_random_graph(num_vertices)
                    graphs.append((random_graph, f"Random Graph #{len(graphs) - 3}"))
                    print(f"\nGenerated Random Graph #{len(graphs) - 3} (Adjacency List):")
                    for node, neighbors in random_graph.items():
                        print(f"{node}: {neighbors}")

                    print("\nGraph stored. You can now calculate its maximum degree, plot its degree distribution, count induced paths, or generate more graphs.")

            elif choice == 2:
                if not graphs:
                    print("\nNo graphs available. Please generate a graph first.")
                else:
                    print("\nChoose a graph to calculate its maximum degree:")
                    for i, (graph, description) in enumerate(graphs):
                        print(f"{i + 1}. {description}")

                    try:
                        graph_choice = int(input("Enter the graph number: "))
                        if 1 <= graph_choice <= len(graphs):
                            selected_graph, description = graphs[graph_choice - 1]
                            if isinstance(selected_graph, dict):
                                nx_graph = ga.convert_adj_list_to_networkx(selected_graph)
                            else:
                                nx_graph = selected_graph
                            max_degree = ga.calculate_max_degree(nx_graph)
                            print(f"\nMaximum Degree of {description}: {max_degree}")
                        else:
                            print("Invalid graph number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid graph number.")

            elif choice == 3:
                if not graphs:
                    print("\nNo graphs stored.")
                else:
                    print("\nStored Graphs:")
                    for i, (_, description) in enumerate(graphs):
                        print(f"{i + 1}. {description}")

            elif choice == 4:
                if not graphs:
                    print("\nNo graphs available. Please generate a graph first.")
                else:
                    print("\nChoose a graph to plot its degree distribution:")
                    for i, (graph, description) in enumerate(graphs):
                        print(f"{i + 1}. {description}")

                    try:
                        graph_choice = int(input("Enter the graph number: "))
                        if 1 <= graph_choice <= len(graphs):
                            selected_graph, description = graphs[graph_choice - 1]
                            if isinstance(selected_graph, dict):
                                nx_graph = ga.convert_adj_list_to_networkx(selected_graph)
                            else:
                                nx_graph = selected_graph
                            ga.plot_degree_distribution(nx_graph)
                            print(f"\nPlotted degree distribution for {description}.")
                        else:
                            print("Invalid graph number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid graph number.")

            elif choice == 5:
                if not graphs:
                    print("\nNo graphs available. Please generate a graph first.")
                else:
                    print("\nChoose a graph to count induced paths of length 2:")
                    for i, (graph, description) in enumerate(graphs):
                        print(f"{i + 1}. {description}")

                    try:
                        graph_choice = int(input("Enter the graph number: "))
                        if 1 <= graph_choice <= len(graphs):
                            selected_graph, description = graphs[graph_choice - 1]
                            if isinstance(selected_graph, dict):
                                nx_graph = ga.convert_adj_list_to_networkx(selected_graph)
                            else:
                                nx_graph = selected_graph
                            induced_paths = ga.count_induced_paths_length_2(nx_graph)
                            print(f"\nNumber of induced paths of length 2 in {description}: {induced_paths}")
                        else:
                            print("Invalid graph number. Please try again.")
                    except ValueError:
                        print("Invalid input. Please enter a valid graph number.")

            elif choice == 6:
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main_menu()
