from tkinter import *
import datetime as dt
import time
import pyaudio
import wave
from threading import Thread

#clock module
def update_clock():
    current_time_1 = dt.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time_1)
    guiWindow.after(1000, update_clock)  # Update the clock label every second

#alarm module
def alarm(set_alarm_timer):
    global set_alarm
    while set_alarm==True:
        time.sleep(1)
        actual_time = dt.datetime.now()
        current_time = actual_time.strftime("%H:%M:%S")
        the_message = "Current Time: " + str(current_time)
        print(the_message)
        if current_time in set_alarm_timer:
            stream.start_stream() #plays alarm sound
            break
#creates a thread for running the alarm function
def start_alarm_func():
    th = Thread(target=get_alarm_time)
    th.start()            

#gets input from user
def get_alarm_time():
    global set_alarm
    set_alarm=True
    alarm_set_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(alarm_set_time)
    
#stops the alarm sound
def stop():
    global set_alarm
    set_alarm=False
    stream.stop_stream()

guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("600x300")
guiWindow.config(bg="#87BDD8")
guiWindow.resizable(width=False, height=False)

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="white",
    bg="#36486B",
    font=("Arial", 15)
)
timeFormat.place(x=170, y=200)

timeFormat = Label(
    guiWindow,
    text="Current Time",
    fg="white",
    bg="#36486B",
    font=("Arial", 15)
)
timeFormat.place(x=46, y=70)

clock_label = Label(
    guiWindow,
    text="",
    fg="white",
    bg="#87BDD8",
    font=("Arial", 15)
)
clock_label.place(x=56, y=110)

add_time = Label(
    guiWindow,
    text=" Hour     Minute   Second",
    font=("Arial", 15),
    fg="white",
    bg="#87BDD8"
)
add_time.place(x=220, y=50)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm:",
    fg="white",
    bg="#034F84",
    relief="solid",
    font=("Helvetica", 13, "bold")
)
setAlarm.place(x=249, y=14)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="#FEFBD8",
    width=4,
    font=("Arial", 20)
)
hourTime.place(x=220, y=90)

minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="#FEFBD8",
    width=4,
    font=("Arial", 20)
)
minuteTime.place(x=297, y=90)

secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="#FEFBD8",
    width=4,
    font=("Arial", 20)
)
secondTime.place(x=374, y=90)

submit = Button(
    guiWindow,
    text="Start The Alarm",
    fg="white",
    bg="#82B74B",
    width=12,
    command=start_alarm_func,
    font=("Arial", 13)
)
submit.place(x=202, y=150)

submit = Button(
    guiWindow,
    text="Stop The Alarm",
    fg="white",
    bg="#82B74B",
    width=12,
    command=stop,
    font=("Arial", 13)
)
submit.place(x=340, y=150)


update_clock()  # Start the clock updating module

#importing audio file
wf = wave.open('D:\Internship\\bedside-clock-alarm-95792.wav', 'rb') #replace with correct path of audio file

#initialising pyaudio and defining callback function
p = pyaudio.PyAudio()
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open stream using callback
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
stream.stop_stream()
set_alarm=True
guiWindow.mainloop()


