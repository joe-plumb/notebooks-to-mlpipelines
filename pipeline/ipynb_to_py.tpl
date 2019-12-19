
{% extends 'python.tpl'%}

## remove header
{% block header -%}
{% endblock header %}

## remove markdown cells
{% block markdowncell -%}
{% endblock markdowncell %}

## change the appearance of execution count
{% block in_prompt %}
{%- endblock in_prompt %}
