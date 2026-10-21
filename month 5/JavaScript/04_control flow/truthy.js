// const userEmail="garg@gmail.com"

// if(userEmail){
//     console.log("got user email")
// }else{
//     console.log("dont have user email")
// }

// falsy values
// false,0,-0,BigInt 0n,"",null, undefined,NaN

//truthy values
// "0", "false","",{},[],Function(){}
// if (userEmail.legth===0){
//     console.log(array is empty)
// }

// const emptyObj={}
// if(Object.keys(emptyObj),length===0){
//     console.log("object is empty");
// }

//Nullish coalescing operator(??): null undefined
let val1;
val1=5??10 //5 value will be assigned
val1=null??10 // 10
val1=undefined??15 // 15
val1=null??10??20 // 10 
console.log(val1)

//Terniary Operator

// syntax=======condition ? true : false

const ice=200
ice>=80 ? console.log("hi") : console.log("yo")