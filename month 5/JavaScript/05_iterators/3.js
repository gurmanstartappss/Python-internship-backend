
const myArray = [1, 2, 3, 4, 5];

// for...of loop: iterates over values
for (const i of myArray) {
    // console.log(i);
}

const greet = "hello world";

for (const i of greet) {
    // console.log(`Each char is ${i}`);
}

// Map: stores unique keys and their associated values
const map = new Map();

map.set('IN', "INDIA");
map.set('USA', "United States of America");
map.set('FR', "France");

// Iterate over Map entries using for...of
for (const [key, value] of map) {
    // console.log(`${key} shortcut is for ${value}`);
}
