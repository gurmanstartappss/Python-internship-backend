// reduce used in shopping carts
const myNums=[1,2,3]

// const myTotal=myNums.reduce(function(acc,currval){
//     console.log(`acc=${acc} and currval=${currval}`)
//     return acc + currval
// },0)

// console.log(myTotal)

// const myTotal=myNums.reduce((acc,currval)=>acc+currval,0)
// console.log(myTotal)

//shopping cart
const shoppingCart=[
    {
        itemname:"js course",
        price:3999
    },
    {
        itemname:"mobile dev",
        price:2999
    },
    {
        itemname:"python dev",
        price:7999
    },
    {
        itemname:"data science",
        price:12999
    },
]
const priceToPay=shoppingCart.reduce((acc,item)=>(acc+item.price),0)
console.log(priceToPay)