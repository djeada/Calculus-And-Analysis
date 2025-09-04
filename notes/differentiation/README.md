## Formal Definition of a derivative

The derivative of a continuous function $f(x)$ on an interval $I$ is defined as the limit of the difference quotient
$$f'(x) = \lim_{\Delta x \to 0}{\frac{f(x + \Delta x) - f(x)}{\Delta x}}$$
Where $\Delta x$ is a small change in $x$


## Differentiability

It's important to realize that a function may not be differentiable at every point; that is, you might not be able to calculate the derivative for every point on the function line.

To be differentiable at a given point:

    The function must be continuous at that point.
    The tangent line at that point cannot be vertical
    The line must be smooth at that point (that is, it cannot take on a sudden change of direction at the point)

## Derivative Rules and Properties

The differntial operator is a linear operator, i.e.\,

$${(f(x) \pm g(x))}' = f'(x) \pm g'(x)$$

$${(c\cdot f(x)}' = c\cdot f'(x)$$

### Product Rule

$$(f(x)\cdot g(x))' = f'(x)\cdot g(x) + f(x)\cdot g'(x)$$

Quotient Rule:
$$\left(\frac{f(x)}{g(x)}\right)' = \frac{f'(x)\cdot g(x) - g'(x)\cdot f(x)}{(g(x))^2}$$

### Chain Rule
$$ (f(g(x)))' = f'(g(x))\cdot g'(x)$$

For a function $f(x) = u(x)v(x)$, the ${n^{th}}$ derivative, $f^{(n)}(x)$ is given by

$$f^{(n)}= \sum_{r=0}^{n}{^nC_r u^{(r)}v^{(n-r)}}$$

## Common Derivatives

$$\frac{d}{dx}a^x = (\ln a)a^x $$

$$\frac{d}{dx}\log_a x = \frac{1}{x\ln a} $$

$$\frac{d}{dx}\sin x = \cos x $$

$$\frac{d}{dx}\cos x = -\sin x $$

$$\frac{d}{dx}\tan x = \sec^2 x$$

$$\frac{d}{dx}\csc x = -\csc x \cot x $$

$$\frac{d}{dx}\sec x = \sec x \tan x $$

$$\frac{d}{dx}\cot x = -\csc^2 x $$

$$\frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1 - x^2}} $$

$$\frac{d}{dx}\cos^{-1}x = - \frac{1}{\sqrt{1 - x^2}} $$

$$\frac{d}{dx}\tan^{-1}x = \frac{1}{1 + x^2} $$

$$\frac{d}{dx}\sec^{-1}x = \frac{1}{ x \sqrt{x^2 - 1}} $$

$$\frac{d}{dx}\csc^{-1}x = -\frac{1}{ x \sqrt{x^2 - 1}} $$

$$\frac{d}{dx}\cot^{-1}x = -\frac{1}{1 + x^2} $$

## Mean Value Theorem

If a function $f(x)$ is continuous and differentiable in the range $(a,c)$, then there exists atleast one value b, $a < b < c$, such that

$$f'(b) = \frac{f(c) - f(a)}{c - a}$$

## Applications of Derivatives

## Tangent to a Curve

Tangent to a curve $f(x)$ at a point $a$:

$$\frac{d}{dx}f(x)\Big\rvert_{x=a}$$

For a straight line passing through points $\mathrm{(x_1,y_1)}$ and  $\mathrm{(x_2, y_2)}$, the slope, m, is constant and is calculated by:

$$m = \tan\theta = \frac{y_2 - y_1}{x_2 - x_1}$$

Where $\theta$ is the angle of the line with the x-axis

## Analysis of a Curve

### Critical Points

$x = a$ is a critical point of $ f(x) $ if $ f'(a)=0 $ or $ f'(a) $ doesn't exist.

### Slope

* $ f(x) $ is increasing on an interval $I$ if $f'(x) > 0$, i.e.\ it has a positive slope on that interval.
* $f(x)$ is decreasing on an interval $I$ if $f'(x) < 0$, i.e.\ it has a negative slope on that interval.
* $f(x)$ is constant on an interval $I$ if $ f'(x) = 0 $.

### Concavity

* $f(x)$ is concave up on an interval $I$ if $ f''(x) > 0 $.
* $f(x)$ is concave down on an interval $I$ if $f''(x) < 0 $.

### Inflection Points

$x = a$ is an inflection point of $f(x)$ if the concavity changes at $f(a)$.

### Extrema

$f(a)$ is a stationary point on an interval $I$ if $f'(a) = 0$.

* If $f''(a) > 0$, then $f(a)$ is a local minimum.
* If $f''(a)< 0$, then $f(a)$ is a local maximum.
* If $f''(a)= 0$, then the second derivative test fails.


## Taylor Polynomials

Let $f(x)$ be a real-valued function that is infinitely differentiable at $x = x_0$. The Taylor series expansion for the function $f(x)$ centered around the point $x = x_0$ is given by

$$\sum_{n=0}^{\infty}f^{(n)}(x_0)\frac{(x - x_0)^{n}}{n!}$$

Where $f^{(n)}(x_0)$ is the $n^\text{th}$ derivative of $f(x)$ at $x = x_0$.

