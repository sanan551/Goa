function manualIndexOf(arr, element) {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === element) {
      return i; 
    }
  }
  return -1; 
}

console.log(manualIndexOf([10, 20, 30, 40], 30)); // 👉 2
console.log(manualIndexOf([1, 2, 3], 5));         // 👉 -1
console.log(manualIndexOf(["a", "b", "c"], "a")); // 👉 0
