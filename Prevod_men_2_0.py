from tkinter import *
import requests

MAIN_COLOR = "#0e1b23"

main_window = Tk()
main_window.minsize(420, 300)
main_window.resizable(False, False)
main_window.title("Převodník měn")
main_window.config(bg=MAIN_COLOR)


def count():
    try:
        currency = drop_menu.get()
        amount = float(user_input.get())

        urlczk = f"https://api.apilayer.com/exchangerates_data/convert?to=CZK&from={currency}&amount={amount}"
        urlusd = f"https://api.apilayer.com/exchangerates_data/convert?to=USD&from={currency}&amount={amount}"
        urleur = f"https://api.apilayer.com/exchangerates_data/convert?to=EUR&from={currency}&amount={amount}"
        urlgbp = f"https://api.apilayer.com/exchangerates_data/convert?to=GBP&from={currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "wYPSksMdMYSjqqf6GLm8WOMEtFx9ewFh"
        }

        responseczk = requests.request("GET", urlczk, headers=headers, data=payload)
        responseusd = requests.request("GET", urlusd, headers=headers, data=payload)
        responseeur = requests.request("GET", urleur, headers=headers, data=payload)
        responsegbp = requests.request("GET", urlgbp, headers=headers, data=payload)

        resultczk = responseczk.json()
        resultusd = responseusd.json()
        resulteur = responseeur.json()
        resultgbp = responsegbp.json()

        czech.config(text=resultczk["result"])
        dollars.config(text=resultusd["result"])
        euro.config(text=resulteur["result"])
        pounds.config(text=resultgbp["result"])
    except:
        header_notification.config(text="Zadejte platnou částku.")


first_frame = Frame(main_window, bg=MAIN_COLOR)
first_frame.pack()
second_frame = Frame(main_window, bg=MAIN_COLOR)
second_frame.pack()

header = Label(first_frame, text="Jakou částku a měnu chcete převést?", bg=MAIN_COLOR, fg="white",
               font=("Arial", 15, "bold"), pady=10)
header.pack()

header_notification = Label(first_frame)
header.pack()

user_input = Entry(second_frame)
user_input.grid(row=0, column=0, padx=10)

drop_menu = StringVar(second_frame)
drop_menu.set("CZK")
drop_menu_options = OptionMenu(second_frame, drop_menu, "CZK", "USD", "GBP", "EUR")
drop_menu_options.grid(row=0, column=1)

confirm_button = Button(second_frame, text="Převést", command=count)
confirm_button.grid(row=0, column=2)

czech = Label(second_frame, bg=MAIN_COLOR, fg="white", font=("Arial", 20))
czech.grid(row=1, column=0)
dollars = Label(second_frame, bg=MAIN_COLOR, fg="white", font=("Arial", 20))
dollars.grid(row=2, column=0)
pounds = Label(second_frame, bg=MAIN_COLOR, fg="white", font=("Arial", 20))
pounds.grid(row=3, column=0)
euro = Label(second_frame, bg=MAIN_COLOR, fg="white", font=("Arial", 20))
euro.grid(row=4, column=0)

czk = Label(second_frame, text="CZK", bg=MAIN_COLOR, fg="white", font=("Arial", 20), pady=5)
czk.grid(row=1, column=2)
usd = Label(second_frame, text="USD", bg=MAIN_COLOR, fg="white", font=("Arial", 20), pady=5)
usd.grid(row=2, column=2)
gbp = Label(second_frame, text="GBP", bg=MAIN_COLOR, fg="white", font=("Arial", 20), pady=5)
gbp.grid(row=3, column=2)
eur = Label(second_frame, text="EUR", bg=MAIN_COLOR, fg="white", font=("Arial", 20), pady=5)
eur.grid(row=4, column=2)

main_window.mainloop()
