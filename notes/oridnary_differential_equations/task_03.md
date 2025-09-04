Show that the transformation $x=e^u$ transforms the differential equation:

$$x^2 \frac{d^2y}{dx^2} + 3x\frac{dy}{dx} -8y = 4lnx \quad for \quad x>0$$

into the differentail equation:

$$\frac{d^2y}{du^2} + 2 \frac{dy}{du}-8y =4u$$

Solution:

Let $u=\ln x$ so $x=e^{u}$, $x>0$. Then

$$
u_x=\frac{du}{dx}=\frac1x=e^{-u},\qquad
y_x=y_u\,u_x=e^{-u}y_u.
$$

For the second derivative, use the chain rule:

$$
y_{xx}=y_{uu}(u_x)^2+y_u\,u_{xx}.
$$

Since $u_{xx}=d(e^{-u})/dx=-e^{-u}u_x=-e^{-2u}$, we get

$$
y_{xx}=y_{uu}e^{-2u}-y_u e^{-2u}=e^{-2u}(y_{uu}-y_u).
$$

Substitute into $x^2y_{xx}+3xy_x-8y=4\ln x$ with $x=e^{u}$ and $\ln x=u$:

$$
e^{2u}\,e^{-2u}(y_{uu}-y_u)+3e^{u}\,e^{-u}y_u-8y=4u
$$

$$
\Rightarrow\quad y_{uu}+2y_u-8y=4u,
$$

as required.

Shortcut: note $ \dfrac{d}{du}=x\dfrac{d}{dx}$. Then

$$
\frac{d^2}{du^2}=x\frac{d}{dx}\!\left(x\frac{d}{dx}\right)
= x\frac{d}{dx}+x^{2}\frac{d^{2}}{dx^{2}},
$$

so $x^{2}y_{xx}=y_{uu}-y_u$ and $xy_x=y_u$. Plugging in immediately yields $y_{uu}+2y_u-8y=4u$.
