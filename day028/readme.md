# Day 28 – Pomodoro App / Simple Timer ⏲️

## 📌 Overview
On Day 28 of my [#100DaysOfPython](https://github.com/Akula-tharun-kumar/100-Days-of-Python) challenge, I built a **Pomodoro Timer App** using the `tkinter` GUI library in Python.

The **Pomodoro Technique** is a time management method that uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. This app helps boost productivity by structuring focused work sessions followed by rest periods.

---

## 🧠 Key Concepts Covered

- GUI Programming using `tkinter`
- Timer mechanisms using `after()` method
- Countdown logic and loop recursion
- Working with global variables
- UI updates and control flow logic
- Use of emojis and Unicode for visual appeal
- Resetting the timer and managing work/break sessions

---

### 🎯 Features

* **Custom Time Input**

  * Set work and break durations in minutes (`m`) or seconds (`s`).
  * Example: `25m` for 25 minutes or `1500s` for 1500 seconds.
* **Session Types**

  * Work Session
  * Short Break
  * Long Break
* **Cycle Tracking**

  * Automatically tracks your work/break cycles.
* **Sound Alerts**

  * Plays a sound when each session ends (using `playsound` or `pygame`).
* **Graphical Interface**

  * Built with **Tkinter** for a clean and interactive user experience.
* **Reset Function**

  * Stop and restart the timer anytime.

---
### 📋 How It Works

1. **Enter Time**

   * Input time for work, short break, and long break sessions.
   * You can use formats like `25m` or `1500s`.

2. **Start Timer**

   * The app starts counting down for the set duration.
   * A sound alert plays when time is up.

3. **Cycle Management**

   * After a work session → short break.
   * After every 4 work sessions → long break.

4. **Reset Anytime**

   * You can stop the current timer and start fresh.

---


### 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tharunerd/100-days-of-python.git
   ```
   ```
   cd day028
   ```

2. Install dependencies:

   ```bash
   pip install playsound
   # OR
   pip install pygame
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

### 📂 Project Structure

```
pomodoro-timer/
day028/
│
├── main.py
└── images/
    └── tomato.png
```    

---
### 🔊 Adding Sound Alerts

Make sure you have an `alarm.mp3` (or `.wav`) file in the project folder.
Example code snippet for sound:

```python
from playsound import playsound
playsound('alarm.mp3')
```

Or with `pygame`:

```python
import pygame
pygame.mixer.init()
pygame.mixer.music.load("alarm.mp3")
pygame.mixer.music.play()
```

---

### ✅ Example Session

* **Work:** 25 minutes
* **Short Break:** 5 minutes
* **Long Break:** 20 minutes
* **Cycles:** Work → Short Break → Work → Short Break → Work → Short Break → Work → Long Break

---

### 🏆 Learning Objectives

* Tkinter GUI development.
* Time management with `after()` method.
* Handling user inputs and validation.
* Adding multimedia (sound) in Python apps.
* Structuring Python projects.

---

