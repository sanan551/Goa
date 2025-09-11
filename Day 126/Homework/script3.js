function manualMap(array, callback) {
  let result = [];
  for (let i=0; i<array.length; i++) {
    result.push(callback(array[i], i, array));
  }
  return result;
}


let nums = [1,2,3];
let doubled = manualMap(nums, x => x*2);
console.log(doubled);



function manualFilter(array, callback) {
  let result = [];
  for (let i=0; i<array.length; i++) {
    if (callback(array[i], i, array)) {
      result.push(array[i]);
    }
  }
  return result;
}

// გამოყენება
let nums1 = [1,2,3,4,5];
let even = manualFilter(nums1, x => x % 2 === 0);
console.log(even); // [2,4]
