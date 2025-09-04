This folder holds small, focused scripts that help produce visualizations, run or convert notebooks, and perform symbolic computations useful for the calculus notes. The examples are intentionally minimal so they can be copied into notebooks or adapted for assignments and demonstrations.

Install the example dependencies in a virtualenv. From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

Note: the environment in the dev container already satisfied the example imports; this step is for reproducibility on other machines.

Examples (how to use)

- Run the parametric plot example (saves/shows a figure):

```bash
python3 scripts/visualization/plot_parametric.py
```

- Run the SymPy derivative example and print LaTeX:

```bash
python3 scripts/symbolic/derive_example.py
```

- Execute a notebook in-place (writes outputs back into the notebook):

```bash
python3 scripts/notebooks/run_notebook.py path/to/notebook.ipynb
```

- Generate quick derivative problems for class practice:

```bash
python3 scripts/utils/problem_gen.py
```

- Scripts are small, pedagogical helpers. For production or CI use, add tests and argument parsing.
- When running visualization scripts on a headless server, adapt them to save figures to files (use `plt.savefig(...)`) instead of `plt.show()`.
- For more complex symbolic computations, consider using Jupyter notebooks directly for interactivity.
