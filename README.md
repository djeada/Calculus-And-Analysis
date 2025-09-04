# Calculus-And-Analysis

My notes, tutorials, and references on calculus and real/complex analysis. I’ve put it together to keep ideas, proofs, and examples in one place, both for my own use and for anyone else who might find it helpful—students, teachers, or just the mathematically curious. It covers fundamentals as well as some advanced topics, with an emphasis on clarity and practicality.

## What’s Inside
- Concept notes with worked examples
- Short tutorials and problem sets
- Code snippets (Python/SymPy) for symbolic and numeric exploration
- Links to high-quality open resources

## Who This Is For
- **Students:** reinforce lectures and prep for exams
- **Educators:** grab examples, problems, and visuals
- **Practitioners/enthusiasts:** refresh key results and techniques

## Using Python (SymPy × NumPy)
Mixing SymPy (symbolic) and NumPy (numeric) can be tricky. Tips:
- Keep **symbolic** workflows purely in SymPy (symbols, `Integer`, `Rational`) until you actually need numbers.
- Avoid introducing binary **floats** too early; prefer `Rational(1, 3)` or `sqrt(2)` over `1/3` or `1.4142`.
- When you need numeric arrays, **convert explicitly** with `lambdify` to produce fast NumPy functions:
  ```python
  f_num = sympy.lambdify(x, f_sym, modules="numpy")

* If you must put SymPy objects in arrays, use `dtype=object` to preserve exactness.
* For controlled approximations, use `sympy.N(expr, n)` (set precision) rather than plain `float(expr)`.

## Contributing

Contributions are welcome! Please:

1. Use clear, minimal notation and include short derivation notes.
2. Add references for theorems or nontrivial results.
3. For code, include a brief docstring and a usage example.
4. Open a PR with a concise summary of changes.

## References

A short list of dependable, freely available materials:

* **MIT Vector Calculus Notes:** [https://web.mit.edu/wwmath/vectorc/index.html](https://web.mit.edu/wwmath/vectorc/index.html)
* **MIT OCW STEM Concept Videos:** [https://ocw.mit.edu/resources/res-tll-004-stem-concept-videos-fall-2013/videos/](https://ocw.mit.edu/resources/res-tll-004-stem-concept-videos-fall-2013/videos/)
* **LibreTexts Calculus:** [https://math.libretexts.org/Bookshelves/Calculus](https://math.libretexts.org/Bookshelves/Calculus)
* **UBC Calculus (CLP) text series:** [http://www.math.ubc.ca/\~CLP/](http://www.math.ubc.ca/~CLP/)
* **“Introduction to Real Analysis Course Lectures” (YouTube playlist):** [https://youtube.com/playlist?list=PLmU0FIlJY-MngWPhBDUPelVV3GhDw\_mJu](https://youtube.com/playlist?list=PLmU0FIlJY-MngWPhBDUPelVV3GhDw_mJu)
* **University of Lethbridge Calculus Texts (GitHub):** [https://github.com/ULeth-Math-CS/CalculusTexts](https://github.com/ULeth-Math-CS/CalculusTexts)
* **UPenn Calculus materials (GitHub):** [https://github.com/shun-liang/upenn\_calculus](https://github.com/shun-liang/upenn_calculus)

