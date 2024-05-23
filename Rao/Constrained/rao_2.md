# Rao-2 Algorithm Implementation

This repository contains a Python implementation of the Rao-2 algorithm, applied to the Himmelblau function with constraints. The Rao-2 algorithm is a stochastic, population-based optimization method used to find the minima of functions.

## Overview

The Rao-2 algorithm is an iterative method that improves a population of candidate solutions with respect to a given objective function. In this implementation, the objective function is the Himmelblau function, modified to include constraints.

### Himmelblau Function

The Himmelblau function is a multi-modal function used to test the performance of optimization algorithms. It is defined as:

\[ z = (x^2 + y - 11)^2 + (x + y^2 - 7)^2 \]

### Constraints

Two constraints are added to the function:

1. \( g1: 26 - (x - 5)^2 - y^2 \geq 0 \)
2. \( g2: 20 - 4x - y \geq 0 \)

Penalties are applied if these constraints are violated, affecting the function's value.

## Implementation Details

The Python script `rao2_algorithm.py` includes the following functions:

- `rao_2()`: The main function that initializes the population and performs the optimization process over a defined number of runs.
- `objective(x)`: Computes the penalized objective function value for each candidate in the population.
- `update_population(x, f)`: Generates a new population based on the current population, the best and the worst candidate solutions.
- `trimr(mini, maxi, x)`: Ensures that the new population respects the variable bounds.

### Algorithm Steps

1. **Initialization**: Generate an initial population randomly within the specified bounds.
2. **Evaluation**: Calculate the objective function for each candidate in the population.
3. **Main Loop**:
   - Update the population using the Rao-2 strategy.
   - Enforce the variable constraints.
   - Evaluate the new population.
   - Update the best solutions found so far.
   - Repeat until the maximum number of generations or function evaluations is reached.
4. **Results**: Output the best solution found across all runs.

## Usage

To run the algorithm, simply execute the script. Modify the `RUNS`, `pop`, and other parameters as necessary to suit different optimization needs or constraints.

## Dependencies

The script requires Python 3 and NumPy. Install NumPy using pip:

```bash
pip install numpy
```

## Conclusion

This implementation showcases how the Rao-2 algorithm can be applied to a complex optimization problem with constraints. By adjusting parameters and refining the objective function, the algorithm's efficacy and efficiency in finding optimal solutions can be further explored.

