<?php       
  
    include('connection.php');  


    $uusername = mysqli_real_escape_string($conn, $_POST['uusername']);
    $upassword = mysqli_real_escape_string($conn, $_POST['upassword']);

    $login_query = "SELECT * FROM users WHERE username='$uusername' AND password='$upassword'";
    $login_query_run = mysqli_query($conn, $login_query);

   if(mysqli_num_rows($login_query_run) > 0)
   {

    header("location: index.html");

   }
   else
   {
    ?>
    <script>
    alert("Invalid Username Or Password");
    </script>
    <?php
    header('Location: login.html');
    
    
   }

    ?>
