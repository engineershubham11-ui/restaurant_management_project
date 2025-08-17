{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title>{% block title %}My Restaruant {% endblock %}</title>
   <style>
    
    body{
        font-family: Arial, Helvetica, sans-serif;
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }
      
        main{
            flex: 1;
            padding:20px;
        }

        footer{
            background-colour: #333;
            colour: whitel;
            text-align: center;
            padding: 15px;
            margin-top: auto;
        }

        .hours{
            margin-top: 5px;
            font-size: 14px;
            colour: #ddd;
        }


    </style>
</head>
<body>
    <header>
        {%block header %} {% endblock %}
    </header>

    <main>
        {% block content %} {% endblock %}
    </main>

    <footer>
       <p> {% now "Y" %}my restaurant. All right reserved.</p>
       <p> class="hours">Opeaning Hours: mon-Fri: 11am - 9am | sat-sun: 10am - 10pm</p>
    </footer>
    
 </body>
</html>
