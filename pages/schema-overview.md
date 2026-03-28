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

  body .content details.schema-overview-help > summary {
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.45rem;
    list-style: none;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
    line-height: 1.35;
    color: inherit !important;
  }

  body .content details.schema-overview-help > summary::marker {
    content: "";
  }

  body .content details.schema-overview-help > summary::-webkit-details-marker {
    display: none;
  }

  body .content details.schema-overview-help > summary::before {
    content: "▸";
    display: inline-block;
    font-size: 0.9em;
    line-height: 1;
    color: #7b6a35;
    transform: translateY(0.02em);
    transition: transform 120ms ease;
  }

  body .content details.schema-overview-help[open] > summary::before {
    transform: rotate(90deg);
  }

  body .content details.schema-overview-help[open] > summary {
    margin-bottom: 8px;
  }

  body .content details.schema-overview-help.alert::before {
    top: calc(var(--bs-alert-padding-y) + 0.68rem);
    transform: translateY(-50%);
  }
</style>

<details class="schema-overview-help alert alert-tips">
<summary>How to read this diagram?</summary>
<div markdown="1">

- Each box is one table of the schema.
- Each row is one column name in that table.
- A `*` means the column is required.
- The key icon marks columns in the [primary key](https://en.wikipedia.org/wiki/Primary_key): values that uniquely identify each row (sometimes using multiple columns together).
- Arrows show [foreign key](https://en.wikipedia.org/wiki/Foreign_key) relationships: a column in one table points to a row in another table.
- `...` means additional columns are allowed by the schema but not listed here.
- Click table names and fields to read descriptions.
- Use the `Open table page` link shown in a table-name tooltip to open the dedicated table page.

</div>
</details>

<div class="schema-overview-bleed">
  {% include schema-diagram-embed.html %}
</div>
