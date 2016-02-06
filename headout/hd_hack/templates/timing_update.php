 <?php
 session_start();

if (!empty($_POST)) {
  include 'db_connect.php';
     $email=$_SESSION['email'];
$query="select * from officerdetails where email='$email'";
$result=mysql_query($query);
$num=mysql_num_rows($result);
 if($num)
 {
while($row=mysql_fetch_array($result))
{
  $panchayat_id=$row["panchayat_id"];
  $officer_id=$row["officer_id"];
}
 }
//$multiple=mysql_real_escape_string($_POST['multiple[]']);
//$sql = array();
 
//foreach( $data as $row ) {
  //  $multiple[] = '("'.mysql_real_escape_string($row['text']).'", '.$row['available_from'].')';
//}
//mysql_query('INSERT INTO officeravailabilitydetails (text, category) VALUES '.implode(',', $sql));

//$multiple[]=mysql_real_escape_string($_POST['multiple']);
//$multiple1[]=mysql_real_escape_string($_POST['multiple1']);
//$multiple2[]=mysql_real_escape_string($_POST['multiple2']);
//$multiple3[]=mysql_real_escape_string($_POST['multiple3']);

//$multiple[] = implode(' ', $_POST['multiple']) . implode(' ', $_POST['multiple1']);
$multiple = implode(' ', $_POST['multiple']); 
       $myArray = explode(' ', $multiple);
$multiple1 = implode(' ', $_POST['multiple1']); 
 $myArray1 = explode(' ', $multiple1);
$multiple2 = implode(' ', $_POST['multiple2']); 
 $myArray2 = explode(' ', $multiple2);
$multiple3 = implode(' ', $_POST['multiple3']); 
 $myArray3 = explode(' ', $multiple3);
//$multiple1[] = 
//echo count($multiple);
for($i=0;$i<count($myArray);$i++)
{
	///$multiple[$i]=$multiple[$i] . $multiple1[$i];
	$myArray[$i]= $myArray[$i].$myArray1[$i];
	//echo "<br/>";
	$myArray2[$i] = $myArray2[$i].$myArray3[$i];
	

  //  echo '<br/>';
}
$date=date('y-m-d'); 

echo $date;
for($i=0;$i<count($myArray);$i++)
{
		$query1="insert into officeravailabilitydetails(panchayat_id,officer_id,date,available_from,available_to) values('$panchayat_id','$officer_id','$date','$myArray[$i]','$myArray2[$i]')";
		$result2=mysql_query($query1);
}
		//$num=mysql_num_rows($result2);
		if($result2)
		//	echo "Reg success!!!";
			echo '<script type="text/javascript">alert("Updated Successful"); window.history.back();</script>';
		else
		echo  '<script type="text/javascript">alert("Updated UnSuccessful"); window.history.back();</script>';

}
?>