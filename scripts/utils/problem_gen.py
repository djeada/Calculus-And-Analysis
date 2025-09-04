#!/usr/bin/env python3
"""Simple problem generator: create random derivative problems and solutions."""
import random
import sympy as sp

x = sp.symbols('x')
funcs = [sp.sin(x), sp.cos(x), sp.exp(x), x**2, sp.log(x)]


def random_problem():
    f = random.choice(funcs)
    k = random.randint(1, 3)
    expr = f * x**k
    sol = sp.diff(expr, x)
    return expr, sol


if __name__ == '__main__':
    for i in range(5):
        expr, sol = random_problem()
        print(f'Problem {i+1}: d/dx {sp.pretty(expr)}')
        print('Solution:', sp.pretty(sol))
        print()
