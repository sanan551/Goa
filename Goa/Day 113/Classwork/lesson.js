const darkModeBtn = document.getElementById("darkModeBtn")
const lightModeBtn = document.getElementById("lightModeBtn")

lightModeBtn.addEventListener("click" , () => {
    document.documentElement.style.setProperty("--backround-color" , "#e9e9e9ff")
})

darkModeBtn.addEventListener("click" , () => {
    document.documentElement.style.setProperty("--backround-color" , "#222222ff")
})