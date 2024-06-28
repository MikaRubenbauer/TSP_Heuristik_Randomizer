
# Project_TSP

This project addresses the Travelling Salesman Problem (TSP) and implements two algorithms to solve the problem:

Minimal Tour: An exact algorithm that checks all possible permutations of cities to find the shortest possible tour.
Tour Approximation: A heuristic algorithm that uses a statistical randomization mechanism to quickly find a reasonable, though not necessarily optimal, solution.


## Features

Exact Solution: Finds the shortest possible tour by evaluating all permutations.
Approximation Solution: Quickly finds a near-optimal tour using probabilistic selection based on distance.

Minimal Tour Algorithm:

Generates all permutations of the cities.
Calculates the total distance for each permutation.
Returns the permutation with the shortest distance.
Tour Approximation Algorithm:

Starts from a given city.
Calculates the total distance to all remaining cities.
Selects the next city based on a probability proportional to the inverse of the distance.
Repeats until all cities are visited.
Returns the complete tour and its total distance.

## Files

4.1.png
A PNG image file, containing a visual representation of a graph or a result relevant to the project.

Ergebnis_13Städte.pdf
A PDF document containing the results or findings of the project for a 13-city Traveling Salesman Problem (TSP).

graph.py
A Python script defining the graph structure and the algorithms used for solving the TSP.

graph.pyc
A compiled Python file, generated automatically from graph.py.

graph_eu_12.xml
An XML file containing graph data, representing a 12-city graph within Europe.

graph_eu_13.xml
An XML file containing graph data, representing a 13-city graph within Europe.

graph_eu_15.xml
An XML file containing graph data, representing a 15-city graph within Europe.

graph_eu_25.xml
An XML file containing graph data, representing a 25-city graph within Europe.

graph_eu_27.xml
An XML file containing graph data, representing a 27-city graph within Europe.

graph_eu_6.xml
An XML file containing graph data, representing a 6-city graph within Europe.

graph_eu_9.xml
An XML file containing graph data, representing a 9-city graph within Europe.

Projekt_TSP.docx
A Word document containing the project report, documentation, or analysis related to the TSP project.

Projekt_TSP.pdf
A PDF version of the project report or documentation related to the TSP project.

Projekt_TSP.py
A Python script, the main script for running the TSP project or containing the core logic for solving the TSP.

test.py
A Python script for testing purposes, containing unit tests or test cases for validating the project's functionality.

test_naeherungsverfahren.py
A Python script for testing approximation methods, containing tests for heuristic or approximation algorithms for the TSP.

.idea/.gitignore
A .gitignore file specific to the IDE (IntelliJ IDEA or PyCharm), listing files and directories to be ignored by version control.

.idea/Geruest Projekt TSP-20240529.iml
An IntelliJ IDEA module file, storing the configuration for the project.

.idea/misc.xml
An IntelliJ IDEA configuration file, containing miscellaneous settings for the project.

.idea/modules.xml
An IntelliJ IDEA configuration file, listing the modules within the project.

.idea/workspace.xml
An IntelliJ IDEA configuration file, storing the workspace settings for the project.

pycache/graph.cpython-310.pyc
A compiled Python file in the __pycache__ directory, generated from graph.py for Python 3.10.


## Documentation

[Documentation German](./Graphen%20Projekt%20TSP/Projekt_TSP.pdf)

