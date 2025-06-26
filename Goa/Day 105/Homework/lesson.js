

// // Homework 1
// function logger() {
//     console.log("Hello")
// }

// setInterval(logger ,1000)


// Homework2
// let count = 0
// let intervalId = 0


// function stopwatch() {
//     count = count += 1
//     console.log(count)
// }

// setInterval(stopwatch,1000)


//Homework 3

// let count = 0
// let intervalId = 0
// watch = document.getElementById("watch")

// function timer() {
//     count = count += 1
//     watch.textContent = count
    

// }
// intervalId = setInterval(timer, 1000)


// function stop() {
//     clearInterval(intervalId)
// }

// function reset() {
//     count = 0
//     watch.textContent = count
// }



// homework 4
//   let intervalId = 0;
//   let count = 0;

//   function say() {
//     console.log(count);
//     count = count + 1;
//   }

//   function start() {
//     count = +prompt("Enter a time :");
//     intervalId = setInterval(say, 1000);
//   }



// homework 5

//   let time = 10;
//   let countdown = document.getElementById("countdown");
//   let bomb = document.getElementById("bomb");

//   function tick() {
//     countdown.textContent = time;
//     time = time - 1;

//     if (time < 0) {
//       clearInterval(intervalId);
//       bomb.style.display = "none";
//       document.body.style.backgroundImage = "url('explosion.png')";
//     }
//   }

//   let intervalId = setInterval(tick, 1000);

