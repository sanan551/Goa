
const me = {
  name: "Giorgi",
  surname: "Iashvili",
  age: 22
};

const mother = {
  name: "Nino",
  surname: "Kikvadze",
  age: 45
};


console.log("Me:", me);
console.log("Mother:", mother);


console.log(me.name, me.surname, me.age);
console.log(mother.name, mother.surname, mother.age);


me.age = 23;
mother.name = "Nina";
console.log(me);
console.log(mother);


me.profession = "Developer";
mother.hobby = "Gardening";
console.log(me);
console.log(mother);


me.surname = "";
mother.age = 0;
console.log(me);
console.log(mother);
