Awesome—let’s make a **Day 16 (OOP) Coffee Machine Simulator** README that matches the tone and structure of your earlier days, but now emphasizes **Object-Oriented Programming** (classes, objects, composition, responsibilities).

This is fully original and safe to publish on your GitHub.

***

# Day 16: Coffee Machine (OOP)

*100 Days of Code (Python Bootcamp Inspired by Dr. Angela Yu)*

## 🎯 Project Overview

Rebuild the Coffee Machine from a **procedural** approach into a clean, **Object‑Oriented** design.  
You’ll split responsibilities across several classes (e.g., `Menu`, `MenuItem`, `CoffeeMaker`, `MoneyMachine`) and compose them into a working simulator.

**Key goals:**

*   Practice **encapsulation**, **composition**, and **single responsibility**.
*   Model real-world entities as Python classes with clear **interfaces** (methods/properties).
*   Improve maintainability and testability compared to the Day 16 procedural version.

***

## 🧠 Concepts Covered

*   **Classes & Objects**: defining blueprints and creating instances
*   **Encapsulation**: grouping data + behavior, hiding internal state where appropriate
*   **Composition**: building bigger systems from smaller parts (e.g., machine has a `CoffeeMaker` + `MoneyMachine`)
*   **Method responsibilities**: `report()`, `is_resource_sufficient()`, `make_coffee()`, `process_coins()`, etc.
*   **Data modeling** with classes like `MenuItem` (name, cost, ingredients)

***

## 📝 Project Description

You will implement an OOP Coffee Machine with:

1.  **Menu & Items**
    *   A `Menu` that returns available `MenuItem`s (espresso, latte, cappuccino).
    *   Each `MenuItem` defines **ingredients needed** and **cost**.

2.  **Coffee Maker**
    *   Tracks resources (water, milk, coffee).
    *   Can: `report()` current levels, verify `is_resource_sufficient(item)`, and `make_coffee(item)` to deduct ingredients.

3.  **Money Machine**
    *   Handles accepting coins (or any currency mapping), summing totals, checking if payment is enough, returning change, and tracking profits.
    *   Can: `make_payment(cost)` and `report()` current earnings.

4.  **App Loop**
    *   Repeatedly prompts: `What would you like? (espresso/latte/cappuccino)`
    *   Commands: `report` (for both resources and money) and `off` (shutdown).
    *   For valid orders: checks resources → processes payment → makes coffee → continues.

***

## 🧩 Class Design (At a Glance)

    +------------------------+       +----------------------+
    |        Menu            |       |      MenuItem        |
    | - items: list[MenuItem]|<----->| - name: str          |
    | + get_items(): str     |       | - cost: float        |
    | + find_item(name): ... |       | - ingredients: dict  |
    +------------------------+       +----------------------+

    +------------------------+       +----------------------+
    |      CoffeeMaker       |       |     MoneyMachine     |
    | - resources: dict      |       | - profit: float      |
    | + report(): None       |       | + report(): None     |
    | + is_resource_sufficient(item):bool| + make_payment(cost): bool |
    | + make_coffee(item):None|       | + process_coins(): float     |
    +------------------------+       +----------------------+

> *Composition:* Your main script **creates** one `Menu`, one `CoffeeMaker`, one `MoneyMachine`, then orchestrates them.

***

## 🛠️ Example Snippets

> These are illustrative examples to show structure. Adapt names and values as you like.

### 1) Menu and MenuItem

```python
# menu.py
from dataclasses import dataclass

@dataclass(frozen=True)
class MenuItem:
    name: str
    cost: float
    ingredients: dict  # {"water": int, "milk": int, "coffee": int}

class Menu:
    def __init__(self, items: list[MenuItem]):
        self._items = items

    def get_items(self) -> str:
        """Return a slash-separated string for the prompt."""
        return " / ".join(item.name for item in self._items)

    def find_item(self, name: str) -> MenuItem | None:
        name = name.lower().strip()
        for item in self._items:
            if item.name == name:
                return item
        return None
```

### 2) CoffeeMaker

