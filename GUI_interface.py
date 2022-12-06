from tkinter import *
import date_calculation as dc

date_first_click = True
year_first_click = True

def get_user_input():
    if date_first_click or year_first_click == True:
        date_label["text"] = "No value Input"
    else:
        user_date_entry = date_entry.get()
        user_month_entry = month_text.get()
        user_year_entry = year_entry.get()

        number_value_month = convert_month_to_digit(user_month_entry)
        day_name = dc.find_the_day(user_date_entry,number_value_month,user_year_entry)
        date_label["text"] = "The day is " + day_name

def convert_month_to_digit(user_input_month):
    
    for each_month in range(len(months)):
        if user_input_month == months[each_month]:
            each_month += 1
            month_digit = str(each_month)
            return month_digit

def date_on_entry_click(event):   
    global date_first_click
    if date_first_click:                 # if this is the first time user clicked it
        date_first_click = False
        date_entry.delete(0, "end") # delete all the text in the entry

def year_on_entry_click(event):
    global year_first_click
    if year_first_click:                 # if this is the first time user clicked it
        year_first_click = False
        year_entry.delete(0, "end") # delete all the text in the entry

window = Tk()
window.geometry("350x300")
window.title("Calander Problem GUI")

label = Label(window, text="Calander Problem GUI", relief="raised")
label.pack(pady="20")

months = [
    "January", 
    "February",
    "March",
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]
month_text = StringVar()
month_text.set("Months")

drop_down_menu = OptionMenu(window,month_text,*months)
drop_down_menu.config(bg="#C0C0C0", fg="BLACK", activebackground="#C0C0F0", activeforeground="BLACK")
drop_down_menu["menu"].config(bg="#C0C0C0", fg="BLACK", activebackground="#C0C0F0")
drop_down_menu.place(x=105,y=56)

date_entry = Entry(relief = SUNKEN, background = "#C0C0C0")
date_entry.insert(0, 'Enter Date...')
date_entry.bind('<FocusIn>', date_on_entry_click)
date_entry.place(y = "60", x = "25", width = 69, height = 25)

year_entry = Entry(relief = SUNKEN, background = "#C0C0C0")
year_entry.insert(0, 'Enter Year (1600-2099)...')
year_entry.bind('<FocusIn>', year_on_entry_click)
year_entry.place(y = "60", x = "200", width = 135, height = 25)

enter_button = Button(window,text="Enter", command = get_user_input)
enter_button.place(y=95,x=150,width=65)

date_label = Label(window,text=" ")
date_label.place(y=125,x=140)

window.mainloop()