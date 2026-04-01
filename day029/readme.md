
---

# Day 29 – Local Password Manager App 🔐

This project is part of my **100 Days of Python** journey (Day 29).
It’s a **Local Password Manager** that allows you to securely store, search, and retrieve passwords for different websites locally on your computer.

## 📌 Features

* **Add New Passwords**: Save website credentials (Website, Email/Username, Password).
* **Search Saved Passwords**: Quickly find and retrieve credentials.
* **Random Password Generator**: Automatically create strong and secure passwords.
* **Local Storage**: All data is stored locally in a JSON file for persistence.

## 🛠 Tech Stack

* **Language:** Python 🐍
* **GUI:** Tkinter
* **Data Storage:** JSON

## 📂 File Structure

```
📁 Local Password Manager
│── main.py           # Main application script
│── data.json         # Local storage for saved passwords (added to gitignore)
│── .gitignore        # add data.txt file
│── logo.png          # Application logo for GUI
│── README.md         # Project documentation
```

## 🚀 How to Run

1. Clone the repository:

   ```bash
   https://github.com/tharunerd/100-days-of-python.git
   ```
2. Navigate to the project folder:

   ```bash
   cd day029 
   ```
3. Run the app:

   ```bash
   python main.py
   ```


## ⚠ Disclaimer

This project is for **learning purposes only**.
Passwords are stored locally in **plain text (JSON)** and are **not encrypted**, so avoid storing real passwords.

---

