import customtkinter as ctk
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Currency Converter")
root.geometry("400x400")

def format_number(num):
    pass

def get_rates():
    data = requests.get("https://cbu.uz/ru/arkhiv-kursov-valyut/json/").json()
    rates = {"UZS":1}
    for i in data:
        rates[i["Ccy"]] = float(i["Rate"])
    return rates











entry = ctk.CTkEntry(root,placeholder_text="Qiymatini kiriting: ")
entry.pack(pady=10,padx = 30, fill="both")

rates = get_rates()
val_list = list(rates.keys())

from_box = ctk.CTkComboBox(root,values=val_list)
from_box.pack(pady=10,padx = 30, fill="both")
from_box.set("USD")

to_box = ctk.CTkComboBox(root,values=val_list)
to_box.pack(pady=10,padx = 30, fill="both")
to_box.set("UZS")

ctk.CTkButton(root,text="Convert").pack(pady=10,padx = 30, fill="both")

result = ctk.CTkLabel(root,text="")
result.pack(pady=10)

root.mainloop()





