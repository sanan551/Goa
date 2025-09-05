
// Homework 1
let count = 0;
let text = document.getElementById("countertext")
function increaseCounter() {
    count++;
    text.textContent = count;
}

// Homework 2

let img = document.getElementById("hoverimage");
img.addEventListener("mouseenter", function () {
    img.width = 200;
    img.height = 200;
});
img.addEventListener("mouseleave", function () {
    img.width = 150;
    img.height = 150;
});

// Homework 3

let p = document.getElementById("hoverp");
let span = document.createElement("span");
span.textContent = "ახალი ელემენტი";

p.addEventListener("mouseenter", function () {
    p.appendChild(span);
});

p.addEventListener("mouseleave", function () {
    p.removeChild(span);
});

// Homework 4
let box = document.getElementById("box");
box.addEventListener("mousedown", function () {
    document.body.style.backgroundColor = "lightblue";
});

box.addEventListener("mouseup", function () {
    document.body.style.backgroundColor = "white";
});


// Homework 5
let paragraph = document.getElementById("paragraph");
let div = document.createElement("div");
div.textContent = "დამალული ელემენტი";

paragraph.addEventListener("click", function () {
    document.body.appendChild(div);
});

// Homework 6
let btn1 = document.getElementById("btn");
let div1 = document.getElementById("div");

btn1.addEventListener("click", function () {
    let el = document.createElement("p");
    el.textContent = "ახალი ელემენტი";
    div1.appendChild(el);
});

// Homework 7
let list = document.getElementById("list");
let li1 = document.getElementById("li1");
let li2 = document.getElementById("li2");
let li3 = document.getElementById("li3");
let btn0 = document.getElementById("btn1")
let btn2 = document.getElementById("btn2")
let btn3 = document.getElementById("btn3")
btn0.addEventListener("click", function () {
    list.removeChild(li1);
});

btn2.addEventListener("click", function () {
    list.removeChild(li2);
});

btn3.addEventListener("click", function () {
    list.removeChild(li3);
});

// Homework 8
let boxs = document.getElementById("divs");
let para = document.getElementById("para");

para.addEventListener("mouseenter", function () {
  let newp = document.createElement("p");
  newp.textContent = "ახალი პარაგრაფი";
  boxs.replaceChild(newp,para); 
});

// Homework 9
let imgs = document.getElementById("imgs");
let btnss = document.getElementById("btnss");

btnss.addEventListener("click", function () {
  imgs.src = "image.png";
});