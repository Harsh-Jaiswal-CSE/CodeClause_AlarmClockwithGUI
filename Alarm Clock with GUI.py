from time import strftime
from tkinter import *
import time
import datetime
from pygame import mixer

root = Tk()
root.title("Personal Alarm-Clock")

def setalarm():
    alarmtime = f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if (alarmtime != "::"):
        alarmclock(alarmtime)

def alarmclock(alarmtime):
    while True:
        time.sleep(1)
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now == alarmtime:
            Wakeup = Label(root, font=('arial', 20, 'bold'), text="Wake up Champion!", bg="DodgerBlue2",
                           fg="white").grid(row=6, columnspan=3)
            print("Wake up Coder!")
            mixer.init()

            mixer.music.load(
                r'C:\Users\acer\Downloads\alarm.mp3')

            mixer.music.play()
            break

hrs  = StringVar()
mins = StringVar()
secs = StringVar()

greet0 = Label(root, font=('arial', 20, 'bold'), text="Enter Time of Alarm").grid(row=1, columnspan=5)
greet1 = Label(root, font=('arial', 20, 'bold'), text="Enter   Hrs:").grid(row=2, columnspan=1)

hrbtn  = Entry(root, textvariable=hrs, width=5, font=('arial', 20, 'bold')).grid(row=2, column=1)
greet2 = Label(root, font=('arial', 20, 'bold'), text="Enter Mins:").grid(row=3, columnspan=1)

minbtn = Entry(root, textvariable=mins, width=5, font=('arial', 20, 'bold')).grid(row=3, column=1)
greet3 = Label(root, font=('arial', 20, 'bold'), text="Enter Secs:").grid(row=4, columnspan=1)

secbtn = Entry(root, textvariable=secs, width=5, font=('arial', 20, 'bold')).grid(row=4, column=1)
secbtn = Button(root, text="Set Alarm", command=setalarm, bg="DodgerBlue2", fg="white",font=('arial', 18, 'bold')).grid(row=5, columnspan=1)


timeleft = Label(root, font=('arial', 20, 'bold'))
timeleft.grid()

mainloop()