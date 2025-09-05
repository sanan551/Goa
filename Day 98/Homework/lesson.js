function Car(brand, model, year) {
  this.brand = brand;
  this.model = model;
  this.year = year;

  this.getDescription = function() {
    return this.year + " " + this.brand + " " + this.model;
  };

  this.age = function() {
    return 2025 - this.year;
  };
}


const car1 = new Car("Toyota", "Corolla", 2015);
const car2 = new Car("BMW", "X5", 2020);
const car3 = new Car("Ford", "Mustang", 2018);


console.log(car1.getDescription(),  car1.age(), );
console.log(car2.getDescription(),  car2.age(), );
console.log(car3.getDescription(),  car3.age(), );


function Rectangle(width, height) {
  this.width = width;
  this.height = height;

  this.getArea = function() {
    return this.width * this.height;
  };

  this.getPerimeter = function() {
    return 2 * (this.width + this.height);
  };
}


const rectangle = new Rectangle(5, 10);

console.log("ფართობი:", rectangle.getArea());
console.log("პერიმეტრი:", rectangle.getPerimeter());
