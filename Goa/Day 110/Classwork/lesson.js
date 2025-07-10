
// classwork 1
let color = 0;

function colorchange() {
    const ball = document.getElementById("ball");

    if (color === 0) {
        ball.style.background = "blue";
        color = 1;
    }
    else if (color === 1) {
        ball.style.background = "green";
        color = 2;
    }
    else if (color === 2) {
        ball.style.background = "yellow";
        color = 3;
    }
    else {
        ball.style.background = "red";
        color = 0;
    }
}

setInterval(colorchange, 5000);

// classwork 2

window.onload = function () {
    console.log(5);
};

// classwork 3

const items = ["ელემენტი 1", "ელემენტი 2", "ელემენტი 3"];
const container = document.getElementById("container");

for (let i = 0; i < items.length; i++) {
    const h2 = document.createElement("h2");
    h2.textContent = items[i];
    container.appendChild(h2);
}



