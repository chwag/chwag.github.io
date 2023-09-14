---
layout: page
title: projects
permalink: /projects/
description: Our research interests
nav: true
nav_order: 1
display_categories: [growth, sb, health]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
{%- if site.enable_project_categories and page.display_categories %}
  <!-- Display categorized projects -->
  {%- for category in page.display_categories %}
  {% if category=="growth" %}
    <h2 class="category">{{ "Bacterial growth" }}</h2>
    Bacterial growth offers vital insights into life, evolution, and disease. The way bacteria grow is intricately linked to factors like nutrient availability, competitive interactions, and environmental challenges such as antibiotics. Our group focuses on two key areas:
  {% else if category=="sb" %}
    <h2 class="category">{{ "Synthetic biology" }}</h2>
    Synthetic biology explores the design and construction of biological components, both for understanding life's fundamental principles and applying them in biotechnology. Within this domain, our group is currently engaged in two areas:
  {% else if category=="health" %}
    <h2 class="category">{{ "Health data science" }}</h2>
    Health data science leverages data-driven approaches for critical healthcare challenges. Our primary focus is centred on:
  {% endif %}
  {%- assign categorized_projects = site.projects | where: "category", category -%}
  {%- assign sorted_projects = categorized_projects | sort: "importance" %}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
  {% endfor %}

{%- else -%}
<!-- Display projects without categories -->
  {%- assign sorted_projects = site.projects | sort: "importance" -%}
  <!-- Generate cards for each project -->
  {% if page.horizontal -%}
  <div class="container">
    <div class="row row-cols-2">
    {%- for project in sorted_projects -%}
      {% include projects_horizontal.html %}
    {%- endfor %}
    </div>
  </div>
  {%- else -%}
  <div class="grid">
    {%- for project in sorted_projects -%}
      {% include projects.html %}
    {%- endfor %}
  </div>
  {%- endif -%}
{%- endif -%}
</div>
