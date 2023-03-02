---
layout: page
permalink: /publications/
title: publications
description: Publications in reversed chronological order
years: [2006, 2009, 2010, 2012, 2013, 2015, 2016, 2018, 2019, 2020, 2021, 2022]
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
