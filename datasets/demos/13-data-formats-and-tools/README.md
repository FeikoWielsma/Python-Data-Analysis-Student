# Module 13 order ledger

`orders.csv` is a synthetic teaching fixture authored for DSC100 in
October 2026. It contains no customer data and makes no claim about real
sales. The dates are fictional observation dates, not a download date.
The course's reuse terms apply; there is no third-party upstream source.
It serves the module 13 **slide demos only**, where every exclusion can be
checked by hand. Exercise 13 uses the real Eurostat road-death extract; see
[eurostat-road-safety-README.md](../../eurostat-road-safety-README.md).

Each row is one order. `order_id` is an opaque four-character identifier
(leading zeros matter); `ordered_at` is a calendar date without a time zone;
`region` is a shipping region; `status` is shipped or cancelled; `units` is
a nonnegative integer quantity. Empty fields mean unknown, not zero.
The row with zero units deliberately tests the distinction.

Task: for shipped orders dated June 2026 with a known region and recorded
units, report the units and orders per region. Sort regions
alphabetically. There are nine June shipped orders, but only six qualify:
two have unknown units and one has an unknown region. Report this population
restriction beside the answer; the result is not total June demand.

Expected answer: North has 7 units across 3 orders; South has 9 units across
3 orders. East's only order has unknown units and is excluded, so there is
no East result row. May, July and cancelled orders are also excluded.
