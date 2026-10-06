const a=100000.31544 //implicitly or automatically defined
const b=new Number(300) //explicitly define

console.log(a)//100
console.log(b)//300

//methods

console.log(a.toString().length) //3c
console.log(a.toFixed(1)) // 100.3
console.log(a.toPrecision(6)) // 100000.
console.log(a.toLocaleString('en-IN'))//commas acc to indian values


// ----------maths lib--------------
console.log(Math)//Object [Math]{properties}
console.log(Math.abs(-4))//absolute
console.log(Math.round(4.6))//round

console.log(Math.random());//random values
console.log(Math.floor(Math.random()*10)+1);

const min=10
const max=20

console.log(Math.floor(Math.random() *(max-min+1))+min)