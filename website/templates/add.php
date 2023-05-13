<?php
//include('config.php');
$servername="localhost";
$username="root";
$password="";
$dbname="proj";
     
      $name = $_POST['name'];
      $phone=$_POST['phone'];
      $subject = $_POST['subject'];
      $email = $_POST['email'];
      $message = $_POST['message'];
  
      $conn=new mysqli($servername,$username,$password,$dbname);

      if($conn->connect_error)
      {die("connection failed:".conn->connect_error);}

      $query="INSERT INTO form (id,name,phone,subject,email,message) VALUES ('','$name','$phone','$subject','$email','$message')";
     // $exec= mysqli_query($connection,$query);
      //if($exec){
       // $msg="Data was created sucessfully";
       // return $msg;

       if($conn->query($query)==TRUE)
       {
        
        
        header(Location: "index.html");
      }
      
      
      else{
        echo"error".$sql."</br>".$conn->error;}
        $conn->close();
      //  $msg= "Error: " . $query . "<br>" . mysqli_error($connection);
      


?>