// //array-shallow copies(references)one value change result in other value changes

// const myArr=[0,1,2,3,4,5]
// console.log(myArr[0]) //0

// const myArr1=[1,2,3,4,5]
// console.log(myArr[1])

// // Array methods
// myArr.push(6)//atlast push element
// console.log(myArr)
// myArr.pop(6)// pop last element
// console.log(myArr)
// myArr.unshift(8)// add element at 1st and shifts rest elements right side
// console.log(myArr)
// myArr.shift() // removes 1st element and shifts elements left side
// console.log(myArr.includes(3))//includes is questionaire methods which give boolean result 

//slice
const x=[0,1,2,3,4,5,6]
console.log(x)
const a = x.slice(2,5)//slice index 2 to index 4(range)
console.log(a)
console.log(x)//doesnt affect previous array
const b = x.splice(1,3)//splice from idx(start,total)
console.log(b)
console.log(x)//affect previous array