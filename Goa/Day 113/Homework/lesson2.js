const darkModeBtn = document.getElementById("darkModeBtn");
const lightModeBtn = document.getElementById("lightModeBtn");

lightModeBtn.addEventListener("click", () => {
    document.documentElement.style.setProperty("--background-color", "#e9e9e9ff");
    document.documentElement.style.setProperty("--text-color", "#222222ff");
    document.documentElement.style.setProperty("--button-bg", "#ffffff");
    document.documentElement.style.setProperty("--button-text", "#000000");
});

darkModeBtn.addEventListener("click", () => {
    document.documentElement.style.setProperty("--background-color", "#222222ff");
    document.documentElement.style.setProperty("--text-color", "#e9e9e9ff");
    document.documentElement.style.setProperty("--button-bg", "#333333");
    document.documentElement.style.setProperty("--button-text", "#ffffff");
});
