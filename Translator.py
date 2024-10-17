from tkinter import *
from tkinter import ttk
from googletrans import Translator , LANGUAGES #pip install googletrans

def change(text="type" , src="English" , dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trns =Translator()
    trasn1 = trns.translate(text,src= src1,dest= dest1)
    return trasn1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change(text = msg , src = s,dest = d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("800x700")
root.config(bg="black")
lab_txt = Label(root, text="Translator", font=("Time New Roman",40,"bold"))
lab_txt.place(x=150,y=40, height=80 , width=500)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Detect Language", font=("Time New Roman",20,"bold"))
lab_txt.place(x=150,y=100, height=80 , width=500)

sor_txt = Text(frame, font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=25,y=180, height=150 , width=750)

lst1 = list(LANGUAGES.values())

comb_sor= ttk.Combobox(frame,value = lst1)
comb_sor.place(x=25,y=340, height=30 , width=80)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command=data )
button_change.place(x=125,y=340, height=30 , width=80)

comb_dest= ttk.Combobox(frame,value = lst1)
comb_dest.place(x=225,y=340, height=30 , width=80)
comb_dest.set("English")


dest_txt = Label(root, text="Translation", font=("Time New Roman",20,"bold"))
dest_txt.place(x=150,y=390, height=80 , width=500)

dest_txt = Text(frame, font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=25,y=480, height=150 , width=750)



root.mainloop()