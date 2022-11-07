from tkinter import *

# Window
main_window = Tk()
main_window.title("Převod měn")
main_window.minsize(200, 200)
main_window.resizable(False, False)
main_window.config(bg="#0e1b23")
main_window.iconbitmap("ico.ico")


# Function
def count():
    eur = float(user_input.get()) / 24.360
    result_eur_label["text"] = round(eur, 2)
    usd = float(user_input.get()) / 24.474
    result_dollars_label["text"] = round(usd, 2)
    gbp = float(user_input.get()) / 27.847
    result_pounds_label["text"] = round(gbp, 2)


# Input
user_input = Entry(width=10, font=("Arial", 15))
user_input.grid(row=0, column=0, padx=10, pady=10)

# Labels
czk_label = Label(text="CZK", bg="#0e1b23", fg="white", font=("Arial", 20))
czk_label.grid(row=0, column=1)

eur_label = Label(text="EUR", bg="#0e1b23", fg="white", font=("Arial", 20))
eur_label.grid(row=1, column=1)
result_eur_label = Label(text="0", bg="#0e1b23", fg="white", font=("Arial", 20))
result_eur_label.grid(row=1, column=0)

dollars_label = Label(text="USD", bg="#0e1b23", fg="white", font=("Arial", 20))
dollars_label.grid(row=2, column=1)
result_dollars_label = Label(text="0", bg="#0e1b23", fg="white", font=("Arial", 20))
result_dollars_label.grid(row=2, column=0)

pounds_label = Label(text="GBP", bg="#0e1b23", fg="white", font=("Arial", 20))
pounds_label.grid(row=3, column=1)
result_pounds_label = Label(text="0", bg="#0e1b23", fg="white", font=("Arial", 20))
result_pounds_label.grid(row=3, column=0)

# Button
count_button = Button(text="Převést", font=("Arial", 20), command=count)
count_button.grid(row=0, column=2, padx=10, pady=10)

main_window.mainloop()
