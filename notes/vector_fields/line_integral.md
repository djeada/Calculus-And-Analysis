The vector field F: R^2 -> R^2 is given by:

$$F(x,y) = <-3x^2-y,-x+2y>$$

Let C be a differentiable curve from point A(1,0) to point B(-1,1).

Evaluate the line integral:

$$\int_{C}Fdr$$

Answer = 4.

When doing a line integral, first see if the vector field is conservative by quickly checking if 

$$\frac{\partial Fx}{\partial y} = \frac{\partial Fy}{\partial x}$$

This one IS conservative (both partial derivatives are -1). So this vector field has a scalar potential:

$$F= \nabla U \quad where U(x,y) = -x^3 -xy + y^2$$

$$\int_{C}Fdr = U(-1, 1) - U(1, 0)$$
