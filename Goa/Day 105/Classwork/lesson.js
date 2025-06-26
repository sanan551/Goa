let count = 0
let intervalId = 0
watch = document.getElementById("counter")

function start() {
    count = count += 1
    watch.textContent = count
    

}
intervalId = setInterval(start, 1000)


function stop() {
    clearInterval(intervalId)
}

function reset() {
    clearInterval(intervalId)
    count = 0
    watch.textContent = count
}

