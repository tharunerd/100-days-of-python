# 🎉 Day 32 - Automated Birthday Wisher 🎂

This is my **Day 32** project from the **100 Days of Python Course by Angela Yu**.  
It’s a **Python automation tool** that sends **personalized birthday emails** to people from a `.csv` file, using pre-made letter templates.  
I even hosted it on **PythonAnywhere** so it runs daily in the cloud — no need to run it manually! 🚀
A step into automating scripts.

---

## 📌 Features

- Reads a **CSV file** containing names, emails, and birth dates.
- Checks **daily** if it’s someone’s birthday.
- Picks a **random letter template** and replaces placeholders with the person’s name.
- Sends the birthday email **automatically** via SMTP.
- Can be run **locally** or hosted on the cloud (**PythonAnywhere**).
- Easy to update with new people or templates.

---

## 🗂 Project Structure
```

📂 birthday\_wisher
├── main.py                  # Main script
├── birthdays.csv             # List of people with names, emails, and birthdays
├── letter\_templates/         # Folder containing birthday letter templates
  ├── letter\_1.txt
  ├── letter\_2.txt
  └── letter\_3.txt

due to personal info added in my .csv file I have added it to .gitignore along with my .env file which conatins my email and its password
````

---

## ⚙️ How It Works
1. **Data Source** → The script reads `birthdays.csv` for names, emails, and birth dates.
2. **Date Check** → Compares today’s date with each entry’s birthday.
3. **Template Customization** → Picks a random `.txt` file from `letter_templates/` and replaces `[NAME]` with the person’s actual name.
4. **Email Sending** → Uses Python's `smtplib` to send the customized message.
5. **Automation** → Hosted on [PythonAnywhere](https://www.pythonanywhere.com/) to run daily.

---

## 📄 CSV Format
Your `birthdays.csv` should look like this:

```csv
name,email,year,month,day
John Doe,johndoe@example.com,1995,8,14
Jane Smith,janesmith@example.com,1998,5,23
````

---

## ✉️ Letter Template Format

Example (`letter_1.txt`):

```
Dear [NAME],

Wishing you the happiest birthday ever! 🎉

Best wishes,
Your Friend
```

The `[NAME]` placeholder will be replaced with the actual name from the CSV.

---

## 🚀 Running the Project

### Run Locally

1. Clone the repo:

   ```bash
   git clone https://github.com/tharunerd/one-hundred-days-of-python.git
   ```
2. Navigate to the project folder:

   ```bash
   cd day_32
   ```
3. Install requirements (if any):

   ```bash
   pip install pandas
   ```
4. Update `birthdays.csv` and letter templates as needed.
5. Run the script:

   ```bash
   python main.py
   ```

### Run in the Cloud

1. Sign up on [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload your files.
3. Schedule the script to run daily under **Tasks**.
4. That’s it — your birthday wishes are sent automatically! 🎉

---

## 🛠 Technologies Used

* **Python 3**
* **Pandas** – For reading and processing CSV files.
* **smtplib** – For sending emails.
* **random** – For selecting a random template.
* **PythonAnywhere** – For cloud hosting.

---

## 🎯 Learning Outcomes

* File handling in Python (`open`, `.read()`, `.write()`).
* Working with CSV files using Pandas.
* Using Python's `datetime` module for date comparisons.
* Email automation with `smtplib`.
* Deploying and scheduling tasks in the cloud.

---

## 📬 Example Output

If today’s date matches someone’s birthday in the CSV:

```
Email sent to: John Doe (johndoe@example.com)
```

The recipient receives a personalized birthday email.

---

