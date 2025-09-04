
I. **Integral of $2^x$:**

The process begins with solving $\int 2^x \, dx$.

II. **Expression of $2^x$ in Exponential Form:**

$2^x = e^{x \ln(2)}$.

III. **Substitution in the Integral:**

The integral becomes $\int e^{x \ln(2)} \, dx$.

IV. **Substitution for Simplification:**

By letting $u = x \ln(2)$, then $\frac{du}{dx} = \ln(2)$, or $dx = \frac{du}{\ln(2)}$.

V. **New Integral in Terms of $u$:**

After substitution, the integral transforms into:

$$\int e^u \frac{du}{\ln(2)} = \frac{1}{\ln(2)} \int e^u \, du.$$

VI. **Solution of the Simplified Integral:**

The integral of $e^u$ is $e^u$, so the solution becomes:

$$\frac{1}{\ln(2)} e^u + C.$$

VII. **Back-Substitution for $u$:**

Replace $u = x \ln(2)$, giving:

$$\frac{1}{\ln(2)} e^{x \ln(2)} + C = \frac{1}{\ln(2)} 2^x + C.$$

VIII. **Final Answer:**

The final result is:

$$\int 2^x \, dx = \frac{2^x}{\ln(2)} + C.$$

The general form of this formula is:

$$\int a^x \, dx = \frac{a^x}{\ln(a)} + C,$$

where $a > 0$ and $a \neq 1$.
