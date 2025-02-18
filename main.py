from tkinter import *  # Import all classes and functions from Tkinter for GUI
from tkinter import messagebox  # Import messagebox for displaying alert dialogs
import random  # Import random module for generating passwords
import pyperclip  # Import pyperclip to copy text to the clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function to generate a random password
def generate_password():
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")  # List of letters
    numbers = list("0123456789")  # List of numbers
    symbols = list("!#$%&()*+")  # List of symbols

    nr_letters = random.randint(8, 10)  # Random number of letters
    nr_symbols = random.randint(2, 4)  # Random number of symbols
    nr_numbers = random.randint(2, 4)  # Random number of numbers

    password_list = []  # Empty list to store generated password characters

    # Add random letters to the password list
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    # Add random symbols to the password list
    for char in range(nr_symbols):
        password_list.append(random.choice(symbols))

    # Add random numbers to the password list
    for char in range(nr_numbers):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)  # Shuffle the characters in the list

    password_generated = "".join(password_list)  # Convert list to string

    password_entry.delete(0, END)  # Clear password entry field
    password_entry.insert(0, password_generated)  # Insert generated password into entry field
    pyperclip.copy(password_generated)  # Copy password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Function to save the password to a file
def save():
    site = website_entry.get()  # Get website input
    email = email_entry.get()  # Get email input
    password = password_entry.get()  # Get password input

    # Check if any field is empty
    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave any fields empty!")  # Show warning message
    else:
        # Confirmation dialog before saving
        isOK = messagebox.askokcancel(title=site, message=f"These are the details entered: {email} \nPassword: {password}. \nOK to save?")
        if isOK:
            with open("password_manager.txt", "a") as f:  # Open file in append mode
                f.write(f"{site} | {email} | {password}\n")  # Write details to file
                website_entry.delete(0, END)  # Clear website entry field
                email_entry.delete(0, END)  # Clear email entry field
                password_entry.delete(0, END)  # Clear password entry field

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create main window
window.title("Password Manager")  # Set window title
window.config(padx=20, pady=20)  # Add padding to the window

canvas = Canvas(height=200, width=200)  # Create canvas for displaying an image
logo = PhotoImage(file="logo.png")  # Load image file
canvas.create_image(100, 100, image=logo)  # Display image at center of canvas
canvas.grid(row=0, column=1)  # Place canvas in the grid layout

# Labels
website_txt = Label(text="Website:")  # Create label for website input
website_txt.grid(row=1, column=0)  # Position label in grid

email_txt = Label(text="Email/Username:")  # Create label for email input
email_txt.grid(row=2, column=0)  # Position label in grid

password_txt = Label(text="Password:")  # Create label for password input
password_txt.grid(row=3, column=0)  # Position label in grid

# Entry fields
website_entry = Entry(width=35)  # Create entry field for website
website_entry.grid(row=1, column=1, columnspan=2)  # Position entry field
website_entry.focus()  # Set focus to website entry field

email_entry = Entry(width=35)  # Create entry field for email
email_entry.grid(row=2, column=1, columnspan=2)  # Position entry field

password_entry = Entry(width=21)  # Create entry field for password
password_entry.grid(row=3, column=1)  # Position entry field

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)  # Create button to generate password
generate_button.grid(row=3, column=2)  # Position button

add_button = Button(text="Add", width=36, command=save)  # Create button to save data
add_button.grid(row=4, column=1, columnspan=2)  # Position button

window.mainloop()  # Run the main event loop
