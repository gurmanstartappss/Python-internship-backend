
const myObject = {
    js: 'javascript',
    cpp: 'c++',
    rb: 'ruby'
};

// for...in loop: iterates over object keys
for (const key in myObject) {
    console.log(key);
}

// Access both keys and values
for (const key in myObject) {
    console.log(`${key} stands for ${myObject[key]}`);
}