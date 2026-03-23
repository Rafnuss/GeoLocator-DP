---
title: Overview
background: /assets/schema-overview.jpg
permalink: /schema-overview/
---

<style>
  .schema-overview-bleed {
    width: min(1450px, calc(100vw - 24px));
    margin-left: 50%;
    transform: translateX(-50%);
    --page-width: min(1450px, calc(100vw - 24px));
  }

  @media (max-width: 640px) {
    .schema-overview-bleed {
      width: calc(100vw - 12px);
      --page-width: calc(100vw - 12px);
    }
  }

  .schema-overview-help summary {
    cursor: pointer;
    font-weight: 700;
  }

  .schema-overview-help[open] summary {
    margin-bottom: 8px;
  }
</style>

This diagram shows how the GeoLocator DP tables are connected.
Each table and each column is documented in detail on its own dedicated page.
Click a table name in the diagram to open that table reference page.

<details class="schema-overview-help alert alert-tips" style="padding-left: 32px;">
<summary>How to read this diagram?</summary>
<div markdown="1">

- Each box is one table of the schema.
- Each row is one column name in that table.
- A `*` means the column is required.
- The key icon marks columns in the [primary key](https://en.wikipedia.org/wiki/Primary_key): values that uniquely identify each row (sometimes using multiple columns together).
- Arrows show [foreign key](https://en.wikipedia.org/wiki/Foreign_key) relationships: a column in one table points to a row in another table.
- `...` means additional columns are allowed by the schema but not listed here.
- Click a table name to open the dedicated page with full column-level details.
- Hover table names and fields to read descriptions.
- Hover arrows to inspect which source and target fields are linked.

</div>
</details>

<div class="schema-overview-bleed">
  {% include schema-diagram-embed.html %}
</div>
