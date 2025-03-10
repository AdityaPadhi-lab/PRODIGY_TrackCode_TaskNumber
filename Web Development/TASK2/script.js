let timer;
let seconds = 0, minutes = 0, hours = 0;
let running = false;

function updateDisplay() {
    document.getElementById("display").innerText =
        (hours < 10 ? "0" + hours : hours) + ":" +
        (minutes < 10 ? "0" + minutes : minutes) + ":" +
        (seconds < 10 ? "0" + seconds : seconds);
}

function startTimer() {
    if (!running) {
        running = true;
        timer = setInterval(() => {
            seconds++;
            if (seconds == 60) { seconds = 0; minutes++; }
            if (minutes == 60) { minutes = 0; hours++; }
            updateDisplay();
        }, 1000);
    }
}

function pauseTimer() {
    clearInterval(timer);
    running = false;
}

function resetTimer() {
    clearInterval(timer);
    running = false;
    seconds = 0; minutes = 0; hours = 0;
    updateDisplay();
    document.getElementById("laps").innerHTML = "";
}

function lapTime() {
    let lapItem = document.createElement("li");
    lapItem.innerText = document.getElementById("display").innerText;
    document.getElementById("laps").appendChild(lapItem);
}

document.getElementById("start").addEventListener("click", startTimer);
document.getElementById("pause").addEventListener("click", pauseTimer);
document.getElementById("reset").addEventListener("click", resetTimer);
document.getElementById("lap").addEventListener("click", lapTime);
