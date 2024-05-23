# Taken from https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under constrained optimization section 

import numpy as np

def rao_2():
    RUNS = 10  # Number of individual runs
    results = []
    for _ in range(RUNS):
        pop = 10  # population size
        var = 2  # Number of design variables
        maxFes = 500000  # Maximum functions evaluation
        maxGen = maxFes // pop  # Maximum number of iterations
        mini = np.array([-5, -5])
        maxi = np.array([5, 5])
        x = np.random.rand(pop, var) * (maxi - mini) + mini
        f = objective(x)
        fopt = []
        
        for gen in range(maxGen):
            xnew = update_population(x, f)
            xnew = trimr(mini, maxi, xnew)
            fnew = objective(xnew)
            improve = fnew < f
            x[improve] = xnew[improve]
            f[improve] = fnew[improve]
            fopt.append(f.min())
        
        val = min(fopt)
        ind = np.argmin(fopt)
        Fes = pop * (ind + 1)
        results.append((val, Fes))
    
    best_vals, fes_vals = zip(*results)
    bbest = min(best_vals)
    mbest = np.mean(best_vals)
    wbest = max(best_vals)
    stdbest = np.std(best_vals)
    mFes = np.mean(fes_vals)
    
    print(f'\n best={bbest}')
    print(f'\n mean={mbest}')
    print(f'\n worst={wbest}')
    print(f'\n std. dev.={stdbest}')
    print(f'\n mean Fes={mFes}')

def trimr(mini, maxi, x):
    return np.clip(x, mini, maxi)

def update_population(x, f):
    row, col = x.shape
    tindex = np.argmin(f)
    windex = np.argmax(f)
    Best = x[tindex]
    worst = x[windex]
    xnew = np.zeros_like(x)
    
    for i in range(row):
        k = np.random.randint(row)
        while k == i:
            k = np.random.randint(row)
        r = np.random.rand(2)
        if f[i] < f[k]:
            xnew[i] = x[i] + r[0] * (Best - worst) + r[1] * (np.abs(x[i]) - np.abs(x[k]))
        else:
            xnew[i] = x[i] + r[0] * (Best - worst) + r[1] * (np.abs(x[k]) - np.abs(x[i]))
    return xnew

def objective(x):
    x1, x2 = x[:, 0], x[:, 1]
    z = (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
    g1 = 26 - (x1 - 5)**2 - x2**2
    g2 = 20 - 4 * x1 - x2
    p1 = 10 * np.minimum(0, g1)**2
    p2 = 10 * np.minimum(0, g2)**2
    f = z + p1 + p2
    return f

# Run the algorithm
rao_2()

