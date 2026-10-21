// loops directly added to properties of array
const coding=["js","ruby","py"]

coding.forEach(function (value){//callback function
    console.log(value)

})

coding.forEach((value)=>{//arrow function
    console.log(value)
})

function printMe(item){
    console.log(item)
}

coding.forEach(printMe)

//=======================================
const myCoding=[
    {
        language:"js",
        filename:"hello"
    },
    {
        language:"py",
        filename:"hi"
    },
    {
        language:"txt",
        filename:"yo"
    }
]

myCoding.forEach((item=>{
    console.log(item.filename)
}))//array>object>value