# Day 17: True/False Quiz (OOP)

*100 Days of Code (Python Bootcamp Inspired by Dr. Angela Yu)*

## 🎯 Project Overview

Build a **True/False Quiz** using **Object‑Oriented Programming**.  
You’ll design small, focused classes to model **questions**, **quiz logic**, and **data**, then tie them together into a clean command‑line experience (and optionally a GUI later).

***

## 🧠 Concepts Covered

*   **Classes & Objects** for modeling domain entities
*   **Encapsulation**: grouping state and behavior (e.g., `QuizBrain` holds score, question index, and logic)
*   **Composition**: a quiz *has many* `Question` objects
*   **Data handling**: ingesting a list/dict of questions (could be JSON or Python list of dicts)
*   **Control flow**: loops, conditionals, validation
*   **Basic separation of concerns** (data vs. logic vs. interface)

***

## 📝 Project Description

Create a quiz program that:

1.  Loads a set of **True/False** questions.
2.  Presents questions **one at a time** to the user.
3.  Accepts user input (`"True"` / `"False"` or `T/F`), validating responses.
4.  Checks correctness, **updates score**, and shows feedback.
5.  Displays **final results** when the quiz ends.

> The focus is on **OOP design**: one class for questions (`Question`), one for quiz logic (`QuizBrain`), and a simple interface layer (CLI now, GUI later).

***

## 💡 Key Features

*   **Question bank** as a list of `Question` objects
*   **Quiz engine** that tracks the current question number and score
*   **Input normalization** (accept `t`, `true`, `T`, `True`, etc.)
*   **Instant feedback** after each question
*   **End summary** with total score and accuracy

***

## 🛠️ Example Snippets

> These examples illustrate structure; adjust names and logic to match your style.

### 1) Question Model

```python
# question.py
from dataclasses import dataclass

@dataclass(frozen=True)
class Question:
    text: str
    answer: bool  # True for "True", False for "False"
```

### 2) Quiz Logic

```python
# quiz_brain.py
class QuizBrain:
    def __init__(self, questions: list):
        self.question_list = questions
        self.question_number = 0
        self.score = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def current_question(self):
        return self.question_list[self.question_number]

    def check_answer(self, user_input: str) -> bool:
        normalized = user_input.strip().lower()
        user_answer = normalized in ("t", "true", "y", "yes")
        correct = self.current_question().answer
        is_correct = (user_answer == correct)
        if is_correct:
            self.score += 1
        self.question_number += 1
        return is_correct
```

### 3) Data (Example Bank)

```python
# data.py
RAW_QUESTIONS = [
    {"text": "The sky is blue.", "answer": True},
    {"text": "2 + 2 equals 5.", "answer": False},
    {"text": "Python is a snake AND a programming language.", "answer": True},
]
```

### 4) Main App (CLI)

```python
# main.py
from question import Question
from quiz_brain import QuizBrain
from data import RAW_QUESTIONS

def build_question_bank():
    return [Question(q["text"], bool(q["answer"])) for q in RAW_QUESTIONS]

def prompt_user(prompt: str) -> str:
    while True:
        ans = input(prompt + " (T/F): ").strip().lower()
        if ans in {"t", "f", "true", "false"}:
            return ans
        print("Please enter T/F or True/False.")

def run_quiz():
    questions = build_question_bank()
    quiz = QuizBrain(questions)

    print("\n🎓 Welcome to the True/False Quiz!\n")
    while quiz.still_has_questions():
        q = quiz.current_question()
        user_ans = prompt_user(f"Q{quiz.question_number + 1}: {q.text}")
        correct = quiz.check_answer(user_ans)
        print("✅ Correct!\n" if correct else "❌ Wrong!\n")

    total = len(questions)
    print(f"Quiz finished! Your score: {quiz.score}/{total} ({quiz.score/total:.0%})")

if __name__ == "__main__":
    run_quiz()
```

***

## 🔁 Flow Overview

1.  **Build** a `Question` list from raw data.
2.  **Initialize** `QuizBrain` with that list.
3.  **Loop** while there are questions: show text → input → check → feedback.
4.  **Finish**: print score/accuracy.

***

## 🧪 Try‑It‑Yourself Enhancements

*   **Question source**: load from a JSON file or an API (e.g., Open Trivia DB), then map to `Question`.
*   **Categories/difficulty**: filter by topic or difficulty levels.
*   **Timer/limits**: add a countdown or max attempts.
*   **Review mode**: store incorrect questions, show explanations afterward.
*   **Scoring rules**: streak bonuses, negative marking, or partial credits.
*   **GUI**: upgrade to a Tkinter interface (Day 34 style later).
*   **Unit tests**: test `still_has_questions`, `check_answer`, and input normalization.

***

## 🗂️ Suggested Repo Structure

    📦 Day17-TrueFalseQuiz
     ┣ 📄 main.py
     ┣ 📄 question_model.py
     ┣ 📄 quiz_brain.py
     ┣ 📄 data.py            # or questions.json
     ┣ 📄 README.md
    

***

## ▶️ How to Run

```bash
python main.py
```

**Controls:**

*   Answer each prompt with `T/F` or `True/False` (case‑insensitive).

***

## ✅ Learning Outcomes

By the end of Day 17, you will:

*   Model a small problem domain with **classes**
*   Separate **data**, **logic**, and **UI** concerns cleanly
*   Write an app that’s easy to **extend** and **test**
*   Be ready to integrate **external data sources** or build a **GUI** version

***

## ✨ Notes for Future You

*   If you plan to fetch questions from an API, add a small **adapter** function that transforms raw JSON into `Question` objects.
*   Keep the **UI thin** (CLI/GUI) and the **logic in `QuizBrain`**—this makes it easy to swap interfaces later.
