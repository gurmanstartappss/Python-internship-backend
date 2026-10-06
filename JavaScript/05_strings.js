//to decaler string
const nam="gurman" //or const nam=new String('Gurman')
const repoCount= 50;

console.log(nam  + repoCount)//old way to concatenate

//use backticks(``)--string interpolation--we create placeholders to inject variables directly
console.log(`Hello my name is ${nam} and repo count is ${repoCount}`)

// syntax------ ` stringssss ${variable}`

console.log(nam[0])//g

//strings methods

let str = "Gurman Garg";

// 1. length → returns length
console.log(str.length);                    // 11

// 2. toUpperCase() → converts to uppercase
console.log(str.toUpperCase());             // GURMAN GARG

// 3. toLowerCase() → converts to lowercase
console.log(str.toLowerCase());             // gurman garg

// 4. includes() → checks if string contains a value
console.log(str.includes("Gurman"));        // true

// 5. startsWith() → checks starting value
console.log(str.startsWith("Gur"));         // true

// 6. endsWith() → checks ending value
console.log(str.endsWith("Garg"));          // true

// 7. indexOf() → returns index of value
console.log(str.indexOf("G"));              // 0

// 8. slice() → extracts part of string
console.log(str.slice(0, 6));                // Gurman
console.log(str.slice(-4));                 // Garg

// 9. replace() → replaces first matching value
console.log(str.replace("Garg", "Singh"));   // Gurman Singh

// 10. replaceAll() → replaces all matching values
let x = "hello hello";
console.log(x.replaceAll("hello", "hi"));    // hi hi

// 11. trim() → removes spaces from both ends
let name = "  Gurman  ";
console.log(name.trim());                   // Gurman

// 12. split() → converts string into array
console.log(str.split(" "));                // ["Gurman", "Garg"]

// 13. charAt() → returns character at index
console.log(str.charAt(0));                 // G

// 14. at() → returns character at index
console.log(str.at(0));                     // G
console.log(str.at(-1));                    // g