# Taken from https://drive.google.com/file/d/1gl4_QCckSizubPaaylLVjWYkLFLuE8k8/view which is found here : https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under unconstrained optimization section 

import numpy as np

def objective(x):
    return np.sum(x**2, axis=1)

def update_population(x, f):
    row, col = x.shape
    best_index = np.argmin(f)
    worst_index = np.argmax(f)
    best = x[best_index]
    worst = x[worst_index]
    x_new = np.zeros((row, col))
    for i in range(row):
        k = np.random.randint(row)
        while k == i:
            k = np.random.randint(row)
        r = np.random.rand(2)
        if f[i] < f[k]:
            x_new[i] = x[i] + r[0] * (best - worst) + r[1] * (np.abs(x[i]) - np.abs(x[k]))
        else:
            x_new[i] = x[i] + r[0] * (best - worst) + r[1] * (np.abs(x[k]) - np.abs(x[i]))
    return x_new

def trimr(mini, maxi, x):
    return np.clip(x, mini, maxi)

def rao_2():
    pop = 10  # Population size
    var = 30  # Number of design variables
    max_fes = 30000  # Maximum functions evaluation
    max_gen = max_fes // pop  # Maximum number of iterations
    mini = -100 * np.ones(var)
    maxi = 100 * np.ones(var)
    x = np.random.uniform(mini, maxi, (pop, var))
    f = objective(x)
    gen = 1
    f_opt = np.zeros(max_gen)
    x_opt = np.zeros((max_gen, var))

    while gen <= max_gen:
        x_new = update_population(x, f)
        x_new = trimr(mini, maxi, x_new)
        f_new = objective(x_new)
        improved = f_new < f
        x[improved] = x_new[improved]
        f[improved] = f_new[improved]
        print(f"Iteration No. = {gen}")
        print("%%%% Final population %%%%%")
        print(np.hstack((x, f.reshape(-1, 1))))
        f_opt[gen - 1], ind = np.min(f), np.argmin(f)
        x_opt[gen - 1] = x[ind]
        gen += 1

    val, ind = np.min(f_opt), np.argmin(f_opt)
    fes = pop * (ind + 1)
    print(f"Optimum value = {val:.10f}")
    print(f"Function Evaluations = {fes}")

if __name__ == "__main__":
    rao_2()
