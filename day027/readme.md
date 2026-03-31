# 📅 Day 27 – GUI Programming with Tkinter | `*args` and `**kwargs` | mile to kilometer converter

Welcome to **Day 27** of my **100 Days of Code: Python Bootcamp by Dr. Angela Yu**!

Today, I entered the world of **Graphical User Interfaces (GUIs)** using Python’s built-in `tkinter` library. Additionally, I learned about advanced function arguments like `*args` and `**kwargs`, which help write more flexible and powerful functions.

---

## ✅ Topics Covered

### 🖼️ Tkinter GUI Programming

- Creating a window with `Tk()`
- Using and styling widgets:
  - `Label`
  - `Button`
  - `Entry`
  - `Text`
  - `Spinbox`
  - `Scale`
  - `Checkbutton`
  - `Radiobutton`
  - `Listbox`
- Understanding widget layout systems:
  - `.pack()`
  - `.place()`
  - `.grid()`
- Event handling using `command=` callbacks
- Fetching input from widgets using `.get()`
- Dynamically updating widgets with `.config()`

### ✨ Function Arguments – `*args` and `**kwargs`

- `*args` for accepting any number of positional arguments
- `**kwargs` for accepting any number of keyword arguments
- Practical examples of how `**kwargs` is used in Tkinter widgets

---

## 🧠 Key Learnings

### Tkinter Basic Window

```python
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=300)
window.mainloop()
```

### Using Widgets

```python
# Label
label = Label(text="Hello, World!", font=("Arial", 18, "bold"))
label.pack()

# Entry
entry = Entry(width=10)
entry.pack()

# Button
def on_click():
    label.config(text=entry.get())

button = Button(text="Click Me", command=on_click)
button.pack()
```

---

### Example: Using `*args` in a Function

```python
def add(*args):
    return sum(args)

print(add(3, 5, 10))  # Output: 18
```

### Example: Using `**kwargs` in a Function

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Tharun", age=23, city="Gurgaon")
```

### Real Example from Tkinter using `**kwargs`

```python
def create_label(**kwargs):
    label = Label(**kwargs)
    label.pack()
    return label

my_label = create_label(text="Dynamic Label", font=("Arial", 16))
```

---

## 💻 How to Run This

No external dependencies required. Just run:

```bash
python .\main.py
python .\mile2kmconcerter.py
python .\playground.py
```

You will see a GUI window pop up. Interact with the widgets and see how the event-driven logic updates the UI.

---

## 🚀 Summary

- Built a GUI using `Tkinter`
- Understood key widgets and layouts
- Implemented dynamic interactions via `command` callbacks
- Learned how `*args` and `**kwargs` can make functions more flexible
- Used `**kwargs` practically in widget creation

This day was a big leap forward into building real applications with Python!

---
