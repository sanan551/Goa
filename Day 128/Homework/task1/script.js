class Car {
  constructor(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  }

  getInfo() {
    console.log(`ბრენდი: ${this.brand}, მოდელი: ${this.model}, წელი: ${this.year}`);
  }
}

const car1 = new Car("BMW", "M5", 2022);
car1.getInfo(); 

