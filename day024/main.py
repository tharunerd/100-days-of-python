import os

PLACEHOLDER = "[name]"

names_path = r"day_24\Input\Names\invited_names.txt"
letter_path = r"day_24\Input\Letters\starting_letter.txt"
output_dir = r"day_24\Output"

os.makedirs(output_dir, exist_ok=True)

with open(names_path) as names_file:
    names = names_file.readlines()

with open(letter_path) as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        output_path = os.path.join(output_dir, f"letter_for_{stripped_name}.txt")
        with open(output_path, mode="w") as completed_letter:
            completed_letter.write(new_letter)

