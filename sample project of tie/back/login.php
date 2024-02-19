<!DOCTYPE html>
<html>
    <head>
        <title>Login</title>
        <link rel="stylesheet" href="main.css">
    </head>
    <body>
        <form method="post" action="login.php">
          <h1>Login</h1>
          <div class="textBoxdiv">
             <input type="text" placeholder="username">
             </div>
             <div class="textBoxdiv">
                <input type="password" placeholder="password">
            </div>
            <input type="submit" value="Login" class="loginBtn">
            <div class="signup">
                Don't have an account ?
               </br>
               <a href="#">signup</a>
            </div>
            
            
        </form>
    </body>
    </html>
<?php
$conn = mysqli_connect("localhost","root","");
if(isset($_POST['login_Btn'])){
    $username=$_POST['username'];
    $password=$_POST['password'];
    $sql= "SELECT * FROM websitelogin.logindetails WHERE username = '$username'";
    $result = mysqli_query($cann,$sql);
    while($row = mysqli_fetch_assoc($result)){
        $resultPassword = $row['password'];
        if($password == $resultPassword){
            header('Location:index.html');
        }
        else{
            echo "<script>
              alert('Location unsuccessful');
            </script>";
        }
    }
}