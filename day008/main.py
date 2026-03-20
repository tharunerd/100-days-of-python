# Caesar cipher


def caesar(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            if direction == "encode":
                result += chr((ord(char) - base + shift_amount) % 26 + base)
            elif direction == "decode":
                result += chr((ord(char) - base - shift_amount) % 26 + base)
        else:
            result += char
    return result

print("start")
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    result = caesar(text, shift, direction)
    print(f"Here's the {direction}d result: {result}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye")


