import pyshorteners
from tkinter import *

#function to retrieve long email as input
def get_long_url():
    og_url = f"{url.get()}"
    shorten_url(og_url)

#function to shorten the url
def shorten_url(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    shorturl.config(text=short_url)
    guiWindow.clipboard_clear()
    guiWindow.clipboard_append(short_url)
    textlabel2.config(text="Short URL copied!!")

#initialing gui window configuration
guiWindow = Tk()
guiWindow.title("URL Shortener")
guiWindow.geometry("600x300")
guiWindow.config(bg="#FAF9F6")
guiWindow.resizable(width=False, height=False)

#gui window labels
textlabel = Label(
    guiWindow,
    text="Enter the long url: ",
    fg="black",
    font=("Arial", 15)
)
textlabel.place(x=60,y= 45)

url = StringVar()

longurl = Entry(
    guiWindow,
    textvariable=url,
    bg="#FEFBD8",
    width=50,
    font=("Arial", 15)
)
longurl.place(x=35,y=80)

submit = Button(
    guiWindow,
    text="Get Short URL",
    fg="white",
    bg="blue",
    width=12,
    command=get_long_url,
    font=("Arial", 13)
)
submit.place(x=60, y=120)

shorturl = Label(
    guiWindow,
    text="",
    fg="black",
    bg="#FAF9F6",
    font=("Arial", 15)
)
shorturl.place(x=150,y=180)

textlabel2 = Label(
    guiWindow,
    text="",
    fg="black",
    bg="#FAF9F6",
    font=("Arial", 15)
)
textlabel2.place(x=150,y= 211)

#starting the gui window main loop
guiWindow.mainloop()




