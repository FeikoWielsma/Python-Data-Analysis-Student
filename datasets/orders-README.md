# Combining Data fixtures

Authored fixture: synthetic DSC100 teaching data, October 2026. All rows and
values were invented for this lesson; no real customers, upstream download,
or historical sales claim.
The months are labels, with no implied observation year.

These fixtures serve the **slide demos only**: a five-order example lets
learners count every match and every inflated unit by hand. Exercise 7 uses
real World Bank files instead; see [wb-population-README.md](wb-population-README.md).

- `orders-jan.csv`, `orders-feb.csv`, `orders-mar.csv`: one row per distinct order.
  `order_id` is a text identifier; `customer_id` is a three-character text
  identifier (leading zeros matter); `units` is a nonnegative integer count.
  February alone supplies `channel` (`online` or `store`). Missing channel in
  other months means unrecorded, not a particular sales channel.
- `orders-customers.csv`: intended one row per customer, with a text `region`.
  The second `001,North` row is a deliberate exact duplicate introduced by
  an invented repeated export. Only this documented exact duplicate may be
  removed. Conflicting records would require investigation. Customer `004`
  has no lookup row; `005` has a lookup row but no order.
- `orders-wide.csv`: a separate reshaping fixture, one row per customer and
  one count per month. It is not an aggregation of the order files.

The order files have 2 + 2 + 1 = 5 rows and 10 + 20 + 30 + 40 + 50 = 150 units.
A left join to the unchecked lookup repeats both orders for `001`: seven
rows and 190 units. With the exact duplicate removed, five rows and 150 units
remain, including the unresolved 50 units for `004`. Known regions account
for 100 units; excluding the unknown region changes the population.
The wide fixture has four measurements totaling 100 units.
