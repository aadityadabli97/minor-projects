# GUI Password Generator with JSON and exceptional handling

from tkinter import *
from tkinter import messagebox  # messagebox is not a class , it is a module to it was not imported in * above
import random
import pyperclip  # using pyperclip module we can extend the functionality to copy and paste the password
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters= int(input("How many letters would you like in your password?\n"))
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    # Eazy Level - Order not randomised:
    # e.g. 4 letter, 2 symbol, 2 number = JduE&!91

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    rnl = [random.choice(numbers) for i in range(random.randint(8, 10))]
    rll = [random.choice(letters) for i in range(random.randint(2, 4))]
    rsl = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_list = rll + rsl + rnl
    # print("Easy password")
    easy_password = "".join(password_list)
    # print(f"your easy password is {easy_password}")
    random.shuffle(password_list)
    password = "".join(password_list)
    # print(f"your password is f{password}")
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="Please do not leave any fields empty")
        # open a messagebox prompt to show information
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


def find_password():
    website = website_input.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file found")
    else:
        for key, value in data.items():
            if key == website:
                messagebox.showinfo(title="website",
                                    message=f"Please find your details  : \n \n Email: {data[key]['email']} \n"
                                            f"\n Password : {data[key]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist ")
        # if website in data:
        #     email=data[website]["email"]
        #     password=data[website]["password"]
        #     messagebox.showinfo(title=website,message=f"Email:{email}\n Password={password}")
        # else:
        #     messagebox.showinfo(title="Error",message=f"No details for {website} exist ")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=1)
website_input.focus()  # it is to focus cursor in this field

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_input.insert(0, "abc@gmail.com")  # It is to insert a value into a entry field

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

# buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", bg="#F6F5F5", width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
