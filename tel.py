import json
import tkinter as tk
from tkinter import messagebox

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def display_contacts():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, f"{contact['first_name']} {contact['last_name']}: {contact['phone']}")

def add_contact():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    phone = entry_phone.get()
    contacts.append({'first_name': first_name, 'last_name': last_name, 'phone': phone})
    save_contacts(contacts)
    display_contacts()
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

def delete_contact():
    selected_index = contacts_listbox.curselection()
    if not selected_index:
        return
    index = selected_index[0]
    deleted_contact = contacts.pop(index)
    save_contacts(contacts)
    display_contacts()
    messagebox.showinfo("Удаление контакта", f"Контакт {deleted_contact['first_name']} {deleted_contact['last_name']} удален.")

app = tk.Tk()
app.title("Телефонный справочник")

contacts = load_contacts()

frame_input = tk.Frame(app)
frame_input.pack(pady=20)

label_first_name = tk.Label(frame_input, text="Имя:")
label_last_name = tk.Label(frame_input, text="Фамилия:")
label_phone = tk.Label(frame_input, text="Телефон:")

entry_first_name = tk.Entry(frame_input)
entry_last_name = tk.Entry(frame_input)
entry_phone = tk.Entry(frame_input)

button_add = tk.Button(frame_input, text="Добавить контакт", command=add_contact)
button_delete = tk.Button(app, text="Удалить контакт", command=delete_contact)

label_first_name.grid(row=0, column=0)
label_last_name.grid(row=1, column=0)
label_phone.grid(row=2, column=0)
entry_first_name.grid(row=0, column=1)
entry_last_name.grid(row=1, column=1)
entry_phone.grid(row=2, column=1)
button_add.grid(row=3, columnspan=2, pady=10)
button_delete.pack(pady=10)

contacts_listbox = tk.Listbox(app, width=50)
contacts_listbox.pack()
display_contacts()

app.mainloop()
