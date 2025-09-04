The vector field: $F: R^2 -> R^2$ is given by:

$$F(x, y) = <-3x^2-y, -x+2y>$$

Let $C$ be a differentiable curve from point A(1, 0) to B(-1, 1).

Evaluate the integral:

$$
\int _ C F dr.
$$

## Solution

First see if the vector field is conservative by quickly checking if:

$$\frac{\partial Fx}{\partial y} =? \frac{\partial Fy}{\partial x}$$

This one IS conservative:

$$\frac{\partial Fx}{\partial y} = -1$$
$$\frac{\partial Fy}{\partial x} = -1$$

So this vector field has a scalar potential 

$$F= \nabla U$$

, where 

$$U(𝑥,𝑦) = -x^3 - xy + y^2$$

$$ F = U(-1, 1) - U(1, 0) = 4$$
