function Car (model,color,releaseYear,isManual) {
    this.model = model
    this.color =  color
    this.releaseYear = releaseYear
    this.isManual = isManual
}

const  car1 = new Car('nissan skyline','white',2000,true)

console.log(car1)

function Person (name,lastname,age) {
    this.name = name
    this.lastname = lastname
    this.age = age
    
}

const person1 = new Person ("Sanan" , "Mamedov",15)

console.log(person1)
