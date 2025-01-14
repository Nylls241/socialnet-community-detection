# socialnet-community-detection
Detection of communities in social networks

## Table of Contents

- [socialnet-community-detection](#socialnet-community-detection)
  - [Table of Contents](#table-of-contents)
  - [Directory Structure](#directory-structure)
  - [Key Features](#key-features)
  - [Installation](#installation)
  - [Run the menu](#run-the-menu)
  - [Usage](#usage)

## Directory Structure
```
└── nylls241-socialnet-community-detection/
    ├── README.md                     # Project documentation
    ├── LICENSE                       # License for the project
    ├── __init__.py                   # Marks the directory as a Python package
    ├── email-Eu-core-department-labels.txt # Dataset containing email network labels
    ├── facebook_combined.txt         # Dataset of Facebook social network edges
    ├── graph_analysis.py             # Script for analyzing graphs
    ├── lastfm_asia_edges.txt         # Dataset of LastFM Asia social network edges
    ├── main.py                       # Main script to run the program
    ├── random_and_stanford_graphs.py # Script for generating and analyzing random/Stanford graphs
    └── requirements.txt              # List of dependencies for the project
```

## Key Features
- Analyze and detect communities in social networks using various datasets.
- Support for multiple datasets, including email networks, Facebook, and LastFM Asia.
- Scripts for advanced graph analysis and community detection.
- Generate random graphs for testing and comparison with standard datasets.
- Easy-to-follow menu-driven interface for running the program.

## Installation

1. Create and activate a virtual environment: 
Open a terminal, go to the project directory, and type:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Run the menu
```sh
python main.py
```

## Usage
1. **Analyze a specific dataset**:
   - Place the dataset file in the project directory.
   - Run the program and select the option to analyze the dataset from the menu.

2. **Generate and analyze random graphs**:
   - Use the `random_and_stanford_graphs.py` script to create random graphs.
   - Analyze the generated graphs using the `graph_analysis.py` script.

3. **Customize analysis**:
   - Modify the `graph_analysis.py` script to adjust the analysis logic as needed.

4. **Extend functionality**:
   - Add new datasets or implement additional algorithms to enhance community detection capabilities.


