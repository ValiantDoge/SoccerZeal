<?php      
    include('connection.php');  
    $u_fname = $_POST['ufname'];
    $u_lname = $_POST['ulname'];
    $u_username = $_POST['uusername'];
    $u_password = $_POST['upassword'];
  

  
    $sql = "INSERT INTO users ()
            VALUES ('$u_fname', '$u_lname', '$u_username', '$u_password')";


    if(mysqli_query($conn,$sql)){
      // Records created successfully. Redirect to landing page
      header("location: login.html");
      exit();
  } else{
      echo "Oops! Something went wrong. Please try again later.";
  }

    ?>