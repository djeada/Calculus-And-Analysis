$$\int \sqrt{9-x^2} dx$$

$x=3\sin t$, $\frac{dx}{dt}=3 \cos t$, $t=sin^{-1}\frac{x}{3}$

$$=\int \sqrt{9 -(3\sin t)^2} 3 \cos t dt$$

$$=3 \int \sqrt{9} \sqrt{1 -(\sin t)^2}  \cos t dt$$

$$=9 \int \cos^2 t dt$$

$$=\frac{9}{2} \int[ \cos (2t) + 1 ]dt$$

$$=\frac{9}{2} (\int \cos (2t) dt \int dt)$$

$$=\frac{9}{2} (\frac{1}{2} \sin (2t) + t )$$

$$= \frac{9}{4} \sin (2t) + \frac{9}{2} t $$

$$= \frac{9}{4} \sin (2 \cdot sin^{-1}\frac{x}{3}) + \frac{9}{2} sin^{-1}\frac{x}{3} $$

$\theta = sin^-1(\frac{x}{3})$, $\sin \thtea t = \frac{x}{3}$, $\cos \theta = \frac{\sqrt{x^2-9}}{3}$

$$\sin 2\theta = 2 \cdot \frac{x}{3} \cdot \frac{\sqrt{x^2-9}}{3}$$

$$= \frac{9}{4} \frac{2x\sqrt{x^2-9}}{9} + \frac{9}{2} sin^{-1}\frac{x}{3} + C$$

$$= \frac{2x\sqrt{x^2-9}}{2} + \frac{9}{2} sin^{-1}\frac{x}{3} + C$$
