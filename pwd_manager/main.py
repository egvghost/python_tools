from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

json_file_path = "./data.json"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
  pwd_length = int(pwd_len_field.get())
  lc_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  uc_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '?', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_']
  pwd_list = []

  while len(pwd_list) < pwd_length:
    if len(pwd_list) < 4 or randint(0, 1) == 1:
      pwd_list.append(choice(lc_letters))
    if (len(pwd_list) < 4 or randint(0, 1) == 1) and len(pwd_list) < pwd_length:
      pwd_list.append(choice(uc_letters))
    if (len(pwd_list) < 4 or randint(0, 1) == 1) and len(pwd_list) < pwd_length:
      pwd_list += choice(symbols)
    if (len(pwd_list) < 4 or randint(0, 1) == 1) and len(pwd_list) < pwd_length:
      pwd_list += choice(numbers)

  shuffle(pwd_list)
  password = "".join(pwd_list)

  pwd_field.delete(0, END)
  pwd_field.insert(0, password)
# ---------------------------- SAVE DATA ------------------------------- #
def save():
  website = web_field.get()
  username = usr_field.get()
  password = pwd_field.get()
  if len(website) == 0 or len(username) == 0 or len(password) == 0:
    messagebox.showinfo(message="You can't provide empty fields")
  else:
    data = {
      website: {
        "username": username,
        "password": password
      }
    }
    try:
      with open(json_file_path, "r") as data_file:
        json_data = json.load(data_file)
    except FileNotFoundError:
      with open(json_file_path, "w") as data_file:
        json.dump(data, data_file, indent=4)
    else:
      json_data.update(data)
      with open(json_file_path, "w") as data_file:
        json.dump(json_data, data_file, indent=4)
    finally:
      web_field.delete(0, END)
      usr_field.delete(0, END)
      pwd_field.delete(0, END)
      messagebox.showinfo(message="The data was saved in the vault")
# ---------------------------- SEARCH DATA------------------------------- #
def search():
  website = web_field.get()
  try:
    with open(json_file_path, "r") as data_file:
      json_data = json.load(data_file)
  except FileNotFoundError:
    messagebox.showerror(title="Search error", message="Data file not found")
  else:
    try:
      messagebox.showinfo(title=website, message=f"Username: {json_data[website]['username']}\nPassword: {json_data[website]['password']}")
    except KeyError:
      messagebox.showwarning(title="Missing info", message=f"No information found for '{website}'")
    else:
      web_field.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

logo_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(130, 100, image=logo_image)
canvas.grid(row=1, column=2)

web_label = Label(text="Website", pady=10)
web_label.grid(row=2, column=1)

web_field = Entry(width=26)
web_field.grid(row=2, column=2, columnspan=2)
web_field.focus()

search_button = Button(text="Search", width=4, command=search)
search_button.grid(row=2, column=4)

usr_label = Label(text="Username", pady=10)
usr_label.grid(row=3, column=1)

usr_field = Entry(width=34)
usr_field.grid(row=3, column=2, columnspan=3)

pwd_label = Label(text="Password", pady=10)
pwd_label.grid(row=4, column=1)

pwd_field = Entry(width=21)
pwd_field.grid(row=4, column=2)

var = IntVar(value=12)
pwd_len_field = Spinbox(from_=8, to=20, increment=1, textvariable=var, width=2)
pwd_len_field.grid(row=4, column=3)

pwd_gen_button = Button(text="Generate", width=4, command=generate_pwd)
pwd_gen_button.grid(row=4, column=4)

add_button = Button(text="Add", width=31, command=save)
add_button.grid(row=5, column=2, columnspan=3)

window.mainloop()
