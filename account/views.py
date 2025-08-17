{% extend "base.html" %}

{% block title % }Home  -  my restaurant{% endblock %}

{% block content %}
     <h2> welcome to my restaurant </h2>
     <p> Enjoy the finest dining experience with us!</p>


     <form method="get" action="#">
     <input type ="text" name="q" placeholder="search menu items..." style="padding:8px; width:250px">
     <button type= "submit" style="padding:8px;">search</button>
    </form>

{% endblock %}