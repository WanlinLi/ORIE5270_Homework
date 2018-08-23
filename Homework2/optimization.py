import numpy as np
from scipy.optimize import minimize

class Rosenbrock(object):
    def __init__(self):
        pass

    @staticmethod
    def rosen_func(x):
        """
        :param x: (list) the independent variable
        :return: (Double) the value of the Rosenbrock function at point x
        """
        func = sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)
        return func

    @staticmethod
    def rosen_grad(x):
        """
        :param x: (list) the independent variable
        :return:(list) the gradient of the Rosenbrock function at point x
        """
        grad = [-400 * x[0] * (x[1] - x[0] ** 2) - 2 * (1 - x[0])]
        for i in range(1, len(x) - 1):
            grad.append(200 * (x[i] - x[i - 1] ** 2) - 400 * x[i] * (x[i + 1] - x[i] ** 2) - 2 * (1 - x[i]))
        grad.append(200 * (x[-1] - x[-2] ** 2))
        grad = np.array(grad)
        return grad

if __name__ == "__main__":
    x0 = np.array([1, 3, 5])
    x1 = np.array([3.5, 6.4, 10.9])
    x2 = np.array([-4, 3.7, -10.9])
    x3 = np.array([-6.4, 19, -87])
    initial_point = [x0, x1, x2, x3]
    res = np.inf
    for x in initial_point:
        res_new = minimize(Rosenbrock.rosen_func, x, method='BFGS', jac=Rosenbrock.rosen_grad,
                           options={'gtol': 1e-8, 'disp': True})
        res = min(res, res_new.fun)
    res
