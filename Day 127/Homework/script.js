const playerChoice = document.getElementById("playerChoice");
const compChoiceP = document.getElementById("compChoice");
const resultP = document.getElementById("result");
const pScoreP = document.getElementById("pScore");
const compScoreP = document.getElementById("compScore");

const choices = ["Rock", "Paper", "Scissors"];
let playerScore = 0;
let computerScore = 0;

playerChoice.addEventListener("click", (e) => {
    if (e.target.tagName !== "BUTTON") return;
    const choice = e.target.textContent;
    const compChoice = choices[Math.floor(Math.random() * 3)];
    compChoiceP.textContent = `Computer choice: ${compChoice}`;

    if (compChoice === choice) {
        resultP.textContent = "Draw!";
    } else if (
        (compChoice === "Rock" && choice === "Scissors") ||
        (compChoice === "Scissors" && choice === "Paper") ||
        (compChoice === "Paper" && choice === "Rock")
    ) {
        computerScore++;
        resultP.textContent = "Computer win!";
        compScoreP.textContent = `Computer score: ${computerScore}`;
    } else {
        playerScore++;
        resultP.textContent = "You win!";
        pScoreP.textContent = `Player score: ${playerScore}`;
    }
});

