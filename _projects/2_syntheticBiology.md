---
layout: page
title: Synthetic biology
description: Understanding and optimising synthetic biological systems
img: assets/img/syntheticBiology.jpg
importance: 3
category: work
---

Synthetic biology explores the design and construction of biological components, both for understanding life's 
fundamental principles and applying them in biotechnology. Within this domain, our group is currently engaged in two 
areas:

### Cell-free protein expression

We develop and analyse computational models to probe conditions that drive self-regeneration within cell-free 
expression systems. We aim to both improve the efficiency and sustainability of protein production and gain deeper 
insights into hallmarks of self-regeneration underpinning living systems.

<div>
<span> Currently working on this: </span>
{%- for person in site.people -%}
    {%- for project in person.projects -%}
        {%- if "cfps" == project -%}
            <li class="tab"><a href="{{ person.url }}">{{ person.title }}</a></li>
        {%- endif -%}
    {%- endfor -%}
{%- endfor -%}
</div>

--------

### Model inference and optimal experimental design

We develop robust methods for parameter inference and optimal experimental design. These tools allow us to propose 
experiments designed to maximise the insights derived and expedite the design-build-test-learn cycle.

<div>
<span> Currently working on this: </span>
{%- for person in site.people -%}
    {%- for project in person.projects -%}
        {%- if "inference" == project -%}
            <li class="tab"><a href="{{ person.url }}">{{ person.title }}</a></li>
        {%- endif -%}
    {%- endfor -%}
{%- endfor -%}
</div>