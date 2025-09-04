## Rules for computing integrals

As in differential calculus, we have parallel rules:

* Linearity (sum rule): $\int (\alpha f+\beta g)=\alpha\!\int f+\beta\!\int g$.
* Change of variables (chain rule analogue).
* Integration by parts (product rule analogue).

## Change of variables

**Definite form.** If $g$ is differentiable on $[a,b]$ and $f$ is integrable on the range of $g$, then

$$
\int_a^b f(g(x))\,g'(x)\,dx=\int_{g(a)}^{g(b)} f(u)\,du.
$$

This automatically handles the sign/orientation: if $g$ is decreasing then $g(a)>g(b)$ and the limits reflect that.

**Indefinite form.** With $u=g(x)$ and $du=g'(x)\,dx$,

$$
\int f(g(x))\,g'(x)\,dx=\int f(u)\,du + C.
$$

## Derivation

Let $F(x)=\displaystyle\int_0^{x} f(t)\,dt$. Then $F'(x)=f(x)$ (FTC). For a differentiable $g$,

$$
\frac{d}{dx}F(g(x))=F'(g(x))\,g'(x)=f(g(x))\,g'(x).
$$

Integrate both sides from $0$ to $x$:

$$
F(g(x))-F(g(0))=\int_{0}^{x} f(g(y))\,g'(y)\,dy.
$$

Since $F(g(x))=\displaystyle\int_{0}^{g(x)} f(u)\,du$, we get

$$
\int_{g(0)}^{g(x)} f(u)\,du=\int_{0}^{x} f(g(y))\,g'(y)\,dy,
$$

which is the change-of-variables formula (rename dummy variables as desired).

## Example

Take $f(u)=1$ and $g(y)=e^{-y^{2}}$. Then $g'(y)=-2y\,e^{-y^{2}}$. For $x=1$,

$$
\int_{g(0)}^{g(1)} 1\,du=\int_{0}^{1} 1\cdot(-2y e^{-y^{2}})\,dy
$$

$$
e^{-1}-1=-2\int_{0}^{1} y e^{-y^{2}}\,dy
$$

$$
\int_{0}^{1} y e^{-y^{2}}\,dy=\frac{1-e^{-1}}{2}.
$$

(As a check, the standard substitution $u=y^{2}$ gives the same result.)
