# Day 2 -Tip Calculator-  Data Types, Type Conversion & Basic Math 🧮

## 📌 Topics Covered

- Python primitive data types :
  - `str` (String)
  - `int` (Integer)
  - `float` (Floating point numbers)
  - `bool` (Boolean)
- Type checking with `type()`
- Type conversion using `str()`, `int()`, `float()`
- Mathematical operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operator precedence (PEMDAS)
- Using f-strings for formatting output

---

## 🧪 Tasks & Practice Exercises

### 🔢 1. Understanding Types and Conversion
- Use `type()` to inspect data types.
- Convert between types using `str()`, `int()`, and `float()`.

```python
# Example:
num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")


### 🧮 2. Mathematical Operators and Precedence
Operator	Meaning	Example
+	Addition	3 + 2 = 5
-	Subtraction	5 - 3 = 2
*	Multiplication	3 * 4 = 12
/	Division	6 / 3 = 2.0
**	Exponentiation	2 ** 3 = 8
//	Floor Division	5 // 2 = 2
%	Modulus (remainder)	5 % 2 = 1

Understand order of operations using PEMDAS:

Parentheses → Exponents → Multiplication/Division → Addition/Subtraction

💡 Final Mini Project: Tip Calculator 💵
🎯 Goal:
Create a simple tip calculator that calculates how much each person should pay after a meal.

🧾 Project Flow:

Ask for total bill amount.

Ask the percentage tip (e.g., 10, 12, 15).

Ask how many people to split the bill.

Calculate each person’s share.

# Sample Formula:
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_bill = bill + (bill * tip_as_percent)
bill_per_person = round(total_bill / people, 2)

print(f"Each person should pay: ${bill_per_person}")

💡 Sample Output:

Welcome to the tip calculator!
What was the total bill? $124.56
What percentage tip would you like to give? 12
How many people to split the bill? 7
Each person should pay: $20.12

✅ Key Takeaways
Practice of converting between strings, integers, and floats.

Basic arithmetic in Python and understanding operator precedence.

Real-world application using math and user input.
