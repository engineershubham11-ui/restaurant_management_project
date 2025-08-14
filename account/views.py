<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scaler=1" />
    <title> Homepage </title>
    <style>
    body {font-family: arial, sans-serif; margin; 0; padding: 0; background-colour: #f4f4f4; colour: #333; }
    header { background-colour: #333; colour: #fff; padding: 1rem; text-align: center; }
    main {max-width: 600px; margin: 2rem auto; background: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); }
    h1 { margin-bottom: 1rem; }
    p { margin: 0.5rem 0 ;}
    footer { text-align: center; padding: 1rem; background-color: #333; color: #fff; padding: 2rem; border-radius: 8px; box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1); }
    </style>
    </head>
    <body>
     <header>
       <h1> welcome to my restaurant </h1>
    </header>
    <main>
       <h2> About us </h2>
       <p><strong>phone:</strong> {{ phone number}}</p>
       <p> Delicious meals, cozy atomsphere, and friendly service.</p>
    </main>
    <footer>
    &copy; <span id="year"></span> my restaurant. all right reserved.
    </footer>
    <script>
    document.getElementByld('year').textcontent = new date().getFullYear();
    </script>
    </body>
    </html>
