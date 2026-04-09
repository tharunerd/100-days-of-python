# Day 31 – Flash Card App (French → English)

## 📌 Overview

This project is part of **Day 31** of the *100 Days of Code: Python* course by Angela Yu.
It’s a **Flash Card Application** built using **Tkinter** for the GUI and **Pandas** for handling word data.
The app helps you learn French vocabulary interactively — showing a French word, then automatically flipping to the English translation after a few seconds.

---

## 🛠 Features

* Displays a **random French word** on a flash card.
* Automatically **flips** to reveal the **English translation** after 3 seconds.
* "✅ Known" button removes the word from the learning list.
* Saves progress in a `words_to_learn.csv` file so you can **resume later**.
* Modern, minimal UI built with Tkinter Canvas and custom buttons.

---

## 📂 Project Structure

```
day31_flash_card/
│── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── right.png
│   ├── wrong.png
│── data/
│   ├── french_words.csv
│   ├── words_to_learn.csv   # created after progress is saved
│── main.py                  # main application script
│── README.md
```

---

## 🚀 How It Works

1. **Launch the app** → A random French word appears.
2. **Wait 3 seconds** → The card flips to show the English translation.
3. **Mark as known/unknown**:

   * ✅ Known → Removes it from your learning list.
   * ❌ Unknown → Keeps it in the rotation.
4. **Progress Saved** → When you close the app, your remaining words are saved.

---

## 📦 Requirements

Install dependencies with:

```bash
pip install pandas
```

Tkinter comes pre-installed with Python.

---

## ▶️ Run the App

```bash
python main.py
```

---

## 📚 Data Source

The `french_words.csv` file contains 100+ French-English word pairs sourced from the course materials.

---

## 💡 Improvements

* Add support for **custom word lists**.
* Implement **multiple language support**.
* Track **accuracy stats** for better learning insights.

---

