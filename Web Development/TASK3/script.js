const board = document.getElementById("board");
const statusText = document.getElementById("status");
const resetButton = document.getElementById("reset");
let cells = [];
let currentPlayer = "X";
let gameState = ["", "", "", "", "", "", "", "", ""];

const winPatterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
];

function checkWinner() {
    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (gameState[a] && gameState[a] === gameState[b] && gameState[a] === gameState[c]) {
            statusText.innerText = `${gameState[a]} wins!`;
            board.style.pointerEvents = "none";
            return;
        }
    }
    if (!gameState.includes("")) {
        statusText.innerText = "It's a draw!";
    }
}

function handleClick(index) {
    if (!gameState[index]) {
        gameState[index] = currentPlayer;
        cells[index].innerText = currentPlayer;
        checkWinner();
        currentPlayer = currentPlayer === "X" ? "O" : "X";
    }
}

function resetGame() {
    gameState.fill("");
    cells.forEach(cell => cell.innerText = "");
    board.style.pointerEvents = "auto";
    statusText.innerText = "";
    currentPlayer = "X";
}

function initBoard() {
    for (let i = 0; i < 9; i++) {
        let cell = document.createElement("div");
        cell.classList.add("cell");
        cell.addEventListener("click", () => handleClick(i));
        board.appendChild(cell);
        cells.push(cell);
    }
}

resetButton.addEventListener("click", resetGame);
initBoard();
