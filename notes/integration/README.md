## Fundamental Theorem of Calculus

Let $f$ be continuous on $[a,b]$.

1. Define $S(x)=\int_a^{x} f(t)\,dt$. Then $S$ is continuous on $[a,b]$, differentiable on $(a,b)$, and

$$
S'(x)=f(x),\qquad \text{i.e. } \frac{d}{dx}\int_a^{x} f(t)\,dt = f(x).
$$

(Chain-rule version: $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f(g(x))\,g'(x)$.)

2. If $F$ is any antiderivative of $f$ on $[a,b]$ (so $F'=f$), then

$$
\int_a^{b} f(x)\,dx = F(b)-F(a).
$$

## Common antiderivatives and integrals

For a constant $C$:

* Power rule ( $n\neq -1$ ): $\displaystyle \int x^{n}\,dx=\frac{x^{n+1}}{n+1}+C$
* $\displaystyle \int \frac{1}{x}\,dx=\ln|x|+C$
* $\displaystyle \int \frac{1}{ax+b}\,dx=\frac{1}{a}\ln|ax+b|+C$
* $\displaystyle \int e^{ax}\,dx=\frac{1}{a}e^{ax}+C$
* $\displaystyle \int \cos(ax)\,dx=\frac{1}{a}\sin(ax)+C$
* $\displaystyle \int \sin(ax)\,dx=-\frac{1}{a}\cos(ax)+C$
* $\displaystyle \int \sec^{2}x\,dx=\tan x + C$
* Bonus pattern: $\displaystyle \int \frac{f'(x)}{f(x)}\,dx=\ln|f(x)|+C$ (when $f(x)\neq 0$).

## Jak rozumieć podwójną całkę (intuicja)

* $\iint_{D} f(x,y)\,dA$ sumuje wartości $f$ po całym obszarze $D$.
* Jeśli $f(x,y)\ge 0$, to daje „objętość” pod powierzchnią $z=f(x,y)$ nad $D$.
* Szczególny przypadek: $\iint_{D} 1\,dA = \text{pole}(D)$.

(Praktycznie: często liczymy jako całkowanie iterowane, np. $\int_{x=a}^{b}\int_{y=g_1(x)}^{g_2(x)} f(x,y)\,dy\,dx$.)
