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
environmental stimuli with cellular mechanisms.

<div>
<span> Currently working on this are: </span> 
{%- for person in site.people -%}
    {%- for project in person.projects -%}
        {%- if "growth" == project -%}
            <li class="tab"><a href="{{ person.url }}">{{ person.title }}</a></li>
        {%- endif -%}
    {%- endfor -%}
{%- endfor -%}
</div>

--------

### Emergence of antibiotic resistance
Given the pressing rise of antibiotic resistance, we investigate mechanisms and environmental factors affecting drug 
efficacy. Our goal is to derive insights that can enhance existing antibiotic therapies by addressing the misuse and 
overuse of antibiotics.

<div>
<span> Currently working on this are: </span>
{%- for person in site.people -%}
    {%- for project in person.projects -%}
        {%- if "ar" == project -%}
            <li class="tab"><a href="{{ person.url }}">{{ person.title }}</a></li>
        {%- endif -%}
    {%- endfor -%}
{%- endfor -%}
</div>