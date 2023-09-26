---
layout: page
title: Bacterial growth
description: Investigating bacterial growth and how it is controlled
img: assets/img/12.jpg
importance: 1
category: work
---

Bacterial growth offers vital insights into life, evolution, and disease. The way bacteria grow is intricately linked 
to factors like nutrient availability, competitive interactions, and environmental challenges such as antibiotics. Our 
group focuses on two key areas:

### Multi-scale models of bacterial cells
We develop computational models to investigate bacterial growth adaptation in complex environments. Our models are 
rooted in core cellular mechanisms, which allows us to predict growth as it emerges from the dynamic interplay of 
environmental stimuli with the cell mechanisms.

<div>
<p> Currently working on this: 
{%- assign people = site.people -%}
{%- for person in people -%}
    {% assign name = person.title %}
    {% assign projects = person.projects %}
    {% for project in projects %}
        {% if "growth" == project %}
             <a href="{{ site.people }}">{{ name }}, </a> 
        {% endif %}
    {% endfor %}
{%- endfor %}
</p>
</div>

--------

### Emergence of antibiotic resistance
Given the pressing rise of antibiotic resistance, we investigate mechanisms and environmental factors affecting drug 
efficacy. Our goal is to derive insights that can enhance existing antibiotic therapies by addressing the misuse and 
overuse of antibiotics.