let a=10
const b=20
var c=30

if(true){
    let a=10
    const b=20
    var c=30//scope problems
    console.log("inner:")
}

console.log(a)//will not print cause declared in block scope
console.log(b)//will not print cause declared in block scope
console.log(c)//30

function one(){
    const username ="gurman"
    function two(){              //two can access username from one
        const website="youtube"
        console.log(username)
    }
    // console.log(website)
    two()
}
one()

if (True){
    const username="gurman"
    if (username==="gurman"){
        const website="youtube"
        console.log(username+website);
    }
    console.log(website)
console.log(username)

}

// +++++++++++++++++++++++++++++++++++++++

console.log(addone(5))
function addone(num){
    return num+1
}

Hoisting
console.log(addtwo(5))
const addtwo=function(num){
    return num+2
}
