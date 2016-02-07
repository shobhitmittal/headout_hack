<?php session_start();
?>
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
	    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="description" content="Invite"/>
		<meta name="author" href="https://www.facebook.com/thillaivasan.sanjay"/>
        <meta name="author" content="sanjay thillaivasan"/>
		<meta name="keywords" content="Invite"/>
		<link rel="shortcut icon" href="css/favicon.png" />
		<link rel="apple-touch-icon" href="css/apple-touch-icon.png" /><!--57*57-->

        <?php include 'cssFiles.php'?>
        
        <title>Invite </title>
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
	
         <?php include 'jsFiles.php'?>
       
         </head>
    <body id="page-top" ng-app="SanjayApp" data-spy="scroll" data-target=".navbar-fixed-top">
        <div class="sarathy"></div>
		<!-- Loader 7 -->

<!--svg version="1.1" id="L7" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
  viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve">
 <path fill="#fff" d="M31.6,3.5C5.9,13.6-6.6,42.7,3.5,68.4c10.1,25.7,39.2,38.3,64.9,28.1l-3.1-7.9c-21.3,8.4-45.4-2-53.8-23.3
  c-8.4-21.3,2-45.4,23.3-53.8L31.6,3.5z">
      <animateTransform 
         attributeName="transform" 
         attributeType="XML" 
         type="rotate"
         dur="2s" 
         from="0 50 50"
         to="360 50 50" 
         repeatCount="indefinite" />
  </path>
 <path fill="#fff" d="M42.3,39.6c5.7-4.3,13.9-3.1,18.1,2.7c4.3,5.7,3.1,13.9-2.7,18.1l4.1,5.5c8.8-6.5,10.6-19,4.1-27.7
  c-6.5-8.8-19-10.6-27.7-4.1L42.3,39.6z">
      <animateTransform 
         attributeName="transform" 
         attributeType="XML" 
         type="rotate"
         dur="1s" 
         from="0 50 50"
         to="-360 50 50" 
         repeatCount="indefinite" />
  </path>
 <path fill="#fff" d="M82,35.7C74.1,18,53.4,10.1,35.7,18S10.1,46.6,18,64.3l7.6-3.4c-6-13.5,0-29.3,13.5-35.3s29.3,0,35.3,13.5
  L82,35.7z">
      <animateTransform 
         attributeName="transform" 
         attributeType="XML" 
         type="rotate"
         dur="2s" 
         from="0 50 50"
         to="360 50 50" 
         repeatCount="indefinite" />
  </path>
</svg-->
                    
 <!-- Navigation -->
    <nav class="navbar navbar-custom navbar-fixed-top" role="navigation">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-main-collapse">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand page-scroll" href="#page-top">
				<!--img src="css/dots1.png"  style="width:11%;float:left;padding-right:5px"/-->
                     <span class="light .heading-font" style="padding-left:5px;color:#FFF;"><i class="fa fa-map-marker fa-lg"></i><i>&nbsp;Invite</i></span> 
                </a>
            </div>

            
            <div class="collapse navbar-collapse navbar-right navbar-main-collapse">
                <ul class="nav navbar-nav">
                   
                    <!--li class="hidden">
                        <a href="#page-top"></a>
                    </li-->
                    <li>
                        <a class="page-scroll" href="#page-top"><i class="fa fa-home fa-lg"></i>&nbsp; HOME</a>
                    </li>
                    <li>
                        <a class="page-scroll" href="#about"><i class="fa fa-cloud fa-lg"></i>&nbsp; ABOUT</a>
                    </li>
					
						<?php
		 if(isset($_SESSION['email']))
			{ 
		echo '<li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><i class="fa fa-laptop fa-lg"></i>&nbsp; EVENTS <span class="caret"></span></a>
          <ul class="dropdown-menu">
		   <li><a href="#eventreg" class="logoutHover blacktext page-scroll"><i class="fa fa-clock-o fa-lg"></i>&nbsp;EVENT REGISTRATION</a></li>
            <li><a href="logout-script.php" class="logoutHover"><i class="fa fa-power-off fa-lg"></i>&nbsp; Logout</a></li>
          </ul>
        </li>';
					
			}
			else{
				echo '<li>
                        <a class="page-scroll" href="#login"><i class="fa fa-bell-o fa-lg"></i>&nbsp; USER LOGIN</a>
                    </li>
					<li>
                        <a class="page-scroll" href="#signup"><i class="fa fa-eye fa-lg"></i>&nbsp; USER SIGNUP</a>
                    </li>';
			}
			?>
					<!--li>
                        <a class="page-scroll" href="#eventreg"><i class="fa fa-coffee fa-lg"></i>&nbsp; EVENT REGISTRATION</a>
                    </li-->
				
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>
	
 <header id="myCarousel" class="carousel slide">
       

      
        <div class="carousel-inner">
            <div class="item active">
                <div class="fill" style="background-image:url('css/bg.jpg');"></div>
                  <div class="captionText carousel-caption">
                    <h3>
					Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.</h3>
                </div>
            </div>
           
          
        </div>

      

    </header>


	<section id="about" class="text-center">
	<div class="jumbotronAbout container">
	 <div class="row">
                <div class="col-md-4 col-md-offset-4 text-center">
                    <h2 class='heading-font'>About</h2>
                    <hr class="heading-line">
                </div>
            </div>
	<p class="AboutClass">	  
		Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
	</p>
	</div>
	</section>
