let num1 = 10;
let num2 = 5;
let text1 = "Hello";
let text2 = "World";
let isTrue = true;


let sum = num1 + num2;
let difference = num1 - num2;
let product = num1 * num2;
let quotient = num1 / num2;
let concatenatedText = text1 + " " + text2;

console.log(sum);
console.log(difference);
console.log(product);
console.log(quotient);
console.log(concatenatedText);

function compareNumbers() {
    console.log("num1 == num2:", num1 == num2);
    console.log("num1 != num2:", num1 != num2);
    console.log("num1 > num2:", num1 > num2);
    console.log("num1 >= num2:", num1 >= num2);
    console.log("num1 < num2:", num1 < num2);
    console.log("num1 <= num2:", num1 <= num2);
}


function confirmExit() {
    let exit = confirm("გსურთ საიტის დატოვება?");
    if (exit) {
        console.log("გმადლობთ სტუმრობისთვის!");
    } else {
        console.log("გმადლობთ, რომ დარჩით!");
    }
}
    
