from tkinter import *

def button_clicked():
    """takes in input from entry and calculates then changes outputs"""
    user_in = float(entry.get())
    kilometers = round(user_in * 1.60934)
    output_label.config(text = kilometers)



window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150,height=100)
window.config(padx=25,pady=25)

entry = Entry(width=15)
entry.grid(row=0, column=1)


a_label = Label(text="Miles", font=("Arial",18,"bold"))
a_label.grid(row = 0, column = 2)

b_label = Label(text="is equal to", font=("Arial",18,"bold"))
b_label.grid(row = 1, column =0)

output_label = Label(text=" 0 ", font=("Arial",18,"bold"))
output_label.grid(row = 1, column =1)

c_label = Label(text="Km", font=("Arial",18,"bold"))
c_label.grid(row = 1, column =2)

button = Button(text="Calculate", command = button_clicked)
button.grid(row=2, column=1)





window.mainloop()
