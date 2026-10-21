const coding=["js","ruby","py"]

const values=coding.forEach((item)=>{
    console.log(item)
    return item//shows that for each loop does not return any values
})

console.log(values)

//to solve this problem

const myNums=[1,2,3,4,5,6,5,6,8,7,4444,61]

const ans=myNums.filter((num)=>num>4)
console.log(ans)

const new1=myNums.filter((num)=>{
    return num>10
})
console.log(new1)

//create array and print using push and if 
const arr=[]
myNums.forEach((num)=>{
    if(num>4){
        arr.push(num)
    }
})
console.log(arr)