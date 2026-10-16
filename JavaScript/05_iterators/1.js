//for loop
for (let index = 0; index < 10;index ++) {
    const element = index
    // console.log(element)
}

//tables
for (let i = 1; i <= 10; i++) {
    // console.log(`table of: ${i}`);
    for (let j = 1; j <= 10; j++) {   
    // console.log(`inner loop value : ${j} and inner loop  ${i}`)
        // console.log(i + '*'+j+'='+i*j);
}
}    

let myArray=["flash", "batman","superman"]
for (let i = 0; i < myArray.length; i++) {
    const element = myArray[i];
    // console.log(element)}
}
for (let index = 1; index <= 20; index++) {
    if (index==5) {
        // console.log("detected 5")
        break
    }
    // console.log(`value of i is ${index}`)    
}
for (let index = 1; index <= 20; index++) {
    if (index==5) {
        // console.log("detected 5")
        continue
    }
    // console.log(`value of i is ${index}`)    
}
