<?php

	require_once'db_connect.php';

    // connecting to db
    //$db = new DB_CONNECT();
$pressavailable=1;
$panchayat_id=1;$count=0;
   $officer_id=1;
if($pressavailable==1)
{
 date_default_timezone_set("Asia/Kolkata");
 $current_time =  date("Ha");
 echo $current_time;
 $sql2="select * from officeravailabilitydetails where panchayat_id='$panchayat_id' and officer_id='$officer_id'";
 $res2=mysql_query($sql2);
 $num2=mysql_num_rows($res2);
 if($num2)
 {
while($row2=mysql_fetch_array($res2))
{
 
   $sunrise=$row2['available_from'];
   $sunset=$row2['available_to'];
   echo $sunrise;echo $sunset;
//  $date2 = DateTime::createFromFormat('Ha', $sunrise);
//$date3 = DateTime::createFromFormat('Ha', $sunset);
if ($current_time > $sunrise && $current_time < $sunset)
{
  echo 'here';
  $count++;
}
else{echo 'hiiiiii';}
}
}
$date=date('y-m-d'); 
if($count==0){
$sql2="update officeravailabilitydetails set available_now=0 where panchayat_id='$panchayat_id' and officer_id='$officer_id' and date='$date'";
$res2=mysql_query($sql2);}
else
{$sql2="update officeravailabilitydetails set available_now=1 where panchayat_id='$panchayat_id' and officer_id='$officer_id' and date='$date'";
$res2=mysql_query($sql2);}
}
//$sunrise = "8 am";
//$sunset = "9 am";
//$date1 = DateTime::createFromFormat('Ha', $current_time);

?>