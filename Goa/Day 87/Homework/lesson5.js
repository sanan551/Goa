let secretNumber = 40
let guess = null;

while (guess != secretNumber) {
  guess = parseInt(prompt("გამოიცანით რიცხვი 1-დან 50-მდე"));

  if (guess < secretNumber) {
    alert("მეტი ცადე!");
  } else if (guess > secretNumber) {
    alert("ნაკლები ცადე!");
  } else if (guess === secretNumber) {
    alert("გილოცავთ! სწორად გამოიცანით 🎉");
  } else {
    alert("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.");
  }
}
