import random
import tkinter as tk
from tkinter import messagebox
import pyperclip

LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

def generate_password(length, use_lower, use_upper, use_numbers, use_symbols):
    characters = ''
    if use_lower:
        characters += LOWERCASE
    if use_upper:
        characters += UPPERCASE
    if use_numbers:
        characters += NUMBERS
    if use_symbols:
        characters += SYMBOLS

    if not characters:
        messagebox.showerror("Error", "No character types selected!")
        return ''

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid length input!")
        return
    password = generate_password(length, use_lower.get(), use_upper.get(), use_numbers.get(), use_symbols.get())
    result_label.config(text=password)

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

use_lower = tk.BooleanVar()
use_upper = tk.BooleanVar()
use_numbers = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Lowercase", variable=use_lower).pack()
tk.Checkbutton(root, text="Include Uppercase", variable=use_upper).pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).pack()

generate_button = tk.Button(root, text="Generate Password", command=display_password)
generate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
