---
layout: page
title: people
permalink: /people/
description: Who we are
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
      {% include people_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for person in sorted_people -%}
      {% include people.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}
{%- else -%}
  <!-- Generate cards for all people -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for person in site.people -%}
      {% include people_horizontal.liquid %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for person in site.people -%}
      {% include people.liquid %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>

--------

## Alumni

### Staff
<div>
{%- for person in site.alumni -%}
  {%- if "Staff" == person.category -%}
    <li class="tab">{{ person.title }}, {{ person.degree }}</li>
  {%- endif -%}
{%- endfor -%}
<br>
</div> 

<!--
% ### Postdocs
<div>
{%- for person in site.alumni -%}
  {%- if "Postdoc" == person.category -%}
    <li class="tab">{{ person.title }}, {{ person.degree }}</li>
  {%- endif -%}
{%- endfor -%}
</div>

### PhD students
<div>
{%- for person in site.alumni -%}
  {%- if "PhD" == person.category -%}
    <li class="tab">{{ person.title }}, {{ person.degree }}</li>
  {%- endif -%}
{%- endfor -%}
</div>
-->

### Honours and Masters
<div>
{%- for person in site.alumni -%}
  {%- if "Honours" == person.category or "Master" == person.category-%}
    <li class="tab">{{ person.title }}, {{ person.degree }}</li>
  {%- endif -%}
{%- endfor -%}
</div>