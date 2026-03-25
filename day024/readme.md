# Day 24 - Files, Directories & Mail Merge Project ✉️

## 📌 Topics Covered

- Reading from files using Python
- Writing to files (`w`, `a`, `r+` modes)
- Working with relative and absolute paths
- Reading file line-by-line
- Stripping whitespace (`strip()`)
- Using `.replace()` to manipulate string content
- Understanding file handling best practices (e.g., using `with` statement)
- Automating a simple **Mail Merge** project

---

## 🛠 Project: Mail Merge Automation

### 🎯 Goal:
Generate personalized letters for a list of invited guests using a template and names file.

---

### 📂 Files Used:

- `Input/Names/invited_names.txt`: Contains a list of names.
- `Input/Letters/starting_letter.txt`: Template letter containing `[name]` as placeholder.
- Output generated in `Output/ReadyToSend/` folder.

---

### 🔄 Workflow:

1. Read the names from `invited_names.txt`.
2. Open the `starting_letter.txt` template.
3. Replace the placeholder `[name]` with the actual guest name.
4. Save the customized letter as a `.txt` file in the `ReadyToSend/` folder.

---

### 📄 Example Output:

**File Name:** `letter_for_Tharun.txt`

**Content:**
```
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

regrads,
tharun
```