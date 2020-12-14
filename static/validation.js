function register_validate()
{
    var Username=document.getElementById("username");
    var password=document.getElementById("password");
    var repass=document.getElementById("confirm_password");
    var phno=document.getElementById("Contact");
    var email=document.getElementById("email");
    var city=document.getElementById("city");
    var address=document.getElementById("address");
    var regx=/^[6-9]\d{9}$/;
    var re =  /^\w+([\.-]?\w+)+@\w+([\.:]?\w+)+(\.[a-zA-Z0-9]{2,3})+$/;
    
    if(Username.value.trim()=="")
    {
    	alert("Username is Empty");
    	return false;
    }
    else if(email.value.trim()=="")
    {
        alert("Email is Empty");
        return false;
    }
    
    else if(!re.test(email.value.trim())){
    	alert("Please Enter a valid Email")
    	return false;
    }
    else if(password.value.trim()=="" || repass.value.trim()=="" )
    {
        alert("Password is Empty");
        return false;
    }
    else if(password.value.trim().length<5 || repass.value.trim().length<5)
    {
        alert("Password must be at least 5 characters");
        return false;
    }
    else if(password.value.trim()!=repass.value.trim())
    {
        alert("Password do not Match!");
        return false;
    }
    else if(!regx.test(phno.value.trim()))
    {
    	alert("Invalid Phone Number");
    	return false;
    }
    else if(city.value.trim()=="")
    {
    	alert("City is Empty");
    	return false;
    }
    else if (address.value.trim()=="")
    {
    	alert("Address is Empty");
    	return false;
    }

    else{
        return true;
    }
    
}






function change_password_validate(){
	var old_pass=document.getElementById("old_password");
	var new_pass=document.getElementById("new_password");
    var confirm_newpass=document.getElementById("confirm_new_password");
    
    if(old_pass.value.trim()=="" || new_pass.value.trim()=="" || confirm_newpass.value.trim()=="")
    {
    	alert("Password is Empty");
    	return false;
    }
    else if(new_pass.value.trim().length<5 || confirm_newpass.value.trim().length<5)
    {
    	alert("Password must be at least 5 characters");
        return false;
    }
    else if(new_pass.value.trim()!=confirm_newpass.value.trim())
    {
        alert("Password do not Match!");
        return false;
    }
    else{
        return true;
    }
}


function OrderValidate(){
	var mode=document.getElementByName("payment_mode")
	var contact=document.getElementById("contact_no");
	var address=document.getElementById("delivery_address")
	var regx=/^[6-9]\d{9}$/;
	if(mode.value()==""){
		alert("Please select Payment Mode");
    	return false;
	}
	else if(!regx.test(contact.value.trim()))
    {
    	alert("Invalid Phone Number");
    	return false;
    }
	else if(address.value.trim()==""){
		alert("Please enter the address");
    	return false;
	}
	else{
		return true;
	}
}