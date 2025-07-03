let ul = document.getElementById("list");

for (let i = 1; i <= 5; i++) {
    let li = document.createElement("li");
    li.textContent = "ელემენტი ნომერი " + i;
    ul.appendChild(li);
}