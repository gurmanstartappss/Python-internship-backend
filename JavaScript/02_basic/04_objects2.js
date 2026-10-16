const tinderuser=new Object()
const tinderuser1={}          //both are same

console.log(tinderuser)

const regularuser={
    email:"garg@gmail.com",
    fullname:{
        firstname:"gurman",
        lastname:"garg",
    }
}
console.log(regularuser.fullname.firstname)

const obj1={1:"a",2:"b"}
const obj2={3:"c",4:"d"}

const result={obj1,obj2}//array in a arry problem
const result2=Object.assign({},obj1,obj2)//correct way and {}optional parameter
// or use spread operator
const result3={...obj1, ...obj2}
console.log(result)
console.log(result2)
console.log(result3)

//database values
const users=[
    {
        id:1,
        email:"g@gmai.com"
    },
    {
        id:1,
        email:"g@gmai.com"
    },
    {
        id:1,
        email:"g@gmai.com"
    },
]

console.log(users[1].email)
console.log(tinderuser)
console.log(Object.keys(tinderuser))
console.log(Object.values(tinderuser))
console.log(tinderuser.hasOwnProperty('isLoggedIn'))

//objects destructuring (in react)
const course={
    coursename:"js",
    price:999,
    teacher:"gurman"
}
// syntactical(destructure and also change name)
const{coursename:name}=course//from where value extract
console.log(name)

// react meth
const navbar =({company})=>{//instead of props.company for destructuring

}
navbar(company="gurman")

