# Taken from https://drive.google.com/file/d/1HUaqFo7x05J-zybPgpaiMTYK0TcMOwr-/view which is found here : https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under unconstrained optimization section 

import numpy as np

def rao1():
    pop = 10  # Population size
    var = 30  # Number of design variables
    max_fes = 30000  # Maximum functions evaluation
    max_gen = max_fes // pop  # Maximum number of iterations

    mini = -100 * np.ones(var)
    maxi = 100 * np.ones(var)

    x = np.zeros((pop, var))
    for i in range(var):
        x[:, i] = mini[i] + (maxi[i] - mini[i]) * np.random.rand(pop)

    f = objective(x)
    gen = 1

    while gen <= max_gen:
        xnew = update_population(x, f)
        xnew = trimr(mini, maxi, xnew)
        fnew = objective(xnew)

        for i in range(pop):
            if fnew[i] < f[i]:
                x[i, :] = xnew[i, :]
                f[i] = fnew[i]

        print(f'Iteration No. = {gen}')
        print('%%%%%%%% Final population %%%%%%%%%')
        print(np.hstack((x, f.reshape(-1, 1))))

        fnew = []
        xnew = []
        fopt = np.min(f)
        ind = np.argmin(f)
        xopt = x[ind, :]

        gen += 1

    val = np.min(fopt)
    ind = np.argmin(fopt)
    fes = pop * ind

    print(f'Optimum value = {val:.10f}')

def objective(x):
    r, c = x.shape
    f = np.zeros(r)
    for i in range(r):
        y = 0
        for j in range(c):
            y += x[i, j] ** 2  # Sphere function
        f[i] = y
    return f

def update_population(x, f):
    row, col = x.shape
    tindex = np.argmin(f)
    best = x[tindex, :]
    windex = np.argmax(f)
    worst = x[windex, :]

    xnew = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            xnew[i, j] = x[i, j] + np.random.rand() * (best[j] - worst[j])
    return xnew

def trimr(mini, maxi, x):
    x = np.maximum(x, mini)
    x = np.minimum(x, maxi)
    return x

# Run the Rao-1 algorithm
rao1()
