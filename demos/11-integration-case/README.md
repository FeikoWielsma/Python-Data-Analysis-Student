# Integration case demos

Run from the `datasets` folder, which holds the Eurostat extracts:

```sh
cd datasets
uv run --project .. --frozen python ../demos/11-integration-case/demo01-steps.py
uv run --project .. --frozen python ../demos/11-integration-case/demo02-audit.py
uv run --project .. --frozen streamlit run ../demos/11-integration-case/app.py   # optional
```

- `demo01-steps.py`: the twelve steps of the slides in one script, printing each step's output
  and saving `road-deaths-by-age.png`.
- `demo02-audit.py`: the intentionally wrong assistant-style proposal and the three checks that
  expose it.
- `app.py`: optional local Streamlit app; install with `uv sync --frozen --all-groups`.

The data and their provenance: [eurostat-road-safety-README.md](../../datasets/eurostat-road-safety-README.md).
`datasets/road-deaths-expected-summary.csv` was computed independently with DuckDB SQL by
`datasets/sources/derive_road_deaths_expected.py`.
