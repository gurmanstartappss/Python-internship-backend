const a =[1,2,3,4,5]
const b =[6,7,8,9,10]

c=a.concat(b)//concat method-to add 1 array
console.log(c)

const d=[...a,...b]//spread method-spread out elements
console.log(d)

const main=[1,2,3,[4,5,6],7,[8,[9,10]]]//when arrays have depth
const real=main.flat(Infinity)
console.log(real)

console.log(Array.from("gurman"))//created an array
console.log(Array.isArray("gurman"))//asking if array there? used for data scraping 
console.log(Array.from({name:"gurman"}))//[] creates blank array


let score1=100 
let score2=200 
let score3=300 

console.log(Array.of(score1,score2,score3))