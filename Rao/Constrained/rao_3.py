# Taken from https://drive.google.com/file/d/1fDoExAHXNV95vsoRE0892lMKjh4tRhUr/view which is found here : https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under constrained optimization section 

import numpy as np

def objective(x):
    r, c = x.shape
    Z = np.zeros((r, 1))
    for i in range(r):
        x1 = x[i, 0]
        x2 = x[i, 1]
        z = ((x1**2 + x2 - 11)**2) + ((x1 + x2**2 - 7)**2)
        g1 = 26 - ((x1 - 5)**2) - (x2**2)
        g2 = 20 - (4*x1) - x2
        p1 = 10 * (min(0, g1)**2)  # penalty if constraint 1 is violated
        p2 = 10 * (min(0, g2)**2)  # penalty if constraint 2 is violated
        Z[i] = z + p1 + p2  # penalized objective function value
    return Z.flatten()

def trimr(mini, maxi, x):
    x = np.where(x < mini, mini, x)
    x = np.where(x > maxi, maxi, x)
    return x

def updatepopulation(x, f):
    row, col = x.shape
    tindex = np.argmin(f)
    Best = x[tindex, :]
    windex = np.argmax(f)
    worst = x[windex, :]
    xnew = np.zeros_like(x)
    for i in range(row):
        k = np.random.randint(row)
        while k == i:
            k = np.random.randint(row)
        if f[i] < f[k]:
            for j in range(col):
                r = np.random.rand(2)
                xnew[i, j] = x[i, j] + r[0]*(Best[j] - abs(worst[j])) + r[1]*(abs(x[i, j]) - x[k, j])
        else:
            for j in range(col):
                r = np.random.rand(2)
                xnew[i, j] = x[i, j] + r[0]*(Best[j] - abs(worst[j])) + r[1]*(abs(x[k, j]) - x[i, j])
    return xnew

def Rao_3():
    RUNS = 10  # Number of individual runs
    best_results = []
    Fes = []

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
            xnew = updatepopulation(x, f)
            xnew = trimr(mini, maxi, xnew)
            fnew = objective(xnew)
            for i in range(pop):
                if fnew[i] < f[i]:
                    x[i, :] = xnew[i, :]
                    f[i] = fnew[i]
            fopt.append(np.min(f))

        Fes.append(pop * np.argmin(fopt))
        best_results.append(np.min(fopt))

    bbest = np.min(best_results)
    mbest = np.mean(best_results)
    wbest = np.max(best_results)
    stdbest = np.std(best_results)
    mFes = np.mean(Fes)

    print(f'\n best={bbest}')
    print(f'\n mean={mbest}')
    print(f'\n worst={wbest}')
    print(f'\n std. dev.={stdbest}')
    print(f'\n mean Fes={mFes}')

if __name__ == '__main__':
    Rao_3()
