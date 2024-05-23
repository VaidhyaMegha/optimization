# Rao-3 Algorithm with Constrained Himmelblau Function

## Overview

This repository contains the implementation of the Rao-3 algorithm, which is used for constrained optimization. The Rao-3 algorithm is demonstrated here using the Himmelblau function, a well-known test case for optimization algorithms. The Himmelblau function has been modified to include constraints to demonstrate the algorithm's ability to handle constrained optimization problems.

## Himmelblau Function

The Himmelblau function is a multi-modal function, used to test the performance of optimization algorithms. It is defined as follows:

\[ f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2 \]

In this implementation, we introduce two constraints:

- \( g1: 26 - (x-5)^2 - y^2 \geq 0 \)
- \( g2: 20 - 4x - y \geq 0 \)

Penalties are added to the function's value if these constraints are violated, influencing the optimization process to favor solutions that adhere to the constraints.

## Rao-3 Algorithm

The Rao-3 algorithm is an optimization method that iteratively updates a population of candidate solutions. It is specifically designed to handle complex optimization problems, including those with constraints. The algorithm operates as follows:

1. **Initialization**: Generate a random population of candidate solutions within the specified bounds.
2. **Evaluation**: Compute the fitness of each candidate using the objective function, which includes penalties for any constraint violations.
3. **Update**: For each candidate in the population, generate a new candidate by considering the best and worst solutions in the current population, along with another randomly selected candidate.
4. **Selection**: Replace the old candidate with the new one if the new candidate has a better fitness.
5. **Termination**: Repeat the evaluation-update-selection steps until a maximum number of generations or function evaluations is reached.

## File Structure

- `rao3_algorithm.py`: Contains the full implementation of the Rao-3 algorithm along with the constrained Himmelblau function.
- `README.md`: This file, describing the project and algorithm.

## Usage

To run the Rao-3 algorithm with the Himmelblau function, simply execute the Python script:

```bash
python rao3_algorithm.py
```

Ensure you have Python and NumPy installed on your system.

## Results

Upon running the script, the algorithm will output the best, mean, worst, and standard deviation of the function's value across multiple runs, along with the average number of function evaluations needed to reach these values.

## Dependencies

- Python 3.x
- NumPy
