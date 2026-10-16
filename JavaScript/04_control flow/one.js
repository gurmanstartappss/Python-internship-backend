// if 
const temp=42
if (temp>40){     // condition true then only it enters block                  
    console.log("temp > 40 ")
} else {console.log("not greater than 40")}

console.log("temp recorded")


const balance=1000

if (balance<500){
    console.log("less than 500")
}else if (balance<900){      //else if
    console.log("less than 500")
}else{
    console.log("greater than 1000")
}


const userLoggedIn=true
const debitCard=true
const loggedInFromGoogle=false
const loggedInFromEmail=true

if(userLoggedIn && debitCard){//and all true
    console.log("allowed")
}
if(loggedInFromEmail || loggedInFromGoogle){//or 
    console.log("user logged in")
}