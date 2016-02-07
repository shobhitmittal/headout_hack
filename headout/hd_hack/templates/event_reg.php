<?php
if (!empty($_POST)) {
session_start();
include 'db_connect.php';
date_default_timezone_set("Indian/Kerguelen");
$email=$_SESSION['email'];
$event_id=rand();
$event_name=mysql_real_escape_string($_POST['event_name']);
$event_desc=mysql_real_escape_string($_POST['event_desc']);
$event_location=mysql_real_escape_string($_POST['event_location']);
$event_start_date=mysql_real_escape_string($_POST['event_start_date']);
$event_end_date=mysql_real_escape_string($_POST['event_end_date']);
$event_created_at=date(DATE_RFC822);
$event_updated_at=date(DATE_RFC822);
$created_by_id=$email;
$updated_by_id=$email;
$delivery_boys=mysql_real_escape_string($_POST['delivery_boys']);
if(!isset($_SESSION['email']))
{
	  echo '<script type="text/javascript">alert("Please login to register!!"); window.history.back();</script>';	
}
else{
$query1="insert into hd_hack_event_table(event_id,event_name,event_desc,event_location,event_start_date,event_end_date,event_created_at,event_updated_at,created_by_id,updated_by_id,delivery_boys) values('$event_id','$event_name','$event_desc','$event_location','$event_start_date','$event_end_date','$event_created_at','$event_updated_at','$created_by_id','$updated_by_id','$delivery_boys')";
/*echo $event_name;
echo '<br/>';
echo $created_by_id;
echo '<br/>';
echo $event_id;
echo '<br/>';
echo $event_created_at;
echo '<br/>';
echo $event_start_date;
echo '<br/>';*/
$result2=mysql_query($query1);
}
if($result2)
echo '<script type="text/javascript">alert("Registration Successful! "); window.history.back();</script>';	
else
echo '<script type="text/javascript">alert("Registration UnSuccessful"); window.history.back();</script>';
 }
?>