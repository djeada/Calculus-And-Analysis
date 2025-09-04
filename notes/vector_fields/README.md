# Vector Fields

A **vector field** on a region $U \subseteq \mathbb{R}^n$ is a function
$\mathbf F: U \to \mathbb{R}^n, \qquad \mathbf F(x) = (F_1(x),\dots,F_n(x)).$
In $\mathbb{R}^3$:
$\mathbf{F}(x,y,z)=P(x,y,z)\,\mathbf i+Q(x,y,z)\,\mathbf j+R(x,y,z)\,\mathbf k.$
**Visualization:** think of arrows attached to each point; *streamlines* or *flow lines* follow the tangent direction of $\mathbf F$.



## Core Operators

### Gradient (of a scalar field)

For $f: \mathbb{R}^3\to\mathbb{R}$:

$$nabla f=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right).
$$

**Facts:**

* Points in the direction of *steepest increase* of $f$.
* Magnitude equals the *maximum directional derivative* at that point.
* $\nabla f$ is **orthogonal** to level surfaces $f(x,y,z)=c$.
* **Directional derivative:** in unit direction $\hat{u}$: $D_{\hat u} f = \nabla f\cdot\hat u$.

**Example:** If $f=x^2+y^2+z^2$, then $\nabla f=\langle 2x,2y,2z\rangle$ (points radially outward).



### Divergence (of a vector field)

For $\mathbf F=\langle P,Q,R\rangle$:
$\nabla\cdot\mathbf F=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}.$
**Intuition:** net *outflow rate* per unit volume (sources/sinks). Positive means source-like; negative means sink-like.

**Example:** $\mathbf F=\langle x,y,z\rangle\Rightarrow\nabla\cdot\mathbf F=3$.



### Curl (of a vector field)

For $\mathbf F=\langle P,Q,R\rangle$:

$$nabla\times \mathbf F=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},; \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},; \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right).
$$

Determinant mnemonic:

$$nabla\times\mathbf F=\begin{vmatrix}
\mathbf i & \mathbf j & \mathbf k\\
\partial_x & \partial_y & \partial_z\\
P & Q & R
\end{vmatrix}.
$$

**Intuition:** local *rotation/twisting* (circulation density). Direction by right-hand rule.

**Example:** $\mathbf F=\langle -y,\;x,\;0\rangle\Rightarrow\nabla\times\mathbf F=\langle 0,0,2\rangle$ (constant swirl about the $z$-axis).



### Laplacian

For a scalar field $f$: $\displaystyle \Delta f=\nabla\cdot(\nabla f)=f_{xx}+f_{yy}+f_{zz}$. A function with $\Delta f=0$ is **harmonic**.



## 2D Specializations

For $\mathbf F(x,y)=\langle P(x,y),Q(x,y)\rangle$:

* $\displaystyle \nabla\cdot\mathbf F=P_x+Q_y$ (same formula, ignoring $z$).
* **Scalar curl** ($k$-component): $\displaystyle \operatorname{curl}_z\mathbf F=Q_x-P_y$.



## Conservative (Gradient) Fields

A vector field $\mathbf F$ is **conservative** if there exists a potential $f$ with $\mathbf F=\nabla f$.

**Equivalent characterizations (on a simply connected domain):**

* $\nabla\times\mathbf F=\mathbf 0$ (curl-free).
* Line integrals are *path independent*.
* The circulation around every closed loop is zero: $\displaystyle \oint_C \mathbf F\cdot d\mathbf r=0$.
* **Gradient Theorem (Fundamental Theorem for Line Integrals):** $\displaystyle \int_{C}\nabla f\cdot d\mathbf r=f(B)-f(A)$, where $A,B$ are the endpoints of $C$.

> **Domain matters:** Curl-free does *not* imply conservative if the domain has a “hole.” Example on $\mathbb R^2\setminus\{(0,0)\}$: $\mathbf F=\left\langle -\frac{y}{x^2+y^2},\frac{x}{x^2+y^2}\right\rangle$ has zero curl off the origin, but $\oint_{|\mathbf r|=1}\mathbf F\cdot d\mathbf r=2\pi\neq 0$.

**Finding a potential:**
If $\mathbf F=\langle P,Q,R\rangle$, integrate one component and match cross-partials.

* Example: $\mathbf F=\langle 2x,2y,2z\rangle\Rightarrow f=x^2+y^2+z^2 + C$.



## Integrals of Fields

### Line integrals

* **Vector field along a curve (work):** For a smooth parameterization $\mathbf r(t)$, $a\le t\le b$,
  $\int_C \mathbf F\cdot d\mathbf r=\int_a^b \mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$
* **Scalar field along a curve (weighted arc length):** $\displaystyle \int_C f\, ds=\int_a^b f(\mathbf r(t))\,\|\mathbf r'(t)\|\,dt$.

### Surface integrals (flux)

For an oriented surface $S$ with unit normal $\mathbf n$:
$\iint_S \mathbf F\cdot\mathbf n\,dS\quad (\text{net outflow through }S).$
Parameterization $\mathbf r(u,v)$: use $\mathbf n\,dS=\frac{\partial\mathbf r}{\partial u}\times\frac{\partial\mathbf r}{\partial v}\,du\,dv$.

### Volume integrals

Triple integral over a region $V$: $\displaystyle \iiint_V g\,dV$.



## The Big Three Theorems (Bridges between integrals)

