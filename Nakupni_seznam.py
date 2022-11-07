from tkinter import *

# Main window
main_window = Tk()
main_window.title("Nákupní seznam")
main_window.minsize(450, 350)
main_window.resizable(False, False)

# Colors and fonts
main_color = "#0e1b23"
main_font = ("Helvetica", 15)
button_font = ("Helvetica", 11)
button_color = "#fdf"
main_window.config(bg=main_color)


# Functions
def add_text_to_list():
    content_list.insert(END, user_input.get())
    user_input.delete(0, END)


def remove_text_from_list():
    content_list.delete(ANCHOR)


def clear_all_from_list():
    content_list.delete(0, END)


def save_list():
    with open("save.txt", "w") as file:
        contentlist = content_list.get(0, END)
        for one in contentlist:
            if one.endswith("\n"):
                file.write(f"{one}")
            else:
                file.write(f"{one}\n")


def open_save_list():
    with open("save.txt", "r") as file:
        for line in file:
            content_list.insert(END, line)


# Frames
first_frame = Frame(main_window, bg=main_color)
first_frame.pack()
second_frame = Frame(main_window, bg=main_color)
second_frame.pack()
third_frame = Frame(main_window, bg=main_color)
third_frame.pack()

# First frame
user_input = Entry(first_frame, width=26, borderwidth=3, font=main_font)
user_input.grid(row=0, column=0)
add_button = Button(first_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_color,
                    command=add_text_to_list)
add_button.grid(row=0, column=1, padx=15, pady=15)

# Scroll bar
content_scroll_bar = Scrollbar(second_frame)
content_scroll_bar.grid(row=0, column=1, sticky=N + S)

# Second frame
content_list = Listbox(second_frame, width=35, borderwidth=3, font=main_font, yscrollcommand=content_scroll_bar.set)
content_list.grid(row=0, column=0)
content_scroll_bar.config(command=content_list.yview)

# Third frame
remove_button = Button(third_frame, text="Odstranit řádek", borderwidth=2, font=button_font, command=remove_text_from_list)
remove_button.grid(row=0, column=0, padx=2, pady=10)
all_remove_button = Button(third_frame, text="Smazat seznam", borderwidth=2, font=button_font, command=clear_all_from_list)
all_remove_button.grid(row=0, column=1, padx=2, pady=10)
save_button = Button(third_frame, text="Uložit změny", borderwidth=2, font=button_font, command=save_list)
save_button.grid(row=0, column=2, padx=2, pady=10)
escape_button = Button(third_frame, text="Zavřít", borderwidth=2, font=button_font, command=main_window.destroy)
escape_button.grid(row=0, column=3, padx=2, pady=10)

# Save list load
open_save_list()

# Main cycle
main_window.mainloop()
