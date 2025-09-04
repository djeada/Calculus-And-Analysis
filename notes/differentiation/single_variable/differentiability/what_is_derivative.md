Let's imagine we have a curve. Now we take any two points and take a line joining these two points. This line is called a secant as it cuts the curve at at least two points( there may be more but that is none of our concern). Now if you imagine taking these points closer to each other, you will see the secant becomes close to the tangent line. If you keep decreasing the distance between these points, and make them arbitrarily close, the secant line therefore becomes the tangent. This needs to be rigorously proved, but it is a good way to get a "feel" of what is going on, which I believe is what you are asking for.

Now the slope(m

) of this secant line should be equal to the slope of the tangent.

Thus

$$m = \frac{\Delta y}{\Delta x} = \frac{y_2-y_1}{x_2-x_1}$$

Taking $x_2=x_1+h$ and taking the limit $h\to0$

$$m=\lim_{h\to0}\frac{f(x_1+h)-f(x_1)}{h}$$

This limit is called the "derivative" and is equal to the slope as we wanted.
