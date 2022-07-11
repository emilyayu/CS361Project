# Name:         Emily Yu
# OSU Email:    yuemi@oregonstate.edu
# Course:       CS361 - Intro to Software Engineering
# Assignment:   Project
# Description:  UI and data extractor


# Import Module
import time
import random
from tkinter import *
import tkinter as tk
import tkinter.font as font
import json
from tkinter import ttk
from tkinter import messagebox

# import prng
# import imgsrv



# create root window
root = Tk()
root.title('Where Should I Eat in Los Angeles?')
font_xlarge = font.Font(family='Georgia', size='18', weight='bold')
font_large = font.Font(family='Georgia', size='14', weight='bold')
font_small = font.Font(family='Georgia', size='12')
# frame = Label(
#     root,
#     text='Choose a Restaurant in Los Angeles',
#     # bg='white',
#     font=20
# )
#
# frame.pack()


root.geometry('500x500')

img = PhotoImage(file="C:/Users/litod/PycharmProjects/CS361/Project/background-T.png")  # changes the background
label = Label(
    root,
    image=img
)
label.place(x=-50, y=-400)
# root['background'] = 'white'
app_title = tk.Label(root, text='Choose a Restaurant in Los Angeles', font=font_xlarge)
app_title.pack(pady= 25, side = TOP )
price_frame = tk.Frame(root)
price_frame.pack(padx =30,pady=15, expand=1)
cuisine_frame = tk.Frame(root)
rating_frame = tk.Frame(root)



def change_to_price_frame():
    """This function swaps from second frame (cuisine preferences) to first frame (price preferences)"""
    cuisine_frame.forget()
    price_frame.pack(padx =30,pady=20, expand=1)


def change_to_cuisine_frame():
    """This function swaps from first frame (price preferences) to second frame (cuisine preferences)"""
    price_frame.forget()
    cuisine_frame.pack(fill='both', expand = 1)#padx =30,pady=20, expand=1)






######
# Sorts Restaurants in Los Angeles by Price
######
possible_results = []
open('Step1-Price.json', 'w').close()


def clicked():
    price_selection = (selected.get())
    if price_selection == 1:
        search_price = '$'
    elif price_selection == 2:
        search_price = '$$'
    elif price_selection == 3:
        search_price = '$$$'
    elif price_selection == 4:
        search_price = '$$$$'
    else:
        search_price = 'All Possible'
        return change_to_cuisine_frame()
    f = open('C:/Users/litod/PycharmProjects/CS361/Project/RestaurantData.json')
    data = json.load(f)
    for i in range(len(data)):
        if data[i]['Price_Range'] == search_price:
            possible_results.append(data[i])
        elif search_price == 'All Possible':
            possible_results.append(data[i])
    f.close()
    with open('Step1-Price.json', 'w') as outfile:
        json.dump(possible_results, outfile)
    return change_to_cuisine_frame()


## Price Preferences

# radio Button Options
price_values = {'$ : $0-$10': '1',
                '$$ : $10-$30': '2',
                '$$$ : $30-$50': '3',
                '$$$$ : $50 +': '4',
                'No Preference': '5'}
selected = IntVar()
lbl_price_preference = tk.Label(price_frame, text='Price Preference Per Entree', font=font_large)
lbl_price_preference.pack(padx = 15, pady = 40)
price_frame.pack(pady=50)
# price_frame.place(x=50, y=50)

for (text, value) in price_values.items():
    r = Radiobutton(price_frame,
                    text=text,
                    variable=selected,
                    value=value,
                    # indicator=0,
                    # background="light blue"
                    )
    r.pack(anchor=W)

Button(price_frame, text='Next', command=clicked, padx=15, pady=5) \
    .pack(ipadx=5, ipady=15, expand=True)

exit = Button(root, text="Exit", fg="black", command=root.destroy) \
    .pack(side=BOTTOM)

# Execute Tkinter
root.mainloop()