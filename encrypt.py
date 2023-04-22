from tkinter import *
from tkinter import messagebox

# Caesar cipher function
def encrypt(text, shift):
    result = ""
    # Loop through each character in the text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Ignore non-alphabetic characters
        else:
            result += char
    return result

# GUI functions
def encrypt_text():
    # Get the input text and shift value from the GUI
    text = input_text.get("1.0", END).strip()
    shift = int(shift_entry.get())
    # Encrypt the text
    encrypted_text = encrypt(text, shift)
    # Display the encrypted text in the output text area
    output_text.delete("1.0", END)
    output_text.insert("1.0", encrypted_text)

def clear_text():
    # Clear the input and output text areas
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)
    # Reset the shift value
    shift_entry.delete(0, END)
    shift_entry.insert(0, "0")

# Create the GUI
root = Tk()
root.title("Caesar Cipher")

# Input text area
input_label = Label(root, text="Input text:")
input_label.pack()
input_text = Text(root, height=5)
input_text.pack()

# Shift value entry
shift_label = Label(root, text="Shift value:")
shift_label.pack()
shift_entry = Entry(root)
shift_entry.pack()
shift_entry.insert(0, "0")

# Encrypt button
encrypt_button = Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack()

# Output text area
output_label = Label(root, text="Encrypted text:")
output_label.pack()
output_text = Text(root, height=5)
output_text.pack()

# Clear button
clear_button = Button(root, text="Clear", command=clear_text)
clear_button.pack()

root.mainloop()
