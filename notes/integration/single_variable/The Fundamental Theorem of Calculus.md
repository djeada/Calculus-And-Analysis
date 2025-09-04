Define the accumulation function

$$
F(x)=\int_0^{x} f(y)\,dy.
$$

It measures the (signed) area from $0$ to $x$. For any $a<b$,

$$
\int_a^{b} f(x)\,dx = F(b)-F(a),
$$

i.e., we can get the area on $[a,b]$ by “measuring out to $b$” and subtracting “what we already had at $a$.”

Now consider a tiny change $\varepsilon$. Then

$$
F(x+\varepsilon)-F(x)=\int_x^{x+\varepsilon} f(y)\,dy.
$$

By the Mean Value Theorem for integrals, there exists $c_\varepsilon\in[x,x+\varepsilon]$ with

$$
\int_x^{x+\varepsilon} f(y)\,dy = f(c_\varepsilon)\,\varepsilon.
$$

If $f$ is continuous at $x$, then $c_\varepsilon\to x$ as $\varepsilon\to 0$ and so

$$
\frac{F(x+\varepsilon)-F(x)}{\varepsilon}\to f(x).
$$

Thus $F'(x)=f(x)$. Equivalently,

$$
\frac{d}{dx}\int_0^{x} f(y)\,dy = f(x).
$$

This is the fundamental theorem of calculus (FTC, part I). Together with the identity above for $\int_a^b f$ (FTC, part II), it links antiderivatives and area.

Quick examples (use a dummy variable inside the integral):

* For $n>0$,

$$
\int_0^{x} n\,t^{\,n-1}\,dt = t^{n}\Big|_{0}^{x}=x^{n}.
$$

* Since $\frac{d}{dt}e^{t}=e^{t}$,

$$
\int_0^{x} e^{t}\,dt = e^{t}\Big|_{0}^{x}=e^{x}-1.
$$

In practice, most integration rules (substitution/change of variables, integration by parts, etc.) follow from combining this theorem with the usual differentiation rules.
