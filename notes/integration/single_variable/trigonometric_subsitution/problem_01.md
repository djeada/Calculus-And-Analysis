$$ \int_{-a}^{a} \sqrt{a^2-x^2}dx$$

Substitution:
$$ x = asin\theta , \quad dx = acos\theta d\theta$$

$$ \sqrt{a^2-x^2} = \sqrt{a^2-a^2sin^2\theta} = \sqrt{a^2}\sqrt{1-sin^2\theta}=a|cos\theta|$$

We assume $cos\theta > 0$

$$ I =  \int_{a}^{-a} acos\theta acos\theta d\theta 

Let's switch to indefinite integral:

$$a^2 \int cos^2\theta d\theta = a^2 \int \frac{1+cos2\theta}{2} d\theta =  a^2 \int \frac{1}{2} d\theta +  a^2 \int \frac{cos2\theta}{2} d\theta =\frac{a^2 }{2}\theta + \frac{a^2}{2}\frac{sin2\theta}{2} = \frac{a^2 }{2}[\theta + \frac{sin2\theta}{2}]$$

Let's take a look of the integral boundaries:

$$x = asin\theta \quad => \quad a = asin\theta \quad => \quad 1 = sin\theta \quad => \quad \theta = \frac{\pi}{2} $$

$$x = asin\theta \quad => \quad -a = asin\theta \quad => \quad -1 = sin\theta \quad => \quad \theta = -\frac{\pi}{2} $$

Going back to the integral:

$$ I = \frac{a^2 }{2}[\theta + \frac{sin2\theta}{2}]_{-\frac{\pi}{2}}^{\frac{\pi}{2}} =\frac{a^2 }{2}[\frac{\pi}{2} + \frac{sin\theta}{2} - (-\frac{\pi}{2}) -  \frac{sin(-\theta)}{2}] = \frac{a^2 }{2} \pi$$
