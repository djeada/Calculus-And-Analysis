
$$\int \frac{\sqrt{x^2+4}}{x}dx$$

Substitution:

$$u=\sqrt{x^2+4}$$

$$x=\sqrt{u^2-4}$$

$$\frac{du}{dx}=\frac{x}{\sqrt{x^2+4}}=\frac{x}{u}$$

$$dx=du \times \frac{u}{x}$$

$$ I = \int \frac{u}{x} \times \frac{u}{x}du$$

$$ = \int \frac{u^2}{u^2-4}du$$

Partial fractions:

$$ \frac{u^2}{u^2 - 4} = \frac{(u^2 - 4) + 4}{u^2- 4}$$

$$=\frac{u^2 - 4}{u^2 - 4} + \frac{4}{u^2 - 4}=1 + \frac{4}{u^2 - 4}$$

$$= 1+  \frac{4}{(u-2)(u+2)} = 1+ \frac{a}{u+2} +\frac{b}{u-2}$$

Let's calculate a and b:

$$a(u-2) + b(u+2) = 4 => b = 1, a = -1$$

Continuing the integral:

$$I =  \int 1 + \frac{1}{u+2} - \frac{1}{u-2}du$$

$$u - ln|u+2|+ ln|u-2| + C = \sqrt{x^2+4} + ln|\frac{ \sqrt{x^2+4}-2}{ \sqrt{x^2+4}+2}| + C$$
