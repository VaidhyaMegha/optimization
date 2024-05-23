# Taken from https://drive.google.com/file/d/1bU4NHz0LXf6CepQKa7S6P8sIw1QlTeCG/view which is found here : https://sites.google.com/view/raoalgorithms/algorithm-codes 
# under unconstrained optimization section 


import numpy as np

def objective(x):
    # Sphere function
    return np.sum(x**2, axis=1)

def update_population(x, f):
    row, col = x.shape
    tindex = np.argmin(f)
    windex = np.argmax(f)
    best = x[tindex, :]
    worst = x[windex, :]
    xnew = np.zeros_like(x)
    for i in range(row):
        k = np.random.randint(row)
        while k == i:
            k = np.random.randint(row)
        r = np.random.rand(2)
        if f[i] < f[k]:
            xnew[i, :] = x[i, :] + r[0] * (best - np.abs(worst)) + r[1] * (np.abs(x[i, :]) - x[k, :])
        else:
            xnew[i, :] = x[i, :] + r[0] * (best - np.abs(worst)) + r[1] * (np.abs(x[k, :]) - x[i, :])
    return xnew

def trimr(mini, maxi, x):
    return np.clip(x, mini, maxi)

def rao_3():
    pop = 10  # Population size
    var = 30  # Number of design variables
    maxFes = 30000  # Maximum function evaluations
    maxGen = maxFes // pop  # Maximum number of generations
    mini = -100 * np.ones(var)
    maxi = 100 * np.ones(var)
    x = np.random.uniform(mini, maxi, (pop, var))
    f = objective(x)
    
    for gen in range(1, maxGen + 1):
        xnew = update_population(x, f)
        xnew = trimr(mini, maxi, xnew)
        fnew = objective(xnew)
        improvement = fnew < f
        x[improvement, :] = xnew[improvement, :]
        f[improvement] = fnew[improvement]
        
        print(f'Iteration No. = {gen}')
        print('%%%%%%% Final population %%%%%%%%')
        print(np.hstack((x, f.reshape(-1, 1))))
        
        if gen == maxGen:
            val = np.min(f)
            ind = np.argmin(f)
            Fes = pop * (ind + 1)
            print(f'Optimum value = {val:.10f}')

if __name__ == '__main__':
    rao_3()
