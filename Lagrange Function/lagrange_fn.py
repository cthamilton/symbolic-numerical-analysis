# %%
import numpy as np
import sympy as sym

# %%

def lagrange_fn(x_array, y_array, out_type):
    # Inputs-
    # x_array: evaluation points
    # y_array: function values at evaluation points
    #          (associated with the evaluation points of the same index)
    # out_type: 3 options - "fun" returns a function, "sym" returns symbolic
    # math object, "lat" returns latex code for the function

    # for consistency ensure arrays are numpy arrays
    x_array = np.asarray(x_array)
    x_array = np.asarray(x_array)

    # catch easy error
    if len(x_array) != len(y_array):
        raise ValueError('arrays not same length')

    # find length of array
    n = len(x_array)
    # create x
    x = sym.symbols('x')
    # create var
    expr = 0

    for i in range(n):
        # reset term
        term = 1
        for j in range(n):
            if i != j:
                # Add factor
                term = term * ((x - x_array[j]) / (x_array[i] - x_array[j]))

        # addend new term with forrect function value
        expr = expr + y_array[i] * term

    # simplify expression (effect will probably depend on terms)
    # Presumably will convert to the monomial basis(if you aren't a fan you
    # can comment this out)
    expr = sym.simplify(expr)

    # Function case
    if out_type == "fun":
        fun_out = sym.lambdify(x, expr)

    # symbolic math object case
    if out_type == "sym":
        fun_out = expr

    # Latex code case
    if out_type == "lat":
        fun_out = sym.latex(expr)

    return fun_out

    raise ValueError('bad type (need to set out_type as fun, sym, or lat)')
