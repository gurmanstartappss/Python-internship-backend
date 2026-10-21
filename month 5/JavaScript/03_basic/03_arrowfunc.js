// this keyword and arrow function
// // if want to refer current context in a scope we use this keyword to access variables
// arrow func does not have this keyword

const user={
    username:"gurman",
    price:999,
    welcome:function(){
        console.log(`${this.username},welcome to website`)
        console.log(this)
    }
}

// user.welcome()
// user.username="sam"//sam is context which changed
// user.welcome()


// const chai=()=>{
//     let username="gurman"
//     console.log(this);
// }
// chai()

const addtwo=(num1,num2)=>{  //basic arrow func
    return num1+num2
}
const addthree=(num1,num2)=>num1+num2 // implicit return(no parenthesis/return)

const addfour=(num1,num2)=>(num1+num2)// () used for returning objects
const addfive=(num1,num2)=>({username:"gurman"})// () used for returning objects
console.log(addthree(5,6))
console.log(addfour(5,6))
console.log(addfive(5,6))


console.log(addtwo(3,4))

