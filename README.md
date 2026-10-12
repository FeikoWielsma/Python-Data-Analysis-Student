# Data Analysis with Python

DSC100 teaches practical data analysis with NumPy, pandas, Matplotlib and Seaborn:
load and inspect data, select, clean, combine and group it, work with time series,
and explain a result with a readable chart. The course closes with an integration
case on real Eurostat data and a short tour of scikit-learn. An optional module
compares Parquet, DuckDB and Polars.

This repository contains the course handouts and runnable material. It is updated
after a successful course build.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/FeikoWielsma/Python-Data-Analysis-Student)

## Following the course online : GitHub Codespaces

If you join remotely, or cannot install software on your machine, you can do
the whole course in your browser. You need a free GitHub account; it includes
60 hours a month of Codespaces, which is more than the course uses.

1. Open <https://codespaces.new/FeikoWielsma/Python-Data-Analysis-Student> and
   click **Create codespace**. The first start takes a few minutes: it installs
   uv and the course's Python packages.
2. You get VS Code in the browser with Python 3.14, uv, pandas, JupyterLab and the
   Python, Jupyter and Ruff extensions installed. Skip **Local setup** below. Open
   a notebook, such as `demos/02-intro-pandas/demos.ipynb`, and pick the `.venv`
   kernel if VS Code asks. Prefer JupyterLab? In <https://github.com/codespaces>,
   choose **...** next to your codespace and then **Open in JupyterLab**.
3. Your work is kept inside the codespace between days. Reopen it from
   <https://github.com/codespaces>. A codespace stops itself after 30 minutes
   of inactivity; that is harmless, your files stay.

## Course material

- [Slides (PDF)](DSC100-Data-Analysis-with-Python.pdf)
- [Exercise guide (PDF)](DSC100-Data-Analysis-with-Python-Exercises.pdf)
- [Exercise guide (HTML)](DSC100-Data-Analysis-with-Python-Exercises.html)
- `demos/`: the examples from the slides, one folder per module, as a notebook
  (`demos.ipynb`) and as separate scripts
- `exercises/`: notebooks with instructions and cells to complete
- `solutions/`: reference answers
- `datasets/`: data files and their source information

| Module | Exercise | Solution |
| --- | --- | --- |
| 1 NumPy | [Notebook](exercises/01-numpy/exercise.ipynb) | [Notebook](solutions/01-numpy/solution.ipynb) |
| 2 Pandas Intro | [Notebook](exercises/02-intro-pandas/exercise.ipynb) | [Notebook](solutions/02-intro-pandas/solution.ipynb) |
| 3 Selecting and Filtering | [Notebook](exercises/03-selecting-and-filtering/exercise.ipynb) | [Notebook](solutions/03-selecting-and-filtering/solution.ipynb) |
| 4 Cleaning and Transforming | [Notebook](exercises/04-cleaning-and-transforming/exercise.ipynb) | [Notebook](solutions/04-cleaning-and-transforming/solution.ipynb) |
| 5 Advanced Indexing | [Notebook](exercises/05-advanced-indexing/exercise.ipynb) | [Notebook](solutions/05-advanced-indexing/solution.ipynb) |
| 6 Rearranging Data | [Notebook](exercises/06-rearranging-data/exercise.ipynb) | [Notebook](solutions/06-rearranging-data/solution.ipynb) |
| 7 Combining Data | [Notebook](exercises/07-combining-data/exercise.ipynb) | [Notebook](solutions/07-combining-data/solution.ipynb) |
| 8 Grouping Data | [Notebook](exercises/08-grouping-data/exercise.ipynb) | [Notebook](solutions/08-grouping-data/solution.ipynb) |
| 9 Matplotlib, pandas plotting, Seaborn | [Notebook](exercises/09-matplotlib/exercise.ipynb) | [Notebook](solutions/09-matplotlib/solution.ipynb) |
| 10 Time Series | [Notebook](exercises/10-time-series/exercise.ipynb) | [Notebook](solutions/10-time-series/solution.ipynb) |
| 11 Integration Case | [Notebook](exercises/11-integration-case/exercise.ipynb) | [Notebook](solutions/11-integration-case/solution.ipynb) |
| 13 Data Formats and Tools (optional) | [Notebook](exercises/13-data-formats-and-tools/exercise.ipynb) | [Notebook](solutions/13-data-formats-and-tools/solution.ipynb) |

Every module, including 12 (Scikit-Learn Essentials) and appendix A (Reading Other
Sources), has its demos in `demos/<module>/demos.ipynb`.

## Browser notebooks

Open <https://analysis.feikowielsma.nl/> and sign in with the course password.
Choose an exercise at `/course`. Each release gets a working copy of its own;
saved answers remain available when the material is updated.

## Local setup

Clone the repository:

```sh
git clone https://git.feikowielsma.nl/SpiralTrain/Python-Data-Analysis-Student.git
cd Python-Data-Analysis-Student
```

The [latest release](https://git.feikowielsma.nl/SpiralTrain/Python-Data-Analysis-Student/releases/tag/latest)
also provides a ZIP of the same material.

Install [uv](https://docs.astral.sh/uv/) and run from the course folder:

```sh
uv sync --frozen
uv run --frozen jupyter lab
```

Python 3.12–3.14 is supported; 3.14 is the teaching default.
`uv sync --frozen --all-groups` adds the optional Numba and Streamlit packages.
Keep the lockfile unchanged during a course week.

In JupyterLab, open `exercises/<module>/exercise.ipynb`, run the first cell and
complete the steps. Compare with the solution when you are done or stuck. Restart
the kernel and run all cells at the end to check that the notebook works from top
to bottom.

## Running a demo

Open `demos/<module>/demos.ipynb` in JupyterLab and run its first cell: it switches to
the folder with that module's data files. Then run any demo with Shift+Enter. The
heading above each cell matches the `demoNN · ...` pill on the slide. Change the code
and run the cell again to experiment; `git restore demos` brings back the original.

The same demos are in the folder as separate `.py` scripts. They read their data with
a bare file name, so run a script from the matching data folder, for example:

```sh
cd datasets/demos/02-intro-pandas
uv run --project ../../.. --frozen python ../../../demos/02-intro-pandas/demo08-head-and-tail.py
```

Save your own work before running `git pull` to retrieve new course material.
