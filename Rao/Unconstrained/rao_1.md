# Rao-1 Algorithm for Sphere Function Optimization

This repository contains the implementation of the Rao-1 algorithm for solving the Sphere function optimization problem. The Rao-1 algorithm is a simple and efficient optimization algorithm designed to solve unconstrained optimization problems.

## Algorithm Overview

The Rao-1 algorithm works by iteratively updating a population of candidate solutions to find the minimum value of the objective function. In this case, the objective function is the Sphere function, which is defined as the sum of the squares of the design variables.

### Key Steps of the Algorithm

1. **Initialization**:
    - Initialize a population of candidate solutions randomly within the specified bounds.
    - Evaluate the objective function for each candidate solution.

2. **Iteration**:
    - Update the population by moving each candidate solution towards the best solution found so far and away from the worst solution.
    - Ensure that the updated solutions remain within the specified bounds.
    - Evaluate the objective function for the updated population.
    - Replace the old solutions with the new solutions if the new solutions are better.

3. **Termination**:
    - The algorithm terminates when the maximum number of iterations is reached.
    - The best solution found during the iterations is reported as the optimal solution.

## Running the Code

### Prerequisites

- Python 3.x
- NumPy library

You can install NumPy using pip if you don't have it installed:

```sh
pip install numpy
```

### Execution

To run the Rao-1 algorithm, simply execute the `rao1.py` file:

```sh
python rao1.py
```

### Code Structure

- `rao1()`: Main function that runs the Rao-1 algorithm.
- `objective(x)`: Computes the Sphere function value for a given population `x`.
- `update_population(x, f)`: Updates the population by moving solutions towards the best and away from the worst.
- `trimr(mini, maxi, x)`: Ensures that the solutions remain within the specified bounds.

### Output

The algorithm prints the following information during execution:
- The iteration number.
- The final population and their objective function values for each iteration.
- The optimal value of the objective function found by the algorithm.

### Example Output

```sh
Iteration No. = 1
%%%%%%%% Final population %%%%%%%%%
[[ 58.22694507  76.28982221 ...  46.97280949  274519.7680473 ]
 [ 18.6972442   34.80385639 ...  10.27201392  145403.61321863]
 ...
 [ 53.28496888 -82.78718389 ...  28.63476158  259212.33612718]]
Optimum value = 145403.6132
```

## Contact

For any questions or suggestions, please feel free to contact the repository owner.
