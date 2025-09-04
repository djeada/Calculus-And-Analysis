# What is an integral?

Differentiation is only half of a traditional calculus course. The other pillar—**integration**—begins with the question “What is the area under this curve?” Despite seeming unrelated, integration is tightly linked to differentiation through the fundamental theorem of calculus.

## Geometric interpretation

Let $f(x)$ be a function and, for simplicity, assume $f(x)\ge 0$ on $[a,b]$. We want the area between the graph $y=f(x)$ and the $x$-axis from $x=a$ to $x=b$.

If $f$ can dip below the axis, $\int_a^b f(x)\,dx$ gives **signed area** (area above the axis minus area below). The actual geometric area in that case is $\int_a^b |f(x)|\,dx$.

## Symbol

We denote the (signed) area by

$$
\int_a^b f(x)\,dx.
$$

The symbol $dx$ indicates the variable of integration. It’s a **dummy (bound) variable**, so

$$
\int_a^b f(x)\,dx=\int_a^b f(z)\,dz.
$$

Units check: if $x$ has units of length and $f$ has units of height, then the integral has units of area.

## Approximation

Partition $[a,b]$ into $N$ subintervals: $a=x_0<x_1<\cdots<x_N=b$, with widths $\Delta x_i=x_i-x_{i-1}$. Choose a sample point $x_i^*$ in each subinterval and approximate the area by rectangles:

$$
R_N=\sum_{i=1}^{N} f(x_i^*)\,\Delta x_i.
$$

Left-endpoint, right-endpoint, and midpoint rules correspond to different choices of $x_i^*$. As we refine the partition (make the widest $\Delta x_i$ small), these Riemann sums approach the exact value:

$$
\int_a^b f(x)\,dx=\lim_{\max \Delta x_i\to 0}\sum_{i=1}^{N} f(x_i^*)\,\Delta x_i,
$$

whenever $f$ is integrable (e.g., continuous).

## Link to differentiation (FTC, brief)

Define $F(x)=\int_a^{x} f(t)\,dt$. Then $F'(x)=f(x)$ and

$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

This is what ties “area under the curve” to antiderivatives.
