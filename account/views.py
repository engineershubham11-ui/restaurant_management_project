<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title> Restaurant Homepage</title>
   <style>
    body {
       font-family:arial, helvetica, sans-serif;
       backgroung-color: #fafafa;
       color: #333;
       margin: 0;
       padding: 0;
     }
     header{
        backgroung-color: #8B0000,
        padding: 20px;
        text-align: center;
     }
     .logo{
        width:180px;
        height:auto;
     }
     h1{
        color: #8B0000;
        text-align:center
        margin-top: 30px;
     }
     p{
        font-size:18px;
        text-align: center;
        margin: 15px auto;
        max-width: 600px;
        line-height: 1.6;
     }
     main {
        padding:20px;
     }
     footer {
        backgroung-color:#333;
        color:white;
        text-align:center;
        padding: 10px;
        margin-top:40px;
     }

    </style>
</head>
<body>
    <header>
    <img src="{% static 'images/ logo.png' %}" alt="Restaurant Logo" class="logo">
    </header>

    <main>
    <p> Enjoy the finest dining experience!</p>
    </main>
         <footer>
         <p> 2025 our restaurant . all right reserved.</p>
        </footer>
 </body>
</html>