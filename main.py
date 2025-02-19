from re import search
from tkinter import *  # Import all classes and functions from Tkinter for GUI
from tkinter import messagebox  # Import messagebox for displaying alert dialogs
import random  # Import random module for generating passwords
import pyperclip  # Import pyperclip to copy text to the clipboard
import json

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
    site = website_entry.get().title()  # Get website input
    email = email_entry.get()  # Get email input
    password = password_entry.get()  # Get password input


    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }
    # Check if any field is empty
    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(message="Please do not leave any fields empty!")  # Show warning message
    else:
        try:
            with open("password_manager.json", "r") as data_file:
                data = json.load(data_file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("password_manager.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("password_manager.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)  # Clear website entry field
            email_entry.delete(0, END)  # Clear email entry field
            password_entry.delete(0, END)  # Clear password entry field


# ---------------------------- SEARCH INFO ------------------------------- #
def search_info():
    site = website_entry.get().title()  # Get website input

    try:
        with open("password_manager.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if site in data:
            email = data[site]["email"]
            password = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"You have not saved information for {site}!")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Create main window
window.title("Password Manager")  # Set window title
window.config(padx=50, pady=50)  # Add padding to the window

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
website_entry.grid(row=1, column=1)  # Position entry field
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

search_button = Button(text="Search", width=13, command=search_info)
search_button.grid(row=1, column=2)

window.mainloop()  # Run the main event loop
