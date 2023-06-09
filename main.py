from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]

    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    p_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_input.get().title()
    email = e_input.get()
    password = p_input.get()
    new_data = {web: {
        "email": email,
        "password": password
    }}

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!', message='Please do not leave any field empty')
    else:
        try:
            with open('data.json', 'r') as r:

                # TURNS JSON TO PYTHON DICT
                # data = json.load(r)
                # print(data)
                # UPDATES JSON STRUCTURE
                data = json.load(r)

        except FileNotFoundError:
            with open('data.json', "w") as r:
                json.dump(new_data, r, indent=4)
        else:
            data.update(new_data)

            with open('data.json', "w") as r:
                json.dump(data, r, indent=4)

        finally:
            web_input.delete(0, END)
            e_input.delete(0, END)
            p_input.delete(0, END)


def find_password():
    try:
        with open('data.json', 'r') as r:
            data = json.load(r)
            for (key, value) in data.items():
                e = value['email']
                p = value['password']
                website = web_input.get().title()
            if website in key:
                messagebox.showinfo(title='Info', message=f'Email: {e} \nPassword: {p}')
            else:
                messagebox.showinfo(title='Info', message=f'No details for {website} exists.')
    except FileNotFoundError:
        messagebox.showinfo(title='Info', message='No Data File Found')




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)
# LABELS
web = Label(text="Website:", font=("Arial", 8))
web.grid(column=0, row=1)

email = Label(text="Email/Username:", font=("Arial", 8))
email.grid(column=0, row=2)

pw = Label(text="Password:", font=("Arial", 8))
pw.grid(column=0, row=3)

# INPUTS
web_input = Entry()
web_input.grid(column=1, row=1, sticky="w")
web_input.focus()

e_input = Entry()
e_input.grid(column=1, row=2, sticky="ew")


p_input = Entry()
p_input.grid(column=1, row=3, sticky='w')

# BUTTONS
gen_pw = Button(text='Generate Password', padx=0, pady=0, command=generate_password)
gen_pw.grid(column=1, row=3)

add = Button(text='Add', width=44, command=save)
add.grid(column=1, row=4, sticky="ew")

search = Button(text='Search', padx=0, pady=0, command=find_password)
search.grid(column=1, row=1)

window.mainloop()
