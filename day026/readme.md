# 📅 Day 26 – List & Dictionary Comprehension + NATO Alphabet Project

Welcome to Day 26 of my **100 Days of Code: Python Bootcamp by Dr. Angela Yu**!

In this lesson, I explored **List Comprehension**, **Dictionary Comprehension**, and applied these concepts to build a fun and interactive **NATO Alphabet Translator**.

---

## ✅ What I Learned

### 🔹 List Comprehension
- A more concise way to create new lists.
- Syntax: `[new_item for item in iterable if condition]`
- It's Pythonic, readable, and efficient.

```python
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)  # Output: [2, 3, 4]
```

### 🔹 Conditional List Comprehension

```python
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
```

### 🔹 Dictionary Comprehension
- Similar to list comprehension but used to create dictionaries.

```python
names = ["Alex", "Beth", "Caroline", "Dave"]
scores = {name: len(name)*10 for name in names}
print(scores)  # Output: {'Alex': 40, 'Beth': 40, 'Caroline': 80, 'Dave': 40}
```

---

## 🧠 Project: NATO Alphabet Translator

### Objective:
Build a program that:
- Loads the NATO phonetic alphabet from a CSV file.
- Accepts a word from the user.
- Returns a list of NATO codes corresponding to each letter.

### 🔧 Core Logic:

```python
import pandas

# Load data
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Get user input and convert
word = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in word]
print(output_list)
```

---

## 📦 How to Run

1. Install pandas:

```bash
pip install pandas
```

2. Ensure the `nato_phonetic_alphabet.csv` file is in your directory. It should contain two columns: `letter` and `code`.

Example content:
```
letter,code
A,Alfa
B,Bravo
C,Charlie
...
```

3. Run the script:

```bash
python main.py
```

---

## 🎯 Key Takeaways

- Learned how to efficiently generate and filter lists and dictionaries.
- Practiced reading CSV files using Pandas.
- Built an interactive and user-friendly mini-project using real-world data.

---
