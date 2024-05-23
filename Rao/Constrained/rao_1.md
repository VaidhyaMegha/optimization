# Rao-1 Algorithm for Constrained Optimization

## Overview
The Rao-1 algorithm is a heuristic optimization method used for solving constrained optimization problems. This implementation focuses on the Himmelblau function, a widely used test function for optimization algorithms. The algorithm iteratively improves a population of solutions by navigating the search space towards regions that balance between exploring and exploiting, guided by the best and worst solutions in the population.

## Algorithm Description
The Rao-1 algorithm works as follows:

1. **Initialization**: Generate an initial population of random solutions within the specified bounds.

2. **Evaluation**: Calculate the objective function value for each solution in the population. The objective function used is the Himmelblau function, modified to include penalties for constraint violations.

3. **Main Loop**:
   - For each generation:
     - **Update Population**: Generate a new population by adjusting each current solution towards the best solution and away from the worst solution using a random factor.
     - **Trimming**: Ensure that all solutions remain within the defined bounds.
     - **Selection**: Replace the current solution with the new solution if the new solution has a better (lower) objective function value.
     - Track the best solution found in each generation.

4. **Termination**: The algorithm terminates when the maximum number of generations is reached.

5. **Results**: Print the final solutions and statistics (best, mean, worst, standard deviation, and mean function evaluations).

## Objective Function - Himmelblau Function

The Himmelblau function is defined as:
\[ f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2 \]

Constraints:
1. \[ g_1(x, y) = 26 - (x - 5)^2 - y^2 \]
2. \[ g_2(x, y) = 20 - 4x - y \]

Penalties are added to the function value if these constraints are violated, affecting the search for the minimum.

## Python Implementation

The Python script includes several functions:
- `Rao_1()`: Main function to run the Rao-1 optimization process.
- `objective(x)`: Computes the penalized objective function value.
- `update_population(x, f)`: Generates a new population by perturbing the current population towards the best solution and away from the worst.
- `trimr(mini, maxi, x)`: Ensures all individuals in the population are within the specified bounds.

## Usage
To use this implementation:
1. Ensure Python and NumPy are installed.
2. Run the script to see the algorithm in action. The output will display the progress of the algorithm and the final results.

## Conclusion
This README provides a basic understanding of the Rao-1 algorithm implemented for the Himmelblau function. The implementation demonstrates the method's applicability to constrained optimization problems in Python.
```

### Explanation:
- **Introduction**: Provides an overview of the algorithm and its purpose.
- **Algorithm Description**: Breaks down the algorithm into initialization, main loop, and termination phases.
- **Objective Function**: Details the function being minimized, including constraints and penalties for violation.
- **Python Implementation**: Describes the Python functions corresponding to different steps of the algorithm.
- **Usage**: Instructions on how to run the implementation.
- **Conclusion**: A brief wrap-up about what the README covers.