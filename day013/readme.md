# Day 13: Introduction to Functions

*100 Days of Code (Python Bootcamp Inspired by Dr. Angela Yu)*

## 🎯 Project Overview

Day 13 focuses on one of the most important building blocks in programming — **functions**.  
You’ll learn how to organize code into reusable chunks, reduce repetition, and write cleaner, more readable programs.

Functions help you:

*   Break large problems into smaller steps
*   Reuse logic without copying/pasting
*   Make your code easier to debug and maintain

***

## 🧠 Concepts Covered

### ✔️ Defining a Function

Learn the syntax of creating your own functions:

```python
def my_function():
    print("Hello")
```

### ✔️ Calling a Function

Functions do nothing until you “call” them:

```python
my_function()
```

### ✔️ Indentation Rules

Python uses indentation to mark code blocks, especially inside functions.

### ✔️ Function Parameters

Pass information *into* functions:

```python
def greet(name):
    print(f"Hello, {name}!")
```

### ✔️ Return Statements

Send a value *back* from a function:

```python
def add(a, b):
    return a + b
```

### ✔️ Composition (functions calling other functions)

Break down large tasks into smaller helper functions.

***

## 📝 What You Do on This Day

*   Practice writing simple functions
*   Add parameters and arguments
*   Return values instead of just printing
*   Convert repeated code into function calls
*   Build confidence working with structured, reusable code

***

## 💡 Why Functions Matter

Functions are the backbone of all larger Python projects you will build later, including:

*   Games
*   GUI apps
*   Web apps
*   APIs
*   Data processing scripts

Without functions, code becomes messy and difficult to scale. Learning them now sets you up for success in upcoming days.

***

## 🛠️ Example Snippets

### 1) A Simple Function

```python
def say_hello():
    print("Hello, world!")
```

### 2) Function with Parameters

```python
def welcome_user(username):
    print(f"Welcome, {username}!")
```

### 3) Returning a Value

```python
def multiply(x, y):
    return x * y
```

### 4) Using Multiple Functions Together

```python
def add(a, b):
    return a + b

def show_result():
    result = add(5, 3)
    print(f"The result is {result}")

show_result()
```

***

## 🧪 Try-It-Yourself Tasks

*   Write a function that checks if a number is even.
*   Create a function that prints a motivational message.
*   Build a small calculator using functions for add/subtract/multiply/divide.

***

## 🗂️ Suggested Repo Structure

    📦 Day13-Functions
     ┣ 📄 functions_basics.py
     ┣ 📄 parameters_and_returns.py
     ┣ 📄 mini_challenges.py
     ┗ 📄 README.md

***

## ✨ Summary

By the end of Day 13, you will understand:

*   How to create and call functions
*   How to pass data using parameters
*   How to produce results using return statements
*   Why functions make your code cleaner and more powerful
