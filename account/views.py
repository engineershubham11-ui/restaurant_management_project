{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>{% block title %}my Restaurant{% endblock %}</title>
   <style>
   body{
    margin: 0;
    font-family: Arial, sans-serif;
    display:flex;
    Flex-direction: column;
    min-height: 100vh;
   }

main{
    flex: 1;
    padding: 20px;
}

footer{
    backgroung-colour: #333;
    colours: white;
    text-align: center;
    padding: 12px;
    margin-top: auto;
}

</style>
</head>
<body>
   <header>
       {% block header %}{% endblock %}
    </header>

    <main>
    {% block content % }{% endblock %}
    </main>

    <footer>
    <p> {% now "Y" %}my Restaurant. All right reserverd.</p>
    </footer>

</body>
<html>
