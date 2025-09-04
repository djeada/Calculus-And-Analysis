$$\lim_{x \to \infty} (\sqrt{x + \sqrt{x}} - \sqrt{x-1})$$

Rationalize, then factor out $\sqrt{x}$.

$$
\begin{aligned}
\lim_{x\to\infty}\bigl(\sqrt{x+\sqrt{x}}-\sqrt{x-1}\bigr)
&=\lim_{x\to\infty}\frac{(x+\sqrt{x})-(x-1)}{\sqrt{x+\sqrt{x}}+\sqrt{x-1}}\\
&=\lim_{x\to\infty}\frac{\sqrt{x}+1}{\sqrt{x+\sqrt{x}}+\sqrt{x-1}}.
\end{aligned}
$$

Write $\sqrt{x+\sqrt{x}}=\sqrt{x}\,\sqrt{1+\tfrac{1}{\sqrt{x}}}$ and $\sqrt{x-1}=\sqrt{x}\,\sqrt{1-\tfrac{1}{x}}$. Then

$$
\frac{\sqrt{x}+1}{\sqrt{x+\sqrt{x}}+\sqrt{x-1}}
=\frac{1+\tfrac{1}{\sqrt{x}}}{\sqrt{1+\tfrac{1}{\sqrt{x}}}+\sqrt{1-\tfrac{1}{x}}}
\;\xrightarrow[x\to\infty]{}\;\frac{1}{1+1}=\frac12.
$$

(Alternatively, use $\sqrt{x+h}=\sqrt{x}+\frac{h}{2\sqrt{x}}+o(1/\sqrt{x})$ with $h=\sqrt{x}$ and $h=-1$.)
