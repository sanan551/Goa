const taskInput = document.getElementById("taskInput");
const addTaskBtn = document.getElementById("addTask");
const taskList = document.getElementById("taskList");

function renderTasks() {
    taskList.innerHTML = "";
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.textContent = task;
        taskList.appendChild(li);
    });
}

addTaskBtn.addEventListener("click", () => {
    const val = taskInput.value.trim();
    if (!val) return;
    const tasks = JSON.parse(localStorage.getItem("tasks")) || [];
    tasks.push(val);
    localStorage.setItem("tasks", JSON.stringify(tasks));
    taskInput.value = "";
    renderTasks();
});

renderTasks();

const toggleThemeBtn = document.getElementById("toggleTheme");
function applyTheme(theme) {
    document.body.classList.remove("light", "dark");
    document.body.classList.add(theme);
    localStorage.setItem("theme", theme);
}
toggleThemeBtn.addEventListener("click", () => {
    const current = localStorage.getItem("theme") || "light";
    const next = current === "light" ? "dark" : "light";
    applyTheme(next);
});
applyTheme(localStorage.getItem("theme") || "light");



const visitSpan = document.getElementById("visitCount");
let count = Number(localStorage.getItem("visitCount") || 0);
count++;
localStorage.setItem("visitCount", count);
visitSpan.textContent = count;

document.getElementById("resetVisits").addEventListener("click", () => {
    localStorage.setItem("visitCount", 0);
    visitSpan.textContent = 0;
});



const colorSelect = document.getElementById("colorSelect");
const preview = document.getElementById("colorPreview");
const clearPrefBtn = document.getElementById("clearPreference");

function applyColor(color) {
    preview.style.background = color || "transparent";
    if (color) localStorage.setItem("preferredColor", color);
}

colorSelect.addEventListener("change", () => {
    applyColor(colorSelect.value);
});

clearPrefBtn.addEventListener("click", () => {
    localStorage.removeItem("preferredColor");
    colorSelect.value = "";
    preview.style.background = "transparent";
});

const savedColor = localStorage.getItem("preferredColor");
if (savedColor) {
    colorSelect.value = savedColor;
    applyColor(savedColor);
}
