# Rao-2 Algorithm Implementation

This repository contains a Python implementation of the Rao-2 algorithm, which is used for unconstrained optimization. Specifically, it is applied to solve the Sphere function. The Rao-2 algorithm is a heuristic method that can be used for finding global minima of mathematical functions.

## Algorithm Description

The Rao-2 algorithm is an iterative optimization algorithm that improves a population of solutions. At each iteration, the algorithm updates the population by moving towards the best solution while avoiding the worst, and by exploring the space around the current solutions. The objective of the algorithm is to minimize the Sphere function, which is defined as the sum of the squares of the variables:

```
f(x) = sum(x_i^2 for i in x)
```

## Files in this Repository

- `rao2_algorithm.py`: The main Python script containing the Rao-2 algorithm and all required functions.

## Requirements

This implementation requires Python 3 and the NumPy library. You can install NumPy using pip:

```bash
pip install numpy
```

## Usage

Run the script directly from the command line:

```bash
python rao2_algorithm.py
```

## How It Works

The `rao2_algorithm.py` script initializes a population of solutions randomly. Each solution or point in the population is represented by a vector of design variables. The following steps are repeated until the maximum number of iterations (generations) is reached:

1. **Objective Evaluation**: The Sphere function is evaluated for each solution.
2. **Population Update**: Generate new solutions based on the current ones by using differential movements influenced by the best and worst solutions in the current population.
3. **Trimming**: Adjust new solutions to ensure they remain within specified bounds.
4. **Selection**: If a new solution has a better objective value than the old one, it replaces the old one in the population.

## Output

The script outputs the current iteration number, the state of the population at the end of each iteration, and finally the optimum value found along with the total number of function evaluations.

## Configuration

You can adjust the following parameters in the script to suit your optimization needs:
- `pop`: Population size.
- `var`: Number of design variables.
- `max_fes`: Maximum number of function evaluations.
- Initial range of design variables set by `mini` and `maxi`.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
