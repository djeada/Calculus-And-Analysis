$$\lim_{x \to \infty} (\frac{2x^2+3}{2x^2+7})^{x^2+2021}$$

Rewrite the base:

$$
\frac{2x^2+3}{2x^2+7}=1-\frac{4}{2x^2+7}.
$$

Set $t_x=-\dfrac{4}{2x^2+7}$. Then $t_x\to 0$ and

$$
\Bigl(1+t_x\Bigr)^{x^2+2021}
=\Bigl((1+t_x)^{1/t_x}\Bigr)^{\,t_x(x^2+2021)}.
$$

As $x\to\infty$, $(1+t_x)^{1/t_x}\to e$ and

$$
t_x(x^2+2021)= -\frac{4(x^2+2021)}{2x^2+7}\longrightarrow -2.
$$

Therefore the limit is $e^{-2}$. (Same result via $\ln$: $(x^2+2021)\ln(1-4/(2x^2+7))\to -2$.)
