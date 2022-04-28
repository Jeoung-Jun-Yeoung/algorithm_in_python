import numpy as np


def func1(w):
    x = w
    return x**2


def numerical_derivative(f, x):
    delta_x = 1e-4
    grand = np.zeros_like(x)

    it = np.nditer(x, flag=['multi_index'], op_flag=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        temp_val = x[idx]

        x[idx] = float(temp_val) + delta_x
        fx1 = f(x)

        x[idx] = temp_val - delta_x
        fx2 = f(x)

        grand[idx] = fx1 - fx2 / (2*delta_x)
        x[idx] = temp_val
        it.iternext()
    return grand


def f(w): return func1(w)


w = np.array([3.0])

ret = numerical_derivative(f, w)

print('type(ret) = ', type(ret), ', ret_val = ', ret)
