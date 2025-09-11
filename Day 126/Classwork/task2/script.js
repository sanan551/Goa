const form = document.getElementById("passwordForm");
const passwordInput = document.getElementById("password");
const message = document.getElementById("message");

form.addEventListener("submit", function (event) {
    event.preventDefault(); 

    const password = passwordInput.value;

    if (password.length >= 8) {
        message.textContent = "Valid Password!";
        message.style.color = "green";
    } else {
        message.textContent = "Password must contain at least 8 characters!";
        message.style.color = "red";
    }
});