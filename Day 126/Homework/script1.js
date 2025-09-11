let arr = [1,2];
arr.push(3); // [1,2,3]
arr.push(4,5); // [1,2,3,4,5]
arr.push("hi"); // [1,2,3,4,5,"hi"]


let arr1 = [1,2,3];
arr.pop(); // [1,2]
arr.pop(); // [1]
arr.pop(); // []

let arr2 = [2,3];
arr.unshift(1); // [1,2,3]
arr.unshift("a"); // ["a",1,2,3]
arr.unshift(10,20); // [10,20,"a",1,2,3]

let arr3 = [1,2,3];
arr.shift(); // [2,3]
arr.shift(); // [3]
arr.shift(); // []

let arr4 = [10,20,30,40];
console.log(arr.slice(1,3)); // [20,30]
console.log(arr.slice(2)); // [30,40]
console.log(arr.slice(-2)); // [30,40]


let arr5 = [1,2,3,4,5];
arr.splice(2,1); // [1,2,4,5]  // index=2-ზე ერთი წაიშალა
arr.splice(1,2,"a","b"); // [1,"a","b",5]
arr.splice(2,0,"X"); // [1,"a","X","b",5] // დამატება
