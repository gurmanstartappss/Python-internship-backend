// JavaScript is a dynamically typed language.
// The data type is determined at runtime based on the value.
// A variable can hold values of different types during its lifetime.

// ==================== PRIMITIVE ====================
// 7 primitive types:
// String, Number, Boolean, null, undefined, Symbol, BigInt

const score = 100                  // Number
const scoreValue = 100.3           // Number
const isLoggedIn = false            // Boolean
const outsideTemp = null            // null
let userEmail = undefined           // undefined

const id = Symbol('123')
const id2 = Symbol('123')

console.log(id == id2)              // false
// Each Symbol is unique, even with the same description.

const bigNumber = 561651616465n     // BigInt


// ================= NON-PRIMITIVE =================
// Also called Reference types.
//
// Arrays
// Objects
// Functions

// Array
const heroes = ["shaktiman", "ironman", "hulk"]

// Object
const myobj = {
    name: "gurman",
    age: 23
}

// Function
const myFunction = function() {
    console.log("hello")
}


// ================= typeof =================

console.log(typeof myFunction)      // "function"

// stack=(primitive) copy
// heap=(non primitive) reference

let my="gurman"
let hi=my
hi="garg"

console.log(hi) ;//garg
console.log(my); //gurman


let user1={
    email:"gurman"
}
let user2=user1
user2.email="garggurman"//reference(heap)

console.log(user1)
console.log(user2)