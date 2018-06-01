# import numpy as np
# import sympy as sym
from lagrange_fn import lagrange_fn

x = [0, 1, 2]
y = [3, 5, 1]

f = lagrange_fn(x, y, "fun")
s = lagrange_fn(x, y, "sym")
l = lagrange_fn(x, y, "lat")

print(l)
