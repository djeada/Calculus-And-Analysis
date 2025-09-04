
Divide top and bottom by $x$:

$$
\frac{x+\sqrt{x+3}}{2x-1}
=\frac{1+\dfrac{\sqrt{x+3}}{x}}{\,2-\dfrac{1}{x}\,}.
$$

Now

$$
\frac{\sqrt{x+3}}{x}
=\frac{1}{\sqrt{x}}\sqrt{1+\frac{3}{x}}
\longrightarrow 0\cdot 1=0,
\qquad
2-\frac{1}{x}\longrightarrow 2\neq 0,
$$

so by limit laws,

$$
\lim_{x\to\infty}\frac{x+\sqrt{x+3}}{2x-1}
=\frac{1+0}{2-0}=\frac12.
$$

Quick bound (epsilon-check). Subtract $\tfrac12$:

$$
\frac{x+\sqrt{x+3}}{2x-1}-\frac12
=\frac{2\sqrt{x+3}+1}{4x-2}.
$$

For $x\ge 1$: $2\sqrt{x+3}+1\le 3\sqrt{4x}=6\sqrt{x}$, hence

$$
0\le \frac{2\sqrt{x+3}+1}{4x-2}
\le \frac{6\sqrt{x}}{4x-2}
\le \frac{6}{4\sqrt{x}} \xrightarrow[x\to\infty]{} 0,
$$

confirming the limit is $1/2$.
