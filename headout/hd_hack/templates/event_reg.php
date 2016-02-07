<?php
if (!empty($_POST)) {

include 'db_connect.php';
date_default_timezone_set("Indian/Kerguelen");
$user_iden=rand();
$f_name=mysql_real_escape_string($_POST['f_name']);
$l_name=mysql_real_escape_string($_POST['l_name']);
$email=mysql_real_escape_string($_POST['email']);
$phone=mysql_real_escape_string($_POST['phone']);  
$password=mysql_real_escape_string($_POST['password']);
$created_at=date(DATE_RFC822);
$updated_at=date(DATE_RFC822);
$query4="select * from hd_hack_user_table where email='$email'";
$result9=mysql_query($query4);
$num=mysql_num_rows($result9);

if($num!=0)
{
	  echo '<script type="text/javascript">alert("Already registered!!"); window.history.back();</script>';	
}
else{
$query1="insert into hd_hack_user_table(user_iden,f_name,l_name,email,phone,password,created_at,updated_at) values('$user_iden','$f_name','$l_name','$email','$phone','$password','$created_at', '$updated_at')";
$result2=mysql_query($query1);
}
if($result2)
echo '<script type="text/javascript">alert("Registration Successful! "); window.history.back();</script>';	
else
echo '<script type="text/javascript">alert("Registration UnSuccessful"); window.history.back();</script>';
 }
?>