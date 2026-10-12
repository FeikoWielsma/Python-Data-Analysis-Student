# Combining Data demos

The CSV dictionary and the known defects in the fixtures are in
[the fixture notes](../../datasets/orders-README.md). Run a demo from the course root:

```sh
uv run --frozen python demos/07-combining-data/demo04-duplicate-keys.py
```

- Demo 03 and demo 06 use `small_orders` and `small_customers`, a separate three-order
  example that makes each join type easy to count.
- Demo 04 uses the five monthly orders to show a many-to-many join inflating a total.
- Demo 05 catches the expected dtype error and shows that pandas matches missing keys.
- Demo 07 separates layout changes from aggregating repeated measurements.

pandas references: [merge](https://pandas.pydata.org/docs/reference/api/pandas.merge.html),
[concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html),
[melt](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html),
[pivot_table](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html),
[join](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html).
