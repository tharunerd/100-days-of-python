import tkinter as tk
from tkinter import messagebox
import json
import random
import string
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()"

    password_list = [random.choice(letters) for _ in range(6)] + \
                    [random.choice(digits) for _ in range(3)] + \
                    [random.choice(symbols) for _ in range(2)]
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # If website exists, update password
    if website in data:
        if messagebox.askyesno(title="Update Entry", message=f"{website} already exists. Update password?"):
            data[website] = new_data[website]
    else:
        data.update(new_data)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    # ✅ NEW FEATURE: Show confirmation popup after saving
    messagebox.showinfo(
        title="Saved Successfully",
        message=f"✅ Saved details for {website}\n\nEmail: {email}\nPassword: {password}\n\nPassword copied to clipboard!"
    )
    pyperclip.copy(password)

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().strip()

    if not website:
        messagebox.showwarning(title="Oops", message="Please enter the website name to search.")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        pyperclip.copy(password)
    else:
        messagebox.showinfo(title="Not Found", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="..\\100-days-of-python\\day030\\logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
tk.Label(text="Website:").grid(row=1, column=0)
tk.Label(text="Email/Username:").grid(row=2, column=0)
tk.Label(text="Password:").grid(row=3, column=0)

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "your_email@example.com")

password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
tk.Button(text="Search", width=13, command=search_password).grid(row=1, column=2)
tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
tk.Button(text="Add", width=36, command=save_password).grid(row=4, column=1, columnspan=2)

window.mainloop()
