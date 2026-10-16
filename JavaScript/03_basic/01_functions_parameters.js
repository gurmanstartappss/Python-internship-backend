
function sayMyName(){
    console.log("G")
    console.log("U")
    console.log("R")
    console.log("M")
    console.log("A")
    console.log("N")
}

sayMyName//reference
sayMyName()//execution

function addTwoNumbers(num1,num2){//parameters
    console.log(num1 + num2)//doent mean value is returning, only printed
}

addTwoNumbers(2,4)//arguments
addTwoNumbers(2,"4")//concat

//1st way
function addTwoNumbers(num1,num2){//parameters
    let result=num1 + num2
    return result           //now it will return result
}
//2nd way
function addTwoNumbers(num1,num2){//parameters
    return num1 + num2//now it will return result
}

//now
function loginuser(username="sam"){
    if (!username){      //or (username===undefined)
        return"please enter a username"
        
    }
    return `hello ${username}, welcome back`
}
console.log(loginuser("gurman"))//if argument is empty then default parameters replace it

function cal(va1,va2,...num1){//rest and spread operator depending on situation
    return num1
}
console.log(cal(200,300,400,500))

const user ={
    username:"hitesh",
    price:199
}
function handleObject(anyobject){
    console.log(`username is ${anyobject.username} price is ${anyobject.price} `)
}

handleObject(user)
handleObject({
    username:"sam",
    price:339
})

const myNewArray=[200,300,400,500]
function returnSecondValue(getArray){
    return getArray[1]
}

//console.log(returnSecondValue)