```python
# coffee_maker.py
class CoffeeMaker:
    def __init__(self, initial_resources: dict):
        # e.g., {"water": 300, "milk": 200, "coffee": 100}
        self.resources = initial_resources | {}  # shallow copy

    def report(self) -> None:
        print(f"Water: {self.resources.get('water', 0)}ml")
        print(f"Milk: {self.resources.get('milk', 0)}ml")
        print(f"Coffee: {self.resources.get('coffee', 0)}g")

    def is_resource_sufficient(self, drink) -> bool:
        for item, required in drink.ingredients.items():
            if self.resources.get(item, 0) < required:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink) -> None:
        for item, required in drink.ingredients.items():
            self.resources[item] -= required
        print(f"Here is your {drink.name} ☕️. Enjoy!")
```

### 3) MoneyMachine

```python
# money_machine.py
COINS = {"quarters": 0.25, "dimes": 0.10, "nickels": 0.05, "pennies": 0.01}

class MoneyMachine:
    def __init__(self):
        self.profit = 0.0

    def report(self) -> None:
        print(f"Money: ${self.profit:.2f}")

    def process_coins(self) -> float:
        print("Please insert coins.")
        total = 0.0
        for coin, value in COINS.items():
            count = int(input(f"How many {coin}? ") or 0)
            total += count * value
        return round(total, 2)

    def make_payment(self, cost: float) -> bool:
        paid = self.process_coins()
        if paid < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = round(paid - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        self.profit += cost
        return True
```

### 4) Main App

```python
# main.py
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU_ITEMS = [
    MenuItem("espresso", 1.5, {"water": 50, "coffee": 18}),
    MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24}),
    MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24}),
]

def main():
    menu = Menu(MENU_ITEMS)
    maker = CoffeeMaker({"water": 300, "milk": 200, "coffee": 100})
    cashier = MoneyMachine()

    is_on = True
    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower().strip()
        if choice == "off":
            is_on = False
        elif choice == "report":
            maker.report()
            cashier.report()
        else:
            drink = menu.find_item(choice)
            if drink is None:
                print("Invalid option. Try again.")
                continue
            if maker.is_resource_sufficient(drink) and cashier.make_payment(drink.cost):
                maker.make_coffee(drink)

if __name__ == "__main__":
    main()
```

***

## 🔁 App Flow

1.  Prompt for choice (menu, `report`, or `off`)
2.  On valid drink:
    *   Check resources (`CoffeeMaker.is_resource_sufficient`)
    *   Process payment (`MoneyMachine.make_payment`)
    *   Brew (`CoffeeMaker.make_coffee`)
3.  Loop until `off`

***

## 🧪 Try‑It‑Yourself Enhancements

*   **Refill command** (`refill water 300`, `refill milk 500`)
*   **Local currency** mapping (₹ coins/notes) + **UPI simulation**
*   **Discount codes** or loyalty points
*   **JSON or YAML config** for menu/resources (load on startup)
*   **Unit tests** for `is_resource_sufficient`, `make_payment`, `find_item`
*   **Exceptions** for predictable failures (e.g., `InsufficientResourcesError`)
*   **Type hints + pydantic** validation for menu/resource schemas

***

## 🗂️ Suggested Repo Structure

    📦 Day16-CoffeeMachine-OOP
     ┣ 📄 main.py
     ┣ 📄 menu.py
     ┣ 📄 coffee_maker.py
     ┣ 📄 money_machine.py
     ┣ 📄 README.md
     ┣ 📁 tests
     ┃ ┣ test_menu.py
     ┃ ┣ test_coffee_maker.py
     ┃ ┗ test_money_machine.py
     ┗ 📁 assets     # optional ASCII art, logos

***

## ▶️ How to Run

```bash
python main.py
```

**Commands available:**

*   `espresso` / `latte` / `cappuccino` – order a drink
*   `report` – show resources and money
*   `off` – power down the machine

***

## ✅ Learning Outcomes

By the end of Day 16 (OOP), you’ll be able to:

*   Design small systems using **classes** with clear responsibilities
*   **Compose** multiple classes to build a complete program
*   Write cleaner code that’s **easier to extend and test**
*   Move from procedural to **object‑oriented thinking**

***

## ✨ Notes for Future You

*   Consider **persistence** (save/load resources & profits between runs)
*   Add an **AdminMode** with passwords for `refill` and `report`
*   Create a **GUI** (Tkinter) or **API** (Flask/FastAPI) wrapper later
*   Explore **LSP/SRP/OCP** from SOLID—this project is a great playground

