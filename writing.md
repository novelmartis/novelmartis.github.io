---
layout: page
title: Writing
permalink: /writing/
---

# Writing
<p class="muted">
Notes, essays, and occasional technical posts.
</p>

<div class="projlist">
{% assign items = site.writing | sort: "date" | reverse %}
{% for p in items %}
  <div class="pcard">
    <div class="phead">
      <div>
        <div class="ptitle"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></div>
      </div>
      <span class="daterange">{{ p.date | date: "%d %b %Y" }}</span>
    </div>
    {% if p.summary %}
      <p class="pdesc">{{ p.summary }}</p>
    {% endif %}
    <div class="plinks">
      <a class="btn" href="{{ p.url | relative_url }}">Read</a>
      <!-- {% if p.source_url %}
        <a class="btn" href="{{ p.source_url }}">Original</a>
      {% endif %} -->
    </div>
  </div>
{% endfor %}
</div>