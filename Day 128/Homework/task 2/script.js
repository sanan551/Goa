class Character {
  static count = 0; 

  constructor(health, damage, speed, level) {
    this.health = health;
    this.damage = damage;
    this.speed = speed;
    this.level = level;
    Character.count++; 
  }

  static count_characters() {
    return Character.count;
  }
}


const ninja = new Character(100, 25, 40, 5);
const samurai = new Character(120, 30, 35, 6);
const viking = new Character(150, 35, 30, 7);
const warrior = new Character(110, 20, 32, 4);
const veteran = new Character(130, 28, 33, 6);
const tribesman = new Character(90, 15, 38, 3);
const necromancer = new Character(80, 40, 25, 8);

console.log("შექმნილი პერსონაჟების რაოდენობა:", Character.count_characters());
