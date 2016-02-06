//Validation of company and student registration
function validateform1()
{
		reg= /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/;
		phoneno=/^[789][0-9]{9}$/;
		x2=document.forms["officer-form"]["email"].value;
		
		if(!reg.test(x2) && !phoneno.test(x2))
		{
		alert("Not a valid email or Not a Valid Phone number");
		return false;
		}
		var x="";
		x=document.forms["officer-form"]["password"].value;
		regex=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/;
		if(!regex.test(x))
		{
		alert("Password should contain minimum 6 characters-atleast 1 Lowercase, 1 Uppercase, 1 Number");
		return false;
		}
}
function validateform2()
{
			var x8=document.forms["regform"]["phone"].value;
			reg= /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,3})$/;
			x2=document.forms["regform"]["email"].value;
			if(!reg.test(x2))
			{
			alert("Not a valid email");
			return false;
			}
			phoneno=/^[789][0-9]{9}$/;
			  
			  if(!phoneno.test(x8))  
					{  
				  alert("Not a valid phone number");
			return false;
					}  
					
			var x="";
			x=document.forms["regform"]["password"].value;
			var x1=document.forms["regform"]["password1"].value;
			regex=/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$/;
			if(!regex.test(x))
			{
			alert("Password should contain minimum 6 characters-atleast 1 Lowercase, 1 Uppercase, 1 Number");
			return false;
			}
			/*if(x!=x1)
			{
			alert("Password doesn't match");
			return false;
			}*/
}			
$(window).load(function(){$(".sarathy").fadeOut("slow");});