<?php
		 if(!isset($_SESSION['email']))
			{ 
		echo '
				<section id="login">
<div class="container">
    	<div class="row">
			<div class="col-md-6 col-md-offset-3">
				<div class="">
					<div class="panel-heading">
						<div class="row">
							<div class="col-xs-12">
							<h3 class="loginTitle"><a href="#" class="active" id="student-form-link">User Login</a> </h3>
							</div>
							
						</div>
						<hr>
					</div>
					<div class="panel-body">
						<div class="row">
							<div class="col-lg-12 box">
								<form id="officer-form" name="officer-form" action="login.php" method="post" role="form" style="display: block;" onsubmit="return validateform1()">
									<div class="form-group">
										<input type="text" name="email" id="email" tabindex="1" class="form-control" placeholder="Email Address/Phone Number" required>
									</div>
									
									<div class="form-group">
										<input type="password" name="password" id="password" tabindex="2" class="form-control" placeholder="Password" required>
									</div>
								
									<div class="form-group">
										<div class="row">
											<div class="col-sm-6 col-sm-offset-3">
												<input type="submit" name="login-submit" id="login-submit" tabindex="4" class="form-control btn btn-lg btn-primary btn-block btn-signin loginButton" value="Log In">
											</div>
										</div>
									</div>
									<div class="form-group text-center">
										
										<a href="#signup"> <label for="signup"> Dont have an account? Sign up</a>
										</label>
									</div>
								</form>
							
									
									
								
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
			
	</section>
	
	 	<section class="signup">
<center><h3><!--font face="arial" size="5px" color="black" class="login">Signup</font--></h3>
 <form id="regform" name="regform" class="form-horizontal" role="form" method="post" action="" onsubmit="return validateform2()">
<div class="container">    
        <div id="signup" style="margin-top:30px; margin-left:200px;" class="mainbox col-md-8 col-md-offset-3 col-sm-10 col-sm-offset-2">                    
            <div class="panel panel-info" >
                    <div class="panel-heading">
                        <div class="panel-title"><center>User Signup</center></div>
                    </div>     

                    <div style="padding-top:0px; box-shadow: 5px 5px 5px #888888;" class="panel-body" >

                        <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>
						<br>
            
						<div class="form-group"> 
              
  <label for="firstname" class="col-sm-2 control-label">First Name<span style="color:red;font-size:20px;"> *</span>:</label>   
  <div class="col-sm-10">       
  <input type="text" class="form-control" id="f_name" name="f_name"             placeholder="Enter Your First Name" required>       </div>   
   </div>      
						<div class="form-group"> 
              
  <label for="firstname" class="col-sm-2 control-label">Last Name<span style="color:red;font-size:20px;"> *</span>:</label>   
  <div class="col-sm-10">       
  <input type="text" class="form-control" id="l_name" name="l_name"             placeholder="Enter Your Last Name" required>       </div>   
   </div>      
  <div class="form-group">    
  <label for="email" class="col-sm-2 control-label">E-mail<span style="color:red;font-size:20px;"> *</span>:</label>      
  <div class="col-sm-10">          
  <input type="email" class="form-control" id="email"      name="email"         placeholder="Enter mail id" required>       </div>    </div>   
  <div class="form-group">    
  <label for="phoneno" class="col-sm-2 control-label">Phone no <span style="color:red;font-size:20px;"> *</span>:</label>      
  <div class="col-sm-10">          
  <input type="number" class="form-control" id="phone" name="phone"  placeholder="Enter Phone number" required> </div>    </div>   
    
   <div class="form-group">    
  <label for="pwd" class="col-sm-2 control-label">Password <span style="color:red;font-size:20px;"> *</span>:</label>      
  <div class="col-sm-10">          
  <input type="password" class="form-control" id="password"          name="password"     placeholder="Enter Your Password" required>       </div>    </div>   
  
  <div class="form-group">    
  <label for="pwd" class="col-sm-2 control-label">Confirm Password<span style="color:red;font-size:25px;"> *</span>:</label>      
  <div class="col-sm-10">          
  <input type="password" class="form-control" id="password1"          name="password1"     placeholder="Confirm Your Password" required>       </div>    </div> 

					 <div class="col-sm-12 controls">
            <!--input type="submit" id="btn-login" -->
                                      <button id="btn-login"  class="btn btn-success" id="simplepost" >Register </button>

  </form>
  
  
	</section>

			';}
			?>
	<?php
		 if(isset($_SESSION['email']))
			{ 
		echo '		
	 	<section id="eventreg">
<center><h3><!--font face="arial" size="5px" color="black" class="login">Signup</font--></h3>
 <form id="eventregform" name="eventregform" class="form-horizontal" role="form" method="post" action="event_reg.php">
<div class="container">    
        <div id="signup" style="margin-top:30px; margin-left:200px;" class="mainbox col-md-8 col-md-offset-3 col-sm-10 col-sm-offset-2">                    
            <div class="panel panel-info" >
                    <div class="panel-heading">
                        <div class="panel-title"><center>Event Registration</center></div>
                    </div>     

                    <div style="padding-top:0px; box-shadow: 5px 5px 5px #888888;" class="panel-body" >

                        <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>
						<br>
           
						<div class="form-group"> 
              
  <label for="firstname" class="col-sm-2 control-label">Event name</label>   
  <div class="col-sm-10">       
  <input type="text" class="form-control" id="event_name" name="event_name"   placeholder="Event Name" required>       </div>   
   </div>      
  <div class="form-group">    
  <label for="event_desc" class="col-sm-2 control-label">Event Description</label>      
  <div class="col-sm-10">          
  <input type="text" class="form-control" id="event_desc"      name="event_desc"         placeholder="Event description" required>       </div>    </div>   
  <div class="form-group">    
  <label for="event_location" class="col-sm-2 control-label">Event location </label>      
  <div class="col-sm-10">          
  <input type="text" class="form-control" id="event_location" name="event_location"  placeholder="Event location" required> </div>    </div>   
    <div class="form-group">    
  <label for="event_start_date" class="col-sm-2 control-label">Event start date</label>      
  <div class="col-sm-10">          
  <input type="text" class="form-control" id="event_start_date"  name="event_start_date"     placeholder="Event start date" required>       </div>    </div> 
    <div class="form-group">    
  <label for="event_end_date" class="col-sm-2 control-label">Event End Date</label>      
  <div class="col-sm-10">          
  <input type="text" class="form-control" id="event_end_date"  name="event_end_date"     placeholder="Event end date" required>       </div>    </div> 
  

					 <div class="col-sm-12 controls">
            <!--input type="submit" id="btn-login" -->
                                      <button id="btn-login"  class="btn btn-success" id="simplepost"> SUBMIT </button>

  </form>
  
  
	</section>
			';
			}?>

   <!--script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.0.7/angular.min.js"></script-->

<script>
$("#simplepost").click(function(e)
{
/*var MyForm = $("#regform").serializeJSON();*/
var data = $('#regform').serialize();
console.log(MyForm);
 $.ajax(
 {
 url : "http://128.199.83.81:8080/user_req_html/",
 type: "POST",
 /*data : {valArray:MyForm},*/
 /*data : MyForm,*/
 /*data:data,*/
 /*data: JSON.stringify(data),*/
 /*data:{'f_name':'test_user','l_name':'test','email':'dfndsus@gmail.com','phone':'81912818778','password':'dfsdsd'},*/
  data:{'code': '202'},
  dataType: "json",
  contentType : "application/json",
  async:false,
  
 success:function(maindta)
 {
alert(maindta);
 },
 error: function(jqXHR, textStatus, errorThrown)
 {
 }
 });
 e.preventDefault(); //STOP default action
});

 ./* function submitform(){
var formData = JSON.stringify($("#regform").serializeArray());
$.ajax({
  type: "POST",
  url: "128.199.83.81:8080/user_reg/",
  data: formData,
  success: function(){},
  dataType: "json",
  contentType : "application/json"
});
  }*/
  
  
</script>
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
</body>
</html>