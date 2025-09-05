let ageInput = prompt("შეიყვანეთ თქვენი ასაკი:");
let age = Number(ageInput);
let result = "";

if (age <= 0) {
  result = "გთხოვთ, შეიყვანეთ სწორი ასაკი.";
}

if (age >= 1 && age < 6) {
  result = "ბილეთი უფასოა.";
}

if (age >= 6 && age <= 17) {
  result = "ბილეთის ფასი არის 5 ლარი.";
}

if (age >= 18 && age <= 64) {
  result = "ბილეთის ფასი არის 10 ლარი.";
}

if (age >= 65) {
  result = "ბილეთის ფასი არის 7 ლარი.";
}

document.getElementById("result").textContent = result;
