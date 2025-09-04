## Limit vs. value at a point

The limit $\lim_{x\to x_0} f(x)$ describes how $f$ behaves near $x_0$; it does not depend on $f(x_0)$.

Example:

$$
f(x)=\begin{cases}
0,& x\ne 0\\
1,& x=0
\end{cases}
\quad\Rightarrow\quad
f(0)=1,\ \ \lim_{x\to 0}f(x)=0.
$$

A function is continuous at $x_0$ iff $\lim_{x\to x_0} f(x)=f(x_0)$. Common continuous building blocks: polynomials, trig, exponential, logarithmic functions and their compositions (on domains where they’re defined). Be careful at points where a formula isn’t defined (e.g. denominator $=0$); the limit may still exist (removable discontinuity) even if the value doesn’t.

Indeterminate forms like $0/0$ or $\infty/\infty$ are where continuity isn’t obvious and real limit work begins.

## Precise definition (ε–δ)

Let $f$ be defined on an open interval around $x_0$ (possibly excluding $x_0$). We say $\lim_{x\to x_0} f(x)=L$ if for every $\varepsilon>0$ there exists $\delta>0$ such that

$$
0<|x-x_0|<\delta\ \Longrightarrow\ |f(x)-L|<\varepsilon.
$$

Equivalent (sequential) view: for every sequence $x_n\to x_0$ with $x_n\ne x_0$, we have $f(x_n)\to L$.

## Common limits

For fixed real constants $k,m$ and $a>0$:

$$
\lim_{x\to\infty}\Bigl(1+\tfrac{k}{x}\Bigr)^{mx}=e^{mk},\qquad
\lim_{x\to\infty}\Bigl(1+\tfrac{1}{x}\Bigr)^{x}=e,\qquad
\lim_{x\to\infty}\Bigl(1-\tfrac{1}{x}\Bigr)^{x}=e^{-1}.
$$

$$
\lim_{x\to\infty}\Bigl(\tfrac{x}{x+k}\Bigr)^{x}=e^{-k},\qquad
\lim_{x\to 0}(1+x)^{1/x}=e.
$$

$$
\lim_{x\to 0}\frac{a^{x}-1}{x}=\ln a,\quad
\lim_{x\to 0}\frac{e^{x}-1}{x}=1,\quad
\lim_{x\to 0}\frac{\ln(1+x)}{x}=1.
$$

$$
\lim_{x\to 0}\frac{\sin x}{x}=1,\quad
\lim_{x\to 0}\frac{\sin(ax)}{bx}=\frac{a}{b},\quad
\lim_{x\to 0}\frac{1-\cos x}{x}=0,\ \ \text{and}\ \ \lim_{x\to 0}\frac{1-\cos x}{x^{2}}=\tfrac12.
$$

## L’Hôpital’s Rule (safe statement)

Let $f,g$ be differentiable on an open interval $I$ containing $a$ (possibly excluding $a$). Assume $g'(x)\ne 0$ on $I\setminus\{a\}$. If

* $\lim_{x\to a} f(x)=\lim_{x\to a} g(x)=0$ or both are $\pm\infty$ (an indeterminate form), and
* $\displaystyle \lim_{x\to a}\frac{f'(x)}{g'(x)}$ exists (finite or $\pm\infty$),

then

$$
\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}.
$$

The rule also holds for one-sided limits and $a=\pm\infty$.

When to use/avoid:

* Use only for $0/0$ or $\infty/\infty$. Convert other forms (e.g. $0\cdot\infty$, $1^{\infty}$, $0^{0}$, $\infty-\infty$) into these first (algebra, logs).
* Often simpler: factor/cancel, rationalize with a conjugate, use series/small-angle approximations, or the squeeze theorem.
