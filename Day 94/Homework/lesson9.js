let numbers = [1, 4, 7, 10, 13, 16, 20];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] % 2 === 0) {
    sum += numbers[i];
  }
}

console.log("ლუწი რიცხვების ჯამი: " + sum);
