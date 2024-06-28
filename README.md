
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
## Documentation

[Documentation German](./Graphen%20Projekt%20TSP/Projekt_TSP.pdf)

