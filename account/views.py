<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <title> contact us </title>
   <script>
    
    function validateForm(){
        let name = document.forms["contactForm"]["name"].value;
        let email = document.Forms["contactForm"]["email"].value;

        if (name ==="" || email === ""){
            alert("please fill in both name and Email fields.");
            return false; 
        }
        return true;
    }

    </script>
</head>
<body>
     <h2> contact us </h2>
     <from name="contactForm" onsubmit="return validateFrom()">
     <label for="name">Name:</label><br>
     <imput type="text" id="name" name="name"><br><br>

     label for="email">Email:</label><br>
     <input type="email" id="email" name="email"><br><br>

     <label for="message">Message:</label><br>
     <textarea id="message" name="message"></textarea><br><br>

     <button type="submit">submit</button>
   
        </form>
 </body>
</html>
