#!/usr/bin/env python3
"""SymPy example: definite and indefinite integrals."""
import sympy as sp

x = sp.symbols('x')
expr = sp.exp(-x**2)
indef = sp.integrate(expr, x)
defi = sp.integrate(expr, (x, 0, sp.oo))
print('Indefinite integral:', sp.pretty(indef))
print('Definite integral 0..inf:', defi)
