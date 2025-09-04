Find the Maclaurin series of

$$f(x)=\frac{1}{1+(2x)^2}$$

and also write your answer in $\sum$ notation.

$$\sum_{n=0}^{\infty}x^n=1+x+x^2+...=\frac{1}{1-x}$$

Observe that if x in the $\frac{1}{1-x}$ is replaced by $-(2x)^2$, then it becomes $\frac{1}{1+(2x)^2}$

$$\sum_{n=0}^{\infty}(-(2x)^2)^n=1+(-(2x)^2)+(-(2x)^2)^2+...=\frac{1}{1-(-(2x)^2)}$$

$$\sum_{n=0}^{\infty}(-1)^n((2x)^2)^n=\frac{1}{1+(2x)^2}$$

$$\sum_{n=0}^{\infty}(-1)^n(2x)^{2n}=\sum_{n=0}^{\infty}(-1)^n2^{2n}x^{2n}$$

What inequaliteis must x satisfy so that the above Maclaurin series do converge to $\frac{1}{1+(2x)^2}$?

$a=1$, $r=-(2x)^2$ and geometric series converge for $|r|<1$.

$$|-(2x)^2|<1$$

$$(2x)^2<1$$

$$-1<2x<1$$

$x \in (-\frac{1}{2}, \frac{1}{2})$
