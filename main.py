import tkinter

#### First Part of day-27#####

# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize (width=500, height=300)
#
# #label
# my_label = tkinter.Label(text="I'm a label",font=("Arial",24,"bold"))
# my_label.grid(column=0,row=0)
# def clicked_me():
# 	print(" I'm Clicked !!")
# 	my_label['text'] = my_input.get()
# #Button
# my_button_1 = tkinter.Button(text="Click Me",command=clicked_me)
# my_button_1.grid(column=1,row=1)
#
# my_button_2 = tkinter.Button(text="Click Me",command=clicked_me)
# my_button_2.grid(column=2,row=0)
#
# #Input Entry
# my_input = tkinter.Entry()
# my_input.grid(column=3,row=2)

#### Last Part of day-27#####
import tkinter


def clicked_me():
	print(" I'm Clicked !!")
	miles = float(top_input.get())
	km = miles * 1.609344
	mid_label.config(text=f"{km}")

# Window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

# Top Entry Widget
top_input = tkinter.Entry(width=7)
top_input.grid(column=1, row=0)


# Top label Widget
top_label = tkinter.Label(text="Miles")
top_label.grid(column=2, row=0)


# Middle label Left Widget
midleft_label = tkinter.Label(text="Is equal to")
midleft_label.grid(column=0, row=1)


# Mid label Widget
mid_label = tkinter.Label(text="0")
mid_label.grid(column=1, row=1)


# Middle label Right Widget
midright_label = tkinter.Label(text="Km")
midright_label.grid(column=2, row=1)


# Button
my_button = tkinter.Button(text="Calculate", command=clicked_me)
my_button.grid(column=1, row=2)


window.mainloop()
# The packer - https://docs.python.org/3/library/tkinter.html#the-packer
# packs all lables on the screen. it's simple way of geometric systems.
