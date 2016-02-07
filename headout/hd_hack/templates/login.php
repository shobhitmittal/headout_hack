<?php 
if (!empty($_POST)) {

session_start();
include 'db_connect.php';
$email=mysql_real_escape_string($_POST['email']);
$password=mysql_real_escape_string($_POST['password']);  

$query4="select * from officerdetails where email='$email' and password='$password'";
$result9=mysql_query($query4);
//$num=mysql_num_rows($result9);
while($row=mysql_fetch_array($result9))
{
$name=$row["first_name"];
}
if($result9)
{
	
	$_SESSION['email']=$email;
//	$_SESSION['name']=$name;
	
	echo '<script type="text/javascript">alert("Login Successful! "); window.history.back();</script>';	
}
else
{
	echo '<script type="text/javascript">alert("Login UnSuccessful ! Please Register"); window.history.back();</script>';
}
}
?>