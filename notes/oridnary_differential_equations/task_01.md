
Linear ODE: $y'+2xy=4x^3$.
Integrating factor: $\mu(x)=e^{\int 2x\,dx}=e^{x^2}$.

Multiply through:

$$
e^{x^2}y'+2x e^{x^2}y=\frac{d}{dx}\!\big(e^{x^2}y\big)=4x^3 e^{x^2}.
$$

Integrate (let $t=x^2$, $dt=2x\,dx$):

$$
e^{x^2}y=\int 4x^3 e^{x^2}\,dx
=2\int t e^{t}\,dt
=2(t-1)e^{t}+C
=2(x^2-1)e^{x^2}+C.
$$

Divide by $e^{x^2}$:

$$
\boxed{\,y(x)=2(x^2-1)+C e^{-x^2}\,}.
$$

Quick check: $y'=4x-2Cx e^{-x^2}$; then $y'+2xy=4x-2Cx e^{-x^2}+2x\big(2(x^2-1)+C e^{-x^2}\big)=4x^3$. ✔️
