let n = Number(prompt("შეიყვანე რიცხვი:"));

let sum = 0;
for (let i = 1; i < n; i++) {
    if (i % 2 !== 0) {
        sum += i;
    }
}

console.log(sum);
