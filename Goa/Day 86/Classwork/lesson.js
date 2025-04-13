let name = prompt("Enter your name");
document.getElementById("name").textContent = name;



let count = 0
function counter1() {
    count = 5
    document.getElementById("count").textContent = count;
    
};



function Reset() {
    count = 0    
    document.getElementById("count").textContent = count;
    
}

function counter2() {
    count = 25
    document.getElementById("count").textContent = count;
    
};
