from tkinter import *
import datetime
import time
import os

def play_sound():
    os.system("aplay sound.wav")

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm_timer:
            print('Wake Up!')
            play_sound()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

root = Tk()
root.title("Alarm Clock")
hour = IntVar()
min = IntVar()
sec = IntVar()
hour_label = Label(root, text="Hour")
hour_label.grid(row=0, column=0)
hour_entry = Entry(root, textvariable=hour)
hour_entry.grid(row=0, column=1)
min_label = Label(root, text="Minute")
min_label.grid(row=1, column=0)
min_entry = Entry(root, textvariable=min)
min_entry.grid(row=1, column=1)
sec_label = Label(root, text="Second")
sec_label.grid(row=2, column=0)
sec_entry = Entry(root, textvariable=sec)
sec_entry.grid(row=2, column=1)
alarm_button = Button(root, text="Set Alarm", command=actual_time)
alarm_button.grid(row=3, column=0, columnspan=2)

root.mainloop()