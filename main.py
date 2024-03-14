import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_count, text="00:00")
    label.config(text = "Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    tick.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps #important
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    reps += 1
    if reps % 8 == 0:#the 8th rep
        count_down(long_break_sec)
        label.config(text="Long Break", fg = RED)
    elif reps % 2 == 0:# the 2,4,6th rep
        count_down(short_break_sec)
        label.config(text="Short Break",fg = PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time
# after(parent, ms, function = None, *args),
# Parameters:
# parent: is the object of the widget or main window whichever is using this function.
# ms: is the time in milliseconds.
# function: which shall be called.
# *args: other options.

# make it loop through
def count_down(count):
    # you have to specify the object label timer here if you use canvas, but for a window, it's unnecessary.
    if count >= 0:
        count_min = math.floor(count/60)
        count_sec = count % 60
        # dynamic typing
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        if count_min == 0:
            count_min = "00"
    else:# time for next step
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✓"
        tick.config(text=mark, fg=GREEN, bg=YELLOW)

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    global timer # define the timer so that we can cancel it
    timer = window.after(1000, count_down, count-1)
    print(count)
# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer label
label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(column=1, row=0)

# Tick label
tick = tk.Label(text="✓", fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# if there's a white border, use highlightthickness=0
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=tomato_img)
canvas.grid(column=1, row=1)

timer_count = canvas.create_text(101.5, 130, text="00:00", fill="White", font=(FONT_NAME, 32, "bold"))


# Buttons

start_button = tk.Button(text="start", command=start_timer)
start_button.grid(column=2, row=2)
reset_button = tk.Button(text="reset", command=reset_timer)
reset_button.grid(column=0, row=2)

window.mainloop()
