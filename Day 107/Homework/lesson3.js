function count(numbers) {
  let c = 0;
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > 10) {
      c = c + 1;
    }
  }
  return c;
}

let result = count([5, 12, 18, 7, 22]);
console.log(result);
