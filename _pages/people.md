---
layout: page
title: people
permalink: /people/
description: Members of the Weisse group
nav: true
nav_order: 2
display_categories: [Head, Postdocs, PhD students, Masters students, Honours students]
horizontal: false
---

<!-- pages/people.md -->
<div class="people">
{%- if site.enable_people_categories and page.display_categories %}
  <!-- Display categorized people -->
  {%- for category in page.display_categories %}
  <h2 class="category">{{ category }}</h2>
  {%- assign categorized_people = site.people | where: "category", category -%}
  {%- assign sorted_people = categorized_people | sort: "order" %}
  <!-- Generate cards for all people -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for person in sorted_people -%}
      {% include people_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for person in sorted_people -%}
      {% include people.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}
{%- endif -%}
</div>
