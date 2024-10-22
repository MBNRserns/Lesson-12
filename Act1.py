from tkinter import *
from gtts import gTTS
import os

def click():
    language = "en"
    myobj=gTTS(text=entry.get(),lang=language,slow=False)
    myobj.save("Text_to_Speech.wav")
    os.system("Text_to_Speech.wav")

root=Tk()
root.title("Text to Speech Conversion")
root.geometry("700x500")

frame1=Frame(root, bg="red", height="140")
frame1.pack(fill=X)

frame2=Frame(root,bg="yellow", height="220")
frame2.pack(fill=X)

frame3=Frame(root,bg="red", height="140")
frame3.pack(fill=X)

txt=Label(frame1, text="Text to Speech", font="bold, 35", bg="red")
txt.place(x=180, y=50)

entry=Entry(frame2, width= 45, bd= 4, font= 14)
entry.place(x=140, y=50)

btn=Button(frame2, text="Submit", width= 15, bg="orange", font="bold, 24", command=click)
btn.place(x=200, y=120)

root.mainloop()