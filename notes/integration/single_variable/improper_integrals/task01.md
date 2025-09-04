
$$\int_{-2}^2\frac{1}{(x+1)^2}dx$$

At $x=-1$ is undefined. Therfore, this integral should be broken into two and then computed using improper integration.

$$=\int_{-2}^{-1}\frac{1}{(x+1)^2}dx + \int_{-1}^{2}\frac{1}{(x+1)^2}dx$$

$$=\lim_{a \to -1^-}\int_{-2}^{a}\frac{1}{(x+1)^2}dx + \lim_{b \to -1^+}\int_{b}^{2}\frac{1}{(x+1)^2}dx$$

Note that $\int \frac{1}{(x+1)^2}dx=\int (x+1)^{-2}dx=-\frac{1}{x+1}+C$.

$$=\lim_{a \to -1^-}(-\frac{1}{x+1}) |^a_{-2} + \lim_{b \to -1^+}(-\frac{1}{x+1}) |^2_{b}$$

$$=\lim_{a \to -1^-}(-\frac{1}{a+1}) - (-\frac{1}{-2+1})+ (-\frac{1}{2+1}) - \lim_{b \to -1^+}(-\frac{1}{b+1})$$

$$\infty -1 -\frac{1}{3}+\infty = \infty$$
