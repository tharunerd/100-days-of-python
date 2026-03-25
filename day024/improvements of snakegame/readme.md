
# 🐍 Snake Game – Persistent Score Edition (Day 24)

## 📘 Overview
On Day 24 of the 100 Days of Python Bootcamp, I enhanced my Snake Game by adding **persistent score tracking** using file handling. This version saves the highest score in a file and updates it automatically when a new record is set — making the game more competitive and realistic.

## 🚀 New Features
- High score saved in a `data.txt` file
- Score updates only when a new high score is achieved
- Seamless integration with the scoreboard display
- Cleaner and more modular code structure

## ✅ Key Learnings
- Using `with open()` for safe and efficient file access
- Stripping `\n` from each line using `.strip()`
- Efficient string replacement with `.replace()`
- Basic automation using file input/output
- Integrating file handling with game logic

## 🧠 Challenge Yourself
- Add error handling (e.g., if the score file doesn't exist)
- Make the game accept dynamic file inputs for templates or scores
- Export game results or scores as PDFs using libraries like `fpdf`

## 🛠️ Technologies Used
- Python 3
- Turtle Graphics
- File I/O (`open`, `read`, `write`)
- OOP principles

## 🧾 How to Run the Game
### 1. Clone the Repository

### 2. Run the Game
```bash
python main2.py
```

> Ensure `data.txt` exists in the project directory. If not, the game will create it automatically.

## 🎮 Controls
- Arrow keys to move the snake: ↑ ↓ ← →
- Eat food to grow and increase your score
- Avoid collisions with walls and yourself

## 📂 File Structure
```
snake-game/
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
└── data.txt  # Stores the high score
```

## 🙌 Reflections
This update made the game feel more polished and user-friendly.  
Learning how to persist data between sessions using files was a valuable step toward building more dynamic and interactive applications.

---

