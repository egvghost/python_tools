import tkinter
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
work_sessions = 0
timer = None
# ------------------------------ TIMER RESET ------------------------------ # 
def timer_reset():
  global reps, work_sessions
  window.after_cancel(timer)
  label.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="00:00")
  check_marks.config(text='')
  reps = 0
  work_sessions = 0
# ------------------------------ TIMER MECHANISM ------------------------------ # 
def start_timer():
  global reps
  reps += 1
  if reps in [1,3,5,7]:
    count_down(WORK_MIN * 60)
    label.config(text="WORK", fg=GREEN)
    bring_to_front(window)
  elif reps in [2,4,6]:
    count_down(SHORT_BREAK_MIN * 60)
    label.config(text="BREAK", fg=PINK)
    bring_to_front(window)
  else:
    count_down(LONG_BREAK_MIN * 60)
    label.config(text="BREAK", fg=RED)
    bring_to_front(window)
    reps = 0
# ------------------------------ COUNTDOWN MECHANISM ------------------------------ # 
def count_down(count):
  global work_sessions, timer
  count_minutes = math.floor(count / 60)
  count_seconds = count % 60
  if count_seconds < 10:
    count_seconds = f"0{count_seconds}"
  canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
  if count > 0:
    timer = window.after(1000, count_down, count - 1)
  else:
    start_timer()
    if reps % 2 == 0:
      work_sessions += 1
      check_marks.config(text=("✔" * work_sessions))
# ------------------------------ Bring to front ------------------------------ #
def bring_to_front(window):
    window.attributes('-topmost',True)
    window.attributes('-topmost',False) # disable the topmost attribute after it is at the front to prevent permanent focus 
    window.focus_force() # focus to the window
# ------------------------------ UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodoro")

image = tkinter.PhotoImage(file="./tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image) # shift a bit the x position to properly center the image if required
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

label = tkinter.Label(text="Timer", font=(FONT_NAME, 50), bg= YELLOW, fg=GREEN, pady=20)
label.grid(column=2, row=1)

start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=1, row=3, pady=30)
reset_button = tkinter.Button(text="Reset", highlightbackground=YELLOW, command=timer_reset)
reset_button.grid(column=3, row=3, pady=30)

check_marks = tkinter.Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=4)

window.mainloop()
