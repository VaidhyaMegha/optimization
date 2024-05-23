# Taken from https://drive.google.com/file/d/1ytTQ8oEHN5wAeoXXveOa4SJP6y3qRAXZ/view which is found here : https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under constrained optimization section 

import numpy as np

def Rao_1():
    RUNS = 10  # Number of individual runs
    for _ in range(RUNS):
        pop = 5  # population size
        var = 2  # Number of design variables
        maxFes = 500000  # Maximum functions evaluation
        maxGen = maxFes // pop  # Maximum number of iterations
        mini = np.array([-5, -5])
        maxi = np.array([5, 5])
        x = np.random.rand(pop, var) * (maxi - mini) + mini
        f = objective(x)
        gen = 0
        fopt = []
        while gen < maxGen:
            xnew = update_population(x, f)
            xnew = trimr(mini, maxi, xnew)
            fnew = objective(xnew)
            for i in range(pop):
                if fnew[i] < f[i]:
                    x[i, :] = xnew[i, :]
                    f[i] = fnew[i]
            print('%%%%%% Final population%%%%%%%')
            print(np.hstack((x, f.reshape(-1, 1))))
            gen += 1
            fopt.append(np.min(f))
        runs_fes = pop * (np.argmin(fopt) + 1)
        runs_best = np.min(fopt)

    bbest = np.min(fopt)
    mbest = np.mean(fopt)
    wbest = np.max(fopt)
    stdbest = np.std(fopt)
    mFes = runs_fes

    print(f'\n best={bbest}')
    print(f'\n mean={mbest}')
    print(f'\n worst={wbest}')
    print(f'\n std. dev.={stdbest}')
    print(f'\n mean Fes={mFes}')

def trimr(mini, maxi, x):
    np.clip(x, mini, maxi, out=x)
    return x

def update_population(x, f):
    row, col = x.shape
    best_index = np.argmin(f)
    worst_index = np.argmax(f)
    Best = x[best_index, :]
    worst = x[worst_index, :]
    xnew = np.zeros((row, col))
    for i in range(row):
        for j in range(col):
            xnew[i, j] = x[i, j] + np.random.rand() * (Best[j] - worst[j])
    return xnew

def objective(x):
    r, _ = x.shape
    Z = np.zeros(r)
    for i in range(r):
        x1, x2 = x[i, 0], x[i, 1]
        z = ((x1**2 + x2 - 11)**2) + ((x1 + x2**2 - 7)**2)
        g1 = 26 - ((x1 - 5)**2) - (x2**2)
        g2 = 20 - (4 * x1) - x2
        p1 = 10 * (min(0, g1)**2)  # penalty if constraint 1 is violated
        p2 = 10 * (min(0, g2)**2)  # penalty if constraint 2 is violated
        Z[i] = z + p1 + p2  # penalized objective function value
    return Z

# Run the Rao-1 algorithm
Rao_1()
