
In some cases, we will need to work in higher dimensions.  For instance, suppose that we have a function of two variables, like $f(x, y)$ and we want to know the volume under $f$ when $x$ ranges over $[a, b]$ and $y$ ranges over $[c, d]$.

We write this as

$$
\int_{[a, b]\times[c, d]} f(x, y)dxdy.
$$

Suppose that we wish to compute this integral.  My claim is that we can do this by iteratively computing first the integral in $x$ and then shifting to the integral in $y$, that is to say

$$
\int_{[a, b]\times[c, d]} f(x, y)dxdy = \int_c^{d} \left(\int_a^{b} f(x, y) dx\right)  dy.
$$

Let's see why this is.

Consider the figure above where we have split the function into $\epsilon \times \epsilon$ squares which we will index with integer coordinates $i, j$.  In this case, our integral is approximately

$$
\sum_{i, j} \epsilon^{2} f(\epsilon i, \epsilon j).
$$

Once we discretize the problem, we may add up the values on these squares in whatever order we like, and not worry about changing the values. In particular, we can say that

$$
 \sum _ {j} \epsilon \left(\sum_{i} \epsilon f(\epsilon i, \epsilon j)\right).
$$

The sum on the inside is precisely the discretization of the integral

$$
G(\epsilon j) = \int _a^{b} f(x, \epsilon j)  dx.
$$

Finally, notice that if we combine these two expressions we get

$$
\sum _ {j} \epsilon G(\epsilon j) \approx \int _ {c}^{d} G(y)  dy = \int _ {[a, b]\times[c, d]} f(x, y)dxdy.
$$

Thus putting it all together, we have that

$$
\int _ {[a, b]\times[c, d]} f(x, y)dxdy = \int _ c^{d} \left(\int _ a^{b} f(x, y) dx\right)  dy.
$$

Notice that, once discretized, all we did was rearrange the order in which we added a list of numbers.  This may make it seem like it is nothing, however this result (called *Fubini's Theorem*) is not always true!  For the type of mathematics encountered when doing machine learning (continuous functions), there is no concern, however it is possible to create examples where it fails (for example the function $f(x, y) = xy(x^2-y^2)/(x^2+y^2)^3$ over the rectangle $[0,2]\times[0,1]$).

Note that the choice to do the integral in $x$ first, and then the integral in $y$ was arbitrary.  We could have equally well chosen to do $y$ first and then $x$ to see

$$
\int _ {[a, b]\times[c, d]} f(x, y)dxdy = \int _ a^{b} \left(\int _ c^{d} f(x, y) dy\right)  dx.
$$

Often times, we will condense down to vector notation, and say that for $U = [a, b]\times [c, d]$ this is

$$
\int _ U f(\mathbf{x})d\mathbf{x}.
$$

## Change of Variables in Multiple Integrals
As with single variables, the ability to change variables inside a higher dimensional integral is a key tool.  Let's summarize the result without derivation.

We need a function that reparameterizes our domain of integration.  We can take this to be $\phi : \mathbb{R}^n \rightarrow \mathbb{R}^n$, that is any function which takes in $n$ real variables and returns another $n$.  To keep the expressions clean, we will assume that $\phi$ is *injective* which is to say it never folds over itself.

$$\phi(\mathbf{x}) = \phi(\mathbf{y}) \implies \mathbf{x} = \mathbf{y}$$

In this case, we can say that

$$
\int _ {\phi(U)} f(\mathbf{x})d\mathbf{x} = \int _ {U} f(\phi(\mathbf{x})) \left|\det(D\phi(\mathbf{x}))\right|d\mathbf{x}.
$$

where $D\phi$ is the *Jacobian* of $\phi$, which is the matrix of partial derivatives of $\boldsymbol{\phi} = (\phi_1(x_1, \ldots, x_n), \ldots, \phi_n(x_1, \ldots, x_n))$,

$$
D\boldsymbol{\phi} = \begin{bmatrix}
\frac{\partial \phi _ 1}{\partial x _ 1} & \cdots & \frac{\partial \phi _ 1}{\partial x _ n} \\
\vdots & \ddots & \vdots \\
\frac{\partial \phi _ n}{\partial x _ 1} & \cdots & \frac{\partial \phi _ n}{\partial x _ n}
\end{bmatrix}.
$$

Looking closely, we see that this is similar to the single variable chain rule, except we have replaced the term $\frac{du}{dx}(x)$ with $\left|\det(D\phi(\mathbf{x}))\right|$.  Let's see how we can to interpret this term.  Recall that the $\frac{du}{dx}(x)$ term existed to say how much we stretched our $x$-axis by applying $u$.  The same process in higher dimensions is to determine how much we stretch the area (or volume, or hyper-volume) of a little square (or little *hyper-cube*) by applying $\boldsymbol{\phi}$.  If $\boldsymbol{\phi}$ was the multiplication by a matrix, then we know how the determinant already gives the answer.

With some work, one can show that the *Jacobian* provides the best approximation to a multivariable function $\boldsymbol{\phi}$ at a point by a matrix in the same way we could approximate by lines or planes with derivatives and gradients. Thus the determinant of the Jacobian exactly mirrors the scaling factor we identified in one dimension.

It takes some work to fill in the details to this, so do not worry if they are not clear now.  Let's see at least one example we will make use of later on.  Consider the integral

$$
\int _ {-\infty}^{\infty} \int _ {-\infty}^{\infty} e^{-x^{2}-y^{2}} dxdy.
$$

Playing with this integral directly will get us no-where, but if we change variables, we can make significant progress.  If we let $\boldsymbol{\phi}(r, \theta) = (r \cos(\theta),  r\sin(\theta))$ (which is to say that $x = r \cos(\theta)$, $y = r \sin(\theta)$), then we can apply the change of variable formula to see that this is the same thing as

$$
\int _ 0^\infty \int_0 ^ {2\pi} e^{-r^{2}} \left|\det(D\mathbf{\phi}(\mathbf{x}))\right|d\theta dr,
$$

where

$$
\left|\det(D\mathbf{\phi}(\mathbf{x}))\right| = \left|\det\begin{bmatrix}
\cos(\theta) & -r\sin(\theta) \\
\sin(\theta) & r\cos(\theta)
\end{bmatrix}\right| = r(\cos^{2}(\theta) + \sin^{2}(\theta)) = r.
$$

Thus, the integral is

$$
\int _ 0^\infty \int _ 0 ^ {2\pi} re^{-r^{2}} d\theta dr = 2\pi\int _ 0^\infty re^{-r^{2}} dr = \pi,
$$

