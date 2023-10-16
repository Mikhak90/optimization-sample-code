import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0] * x[1]


def constraint1(x):
    return -1 * x[0] * x[1] + 40

def constraint2(x):
    return x[0] * x[1] - 25

x0 = np.array([2,3])

print('Initial objective function value:'+str(objective(x0)))

b = (0,7)
bnds = (b,b)
con1 = {'type':'ineq','fun':constraint1}
con2 = {'type':'ineq','fun':constraint2}
cons=([con1,con2])

solution = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)

x=solution.x

print('final objective function value:'+str(objective(x)))

print('Optimized output results: ')
print('x1='+str(x[0]))
print('x2='+str(x[1]))
