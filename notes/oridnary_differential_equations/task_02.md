Problem. Solve the differential equation

$$
\frac{dy}{dx}=\frac{3y}{x-2}\qquad (x\ne 2),
$$

and describe the domain of solutions. If an initial value $y(x_0)=y_0$ with $x_0\ne 2$ is given, express the particular solution.

Solution (separation of variables).
Separate and integrate:

$$
\frac{1}{y}\,dy=\frac{3}{x-2}\,dx
\quad\Longrightarrow\quad
\ln|y|=3\ln|x-2|+C.
$$

Exponentiate and absorb constants:

$$
|y|=e^{C}|x-2|^{3}\ \Longrightarrow\ y=C\,(x-2)^3,\qquad C\in\mathbb{R}.
$$

This family includes the constant solution $y\equiv 0$ (take $C=0$).

Check:

$$
y'=3C(x-2)^2=\frac{3C(x-2)^3}{x-2}=\frac{3y}{x-2}.
$$

Domain and behavior.
The equation is singular at $x=2$, so nontrivial solutions are defined on intervals that do not cross $x=2$: either $(-\infty,2)$ or $(2,\infty)$. Solutions cannot be extended through $x=2$.

Initial value.
Given $y(x_0)=y_0$ with $x_0\ne 2$,

$$
C=\frac{y_0}{(x_0-2)^3},\qquad
y(x)=\frac{y_0}{(x_0-2)^3}\,(x-2)^3,
$$

valid on the side of $x=2$ containing $x_0$.

(Alternate linear-ODE route: $y'-\tfrac{3}{x-2}y=0$ with integrating factor $\mu=(x-2)^{-3}$ gives $(\mu y)'=0\Rightarrow y=C(x-2)^3$ as above.)
