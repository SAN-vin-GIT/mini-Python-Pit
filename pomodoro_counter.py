import math
from tkinter import *
from venv import create


# Colors
green = "#C1BAA1"
red="#9F5255"
txt_green = "#3E7B27"
magenta = "#AA5486"


#----Constraints----#

FONT_NAME = "Poppins"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None



# reset timer
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    heading.config(text="Mindful Minutes", bg=green, fg=red, font=(FONT_NAME, 28, "bold"))
    a_label.config(text = "")
    global reps
    reps = 0

# timer mechanism
def start_timer():
    global reps
    reps += 1
    count_down(5 * 60)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="Take a Break",bg=green,fg=txt_green, font=(FONT_NAME,28,"bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="Take a Break", bg=green, fg=magenta, font=(FONT_NAME, 28, "bold"))
    else:
        count_down(work_sec)
        heading.config(text="Get Back to Work", bg=green, fg=red, font=(FONT_NAME, 28, "bold"))


# Countdown
# this counter creatively counts down by using window.after which takes 1000ms which is 1 second and loops backwards
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1 )
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
            a_label.config(text = marks,bg=green,fg=red, font=(FONT_NAME,28,"bold"))




# UI SETUP
window = Tk()
window.title("Mindful Minutes")
window.config(padx=100,pady=50,bg=green)



heading = Label(text="Mindful Minutes",bg=green,fg=red, font=(FONT_NAME,28,"bold"))
heading.grid(row = 0, column = 1)

canvas = Canvas(width=250,height =250,bg=green, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(100,130,text = "OO:OO", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)



start = Button(text="START",bg=green,highlightthickness=0, font=(FONT_NAME,28,"bold"), command=start_timer)
start.grid(row=2, column=0)

a_label = Label(bg=green,fg=red, font=(FONT_NAME,28,"bold"))
a_label.grid(row = 3, column = 1)

reset = Button(text="RESET",bg=green,highlightthickness=0, font=(FONT_NAME,28,"bold"), command=reset_timer)
reset.grid(row=2, column=2)





window.mainloop()
