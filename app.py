import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import pyttsx3
import pymysql

class App:
       

    def __init__(self, root):

        global GButton_345
        global GButton_970
        global GListBox_744
        global GLineEdit_642
        global GLabel_940

        #setting title
        root.title("TTS")

        #setting window size
        width=800
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        obj=LabelFrame(root,text="Text_to_speech",font=30)       
        obj["text"]="Text_to_speech"
        ft=tkFont.Font(family='Times',size=15)
        obj["font"]=ft
        obj.pack(fill="both",expand="yes",padx=20,pady=20)
        
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Button for Convet to audio 
        GButton_345=tk.Button(root)
        GButton_345["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        GButton_345["font"] = ft
        GButton_345["fg"] = "#000000"
        GButton_345["justify"] = "center"
        GButton_345["text"] = "CONVERT TO AUDIO"
        GButton_345["relief"] = "groove"
        GButton_345.place(x=120,y=200,width=233,height=50)
        GButton_345["command"] = self.GButton_345_command

        # Button for Exit
        GButton_970=tk.Button(root)
        GButton_970["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_970["font"] = ft
        GButton_970["fg"] = "#000000"
        GButton_970["justify"] = "center"
        GButton_970["text"] = "EXIT"
        GButton_970["relief"] = "groove"
        GButton_970.pack(side=BOTTOM,pady=20)
        GButton_970["command"] = self.GButton_970_command

        # List box for showing list of audio files.
        GListBox_744=tk.Listbox(obj)
        GListBox_744["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_744["font"] = ft
        GListBox_744["fg"] = "#333333"
        GListBox_744["relief"] = "groove"
        GListBox_744.pack(side=RIGHT,ipadx=80,ipady=100,padx=40,pady=20)
        GListBox_744["command"] = GListBox_744.insert(tk.END, self.fetch_filenames())

        # Text Box 
        GLineEdit_642=tk.Entry(root)
        GLineEdit_642["borderwidth"] = "1px"
        ft = tkFont.Font(family='Halvetica',size=18)
        GLineEdit_642["font"] = 'Halvetica'
        GLineEdit_642["fg"] = "#333333"
        GLineEdit_642["justify"] = "center"
        GLineEdit_642["text"] = "ENTER YOUR TEXT"
        GLineEdit_642.place(x=50,y=90,width=348,height=61)
        GLineEdit_642["textvariable"] = textv

        # Label 
        GLabel_940=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_940["font"] = ft
        GLabel_940["fg"] = "#333333"
        GLabel_940["justify"] = "center"
        GLabel_940["text"] = "Enter Your Text Below"
        GLabel_940.place(x=150,y=50,width=173,height=30)

    # To fetch data from Database 
    def fetch_filenames(self):
        GListBox_744.delete(0,END)
        conn = pymysql.connect(host='localhost', user='root', password='cdac123', db='audiodb')
        cur = conn.cursor()
        cur.execute("select * from audiofiles")
        filenames = cur.fetchall()
        cur.close()
        conn.close()

        for filename in filenames:
            GListBox_744.insert(END, filename[0])

    # Button Fuction for exceution 
    def GButton_345_command(self):
        engine.setProperty('rate',100) 
        engine.say(textv.get())
        engine.save_to_file(textv.get(),(f"{textv.get()}.mp3").replace(" ","_")) 
        engine.runAndWait() 
        engine.stop() 
        
        #To delete text after execution or pressing button.
        GLineEdit_642.delete(0,END)

        # Connection with database to insert data into database and execute query.
        conn = pymysql.connect(host='localhost', user='root', password='cdac123', db='audiodb')
        cur = conn.cursor()
        cur.execute("insert into audiofiles (AF_NAme)values('%s')" % (f"{textv.get()}.mp3").replace(" ","_"))
        conn.commit()
        cur.close()
        conn.close()

        self.fetch_filenames()

    # Exit button function 
    def GButton_970_command(self):
        exit()

  

if __name__== "__main__":
    root = tk.Tk()
    engine = pyttsx3.init()
    textv = tk.StringVar()
    app = App(root)
    root.mainloop()