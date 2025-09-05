let count = 0
function counter1() {
    count += 10    
    document.getElementById("count").textContent = count;
    
};


function Reset() {
    count = 0    
    document.getElementById("count").textContent = count;
    
}

function counter2() {
    count -= 10    
    document.getElementById("count").textContent = count;
    
};
