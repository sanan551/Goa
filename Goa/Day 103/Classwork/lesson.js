// classwork 1
let img = document.getElementById("img");
let btn = document.getElementById("btn");

btn.addEventListener("pointerdown", function () {
    img.src = "image copy.png";
})

// classwork 2

let btn1 = document.getElementById("loseBtn");

btn1.addEventListener("mouseup", function () {
    console.log("you lost!");
});


// classwork 3

let paragraph = document.getElementById("hoverText");

paragraph.addEventListener("mouseover", function () {
    paragraph.style.color = "red";
    paragraph.textContent = "why did you hover over me";
});