#!/usr/bin/env python3
"""SymPy example: symbolic derivative and LaTeX output."""
import sympy as sp

x = sp.symbols('x')
expr = sp.sin(x)**2 * sp.exp(x)
d = sp.diff(expr, x)
print('Expression:', sp.pretty(expr))
print('Derivative:', sp.pretty(d))
print('\nLaTeX:\n', sp.latex(d))
