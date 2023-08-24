import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

def mesh_function(f, t):
    mesh = np.zeros_like(t)
    for i, element in enumerate(t): # Unsure why we loop instead of vectorizing
        mesh[i] = f(element)

    return mesh

def func(t):
    if 0 <= t <= 3:
        func_val = np.exp(-t)
    if 3 < t <= 4:
        func_val = np.exp(-3 * t)


    return func_val

def test_mesh_function():
    t = np.array([1, 2, 3, 4], dtype=float)
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)


if __name__ == "__main__":
    test_mesh_function()
    t = np.linspace(0,  4, 25)
    plt.plot(t, mesh_function(func, t))
    plt.title("Excersise 1.1")
    plt.ylabel("Function value")
    plt.xlabel("Time [t]")
    plt.show()