* **Gradient Theorem:** $\displaystyle \int_{C}\nabla f\cdot d\mathbf r=f(B)-f(A)$.
* **Stokes’ Theorem:** For an oriented surface $S$ with boundary $\partial S$:
  $\oint_{\partial S} \mathbf F\cdot d\mathbf r=\iint_S (\nabla\times\mathbf F)\cdot\mathbf n\,dS.$
* **Divergence (Gauss) Theorem:** For a solid $V$ with boundary $\partial V$:
  $\iint_{\partial V} \mathbf F\cdot\mathbf n\,dS=\iiint_V \nabla\cdot\mathbf F\,dV.$
  *Example check:* $\mathbf F=\langle x,y,z\rangle$ on a sphere of radius $a$: flux $=4\pi a^3$.



## Quick Worked Examples

1. **Div & Curl:** Let $\mathbf F=\langle x^2, yz, x-2z\rangle$.

* $\nabla\cdot\mathbf F=2x+z-2$.
* $\nabla\times\mathbf F=\langle -y,-1,0\rangle$.

2. **Circulation via Green/Stokes:** $\mathbf F=\langle -y,x,0\rangle$ around unit circle $C$ in the $xy$-plane.

* $\operatorname{curl}_z\mathbf F=2$, so $\displaystyle \oint_C \mathbf F\cdot d\mathbf r=\iint_{\text{disk}}2\,dA=2\pi$.

3. **Conservative check & potential:** $\mathbf F=\langle 2xy, x^2+2z, 2y\rangle$.

* Curl is zero; domain is all of $\mathbb R^3$ (simply connected) $\Rightarrow$ conservative.
* Integrate: from $P=2xy$ get $f=x^2y+g(y,z)$. Match $f_y=x^2+g_y=x^2+2z\Rightarrow g=2zy+h(z)$. Then $f_z=2y+h'(z)=2y\Rightarrow h'=0$. So a potential is $f=x^2y+2zy$.



## Common Pitfalls & Tips

* **Orientation matters:** reversing curve/surface orientation flips the sign of the integral.
* **Units:** grad has units of $f$ per length; div has units of 1/length; curl has units of 1/length times field units.
* **Domain holes:** curl-free $\not\Rightarrow$ conservative unless the domain is simply connected.
* **Smoothness:** many theorems assume continuous partials ($C^1$) on/inside the region.
* **2D vs 3D:** in 2D, “curl” is the scalar $k$-component; don’t confuse with 3D vector curl.

## Alternative Coordinates (quick reference)

**Cylindrical** $(r,\theta,z)$ with components $\mathbf F=F_r\,\mathbf e_r+F_\theta\,\mathbf e_\theta+F_z\,\mathbf e_z$:
$\nabla\cdot\mathbf F=\frac{1}{r}\frac{\partial}{\partial r}(rF_r)+\frac{1}{r}\frac{\partial F_\theta}{\partial\theta}+\frac{\partial F_z}{\partial z}.$

$$begin{aligned}
(\nabla\times\mathbf F)_r&=\tfrac{1}{r}\Big(\tfrac{\partial F_z}{\partial\theta}-\tfrac{\partial (rF_\theta)}{\partial z}\Big),\\
(\nabla\times\mathbf F)_\theta&=\tfrac{\partial F_r}{\partial z}-\tfrac{\partial F_z}{\partial r},\\
(\nabla\times\mathbf F)_z&=\tfrac{1}{r}\Big(\tfrac{\partial (rF_\theta)}{\partial r}-\tfrac{\partial F_r}{\partial\theta}\Big).
\end{aligned}
$$

**Spherical** \((r,\theta,\varphi)\) (radial, polar, azimuth):
\[\nabla\cdot\mathbf F=\frac{1}{r^2}\frac{\partial}{\partial r}(r^2F_r)+\frac{1}{r\sin\theta}\frac{\partial}{\partial\theta}(\sin\theta\,F_\theta)+\frac{1}{r\sin\theta}\frac{\partial F_\varphi}{\partial\varphi}.\]


## Notation & Identities
- Unit vectors: \(\mathbf i,\mathbf j,\mathbf k\) or \(\mathbf e_x,\mathbf e_y,\mathbf e_z\).
- \(\displaystyle \Delta f=\nabla\cdot\nabla f\) (Laplacian).
- **Vector identities (when fields are sufficiently smooth):**
  - \(\nabla\times(\nabla f)=\mathbf 0\).
  - \(\nabla\cdot(\nabla\times\mathbf F)=0\).
  - Product rules: \(\nabla\cdot(\phi\mathbf F)=\phi\,\nabla\cdot\mathbf F+\nabla\phi\cdot\mathbf F\); \(\nabla\times(\phi\mathbf F)=\nabla\phi\times\mathbf F+\phi\,\nabla\times\mathbf F\).

### Mini “Sanity Checks”
- If \(\nabla\cdot\mathbf F\equiv 0\), total flux through a closed surface can be zero (e.g., incompressible flow), but local flux may be nonzero.
- If \(\nabla\times\mathbf F\equiv 0\) on a simply connected domain, \(\mathbf F\) is conservative \(\Rightarrow\) closed-loop work is zero.
- For spheres or circles with radial fields, expect symmetry to simplify integrals.


> **Easy To Remember:**
> - \(\nabla f\): where does \(f\) increase fastest? (direction & rate)
> - \(\nabla\cdot\mathbf F\): how much “stuff” is created/removed near a point?
> - \(\nabla\times\mathbf F\): how strongly does the field swirl there?

