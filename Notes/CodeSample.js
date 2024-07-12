<p>Name: <input type="text" ng-model="name"></p>
<p ng-bind="name"></p>
{% verbatim %}
Name: {{ name }}  
{% endverbatim %}

======


{% if user.is_authenticated %}
<li>Welcome {{ user.username }}</li>
{% endif %}

=====

<form action="{% url 'logout' %}" method="post">
  {% csrf_token %}
  <button type="submit">Log Out</button>
</form>

======