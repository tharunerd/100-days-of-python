
# 📅 Day 25 – CSV Files and Pandas in Python

Welcome to Day 25 of my **100 Days of Code: Python Bootcamp by Dr. Angela Yu**!  
This day was all about learning how to read, analyze, and manipulate data using **CSV files** and the **Pandas** library.

---

## ✅ What I Learned

- How to read `.csv` files using:
  - The built-in `csv` module
  - The `pandas` library
- How to access specific rows and columns from a CSV
- How to find averages, maximum, and conditional data
- How to create your own `DataFrame`
- How to export data back to a CSV file

---

## 🛠 Concepts and Code Used

### Reading CSV with Pandas

```python
import pandas as pd

data = pd.read_csv("weather_data.csv")
print(data["temp"])
````

### Data Analysis

```python
# Get average temperature
print(data["temp"].mean())

# Get max temperature
print(data["temp"].max())

# Get row with highest temperature
print(data[data.temp == data.temp.max()])
```

### Creating and Exporting a DataFrame

```python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

df = pd.DataFrame(data_dict)
df.to_csv("new_scores.csv", index=False)
```

---

🐿️ Squirrel Census Data Project
Using real-world data from the Central Park Squirrel Census, I analyzed the count of squirrels based on their fur color.

🗺️ U.S. States Game (Turtle + CSV)
This is a fun interactive project where you guess all 50 U.S. states. It uses:
- turtle for graphics
- pandas for data handling
- us-states.csv file as reference

**Highlights:**
You guess states by typing their names
If correct, it appears on the map
When you exit, it shows the states you missed and saves them to a file

## 📦 How to Run This Project

1. Install Pandas if you haven't already:

   ```bash
   pip install pandas
   ```
2. Go to the project file 

    ```bash
    -> cd weather report
    -> cd squirrel count
    -> cd US states 
    ```    
3. Run the script:

   ```bash
   python main.py
   ```

---
