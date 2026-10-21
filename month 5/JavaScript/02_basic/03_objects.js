// objects and Event
// to decare objects:
// literal(no singleton) and constructor(creates singleton when object created by a constructor)

//symbol declared
const mysym=Symbol("key1")

//----object literals

const jsuser={      //objects should have key value pair unlike arrays 
    name:"gurman",
    age:18,
    mysym:"mykey1",//wrong syntax
    [mysym]:"mykey1",//correct syntax
    location:"indore",
    isloggedin:"True",
    lastlogin:["monday","tuesday"]
}

// now to access values

console.log(jsuser.name)
console.log(jsuser["name"])
console.log(jsuser.mysym)//wrong syntax mykey1 (string)
console.log(typeof jsuser[mysym])//correct syntax symbol print acting as key in array (both give same but syntax differnece)

// Object.freeze(jsuser)//freezes the object so no changes affect

//functions(treated like variables)

jsuser.greeting=function(){
    console.log("hello")
}
console.log(jsuser.greeting())

jsuser.greeting2=function(){  //string interpolation
    console.log(`hello ${this.name}`)
}
console.log(jsuser.greeting())
console.log(jsuser.greeting2())