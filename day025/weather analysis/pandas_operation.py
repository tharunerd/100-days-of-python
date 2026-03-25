import pandas as pd
import csv
import matplotlib.pyplot as plt

# Using just file methods
with open("weather_data.csv") as data_file:
    data_lines = data_file.readlines()
    print(data_lines)

# Using csv library
with open("weather_data.csv") as data_file:
    csv_data = csv.reader(data_file)
    temperatures = []
    for row in csv_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# Using pandas
df = pd.read_csv("weather_data.csv")
print(type(df))
print(type(df["temp"]))

data_dict = df.to_dict()
print(data_dict)

temp_list = df["temp"].to_list()
print(len(temp_list))

print(df["temp"].mean())
print(df["temp"].max())

# Get Data in Columns
print(df["condition"])
print(df.condition)

# Get Data in Row
print(df[df.day == "Monday"])
print(df[df.temp == df.temp.max()])

# Get Row data value
monday = df[df.day == "Monday"]
monday_temp = int(monday.temp.iloc[0])
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
students_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
students_df = pd.DataFrame(students_dict)
students_df.to_csv("new_data.csv", index=False)

# 1. View the data
print("Full Data:")
print(df)
print("\nFirst 5 rows:")
print(df.head())

# 2. Get summary statistics
print("\nSummary statistics:")
print(df.describe())

# 3. Access columns
print("\nTemperature column:")
print(df["temp"])

# 4. Filter data
print("\nDays with temperature > 20:")
print(df[df["temp"] > 20])

# 5. Calculate averages
print("\nAverage temperature:")
print(df["temp"].mean())

# 6. Find max/min values
print("\nDay with highest temperature:")
print(df[df["temp"] == df["temp"].max()])

# 7. Convert data (Celsius to Fahrenheit)
df["temp_F"] = df["temp"] * 9/5 + 32
print("\nData with Fahrenheit column:")
print(df)

# 8. Create new columns
df["is_warm"] = df["temp"] > 20
print("\nData with 'is_warm' column:")
print(df)

# 9. Plot data (requires matplotlib)
df.plot(x="day", y="temp", kind="line", marker="o", title="Temperature by Day")
plt.show()

# 10. Export data
df.to_csv("weather_data_modified.csv", index=False)

# 11. Group and aggregate (if you have a 'condition' column)
if "condition" in df.columns:
    print("\nAverage temp by condition:")
    print(df.groupby("condition")["temp"].mean())

# 12. Handle missing data
print("\nData with missing values filled (if any):")
print(df.fillna(0))