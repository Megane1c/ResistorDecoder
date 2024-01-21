# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:06:16 2018

@author: deoca
"""

from PIL import ImageTk
from tkinter import messagebox
import tkinter as tk
import os
import sys

cwd = os.getcwd()
module_cd = os.path.join(cwd, 'assets/modules')
img_d = 'assets/img'
sys.path.insert(1, module_cd)

import firstWindow as fr
import secondWindow as frb
import thirdWindow as fvb
import fourthWindow as sxb
import fifthWindow as fw
import ctypes

myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class MainWindow(tk.Tk):
    f1 = "Arial 13 bold"
    def __init__(self):
        super().__init__()
        self.title('Main Menu')
        
        ##### MENUBAR #####
        self.menubar = tk.Menu(self, tearoff=0)
        self.config(menu=self.menubar)
        self.menubar.add_command(label="About", command = self.abt)

        self.btn()
    
    def abt(self):
        messagebox.showinfo("About the program","Version: 1.0\nUpdate: 10-14-2018\nCreator: Deocadiz, Angelito B.")
    
    ##### BUTTON COMMANDS #####
    def btn(self):
        tk.Button(self, text='About Resistors', command=self.new_window1, fg='SlateBlue1',bg='ghost white', font=self.f1).pack(fill=tk.X) 
                      

        self.b2 = tk.Button()
        image1 = ImageTk.PhotoImage(file=os.path.join(cwd, img_d, 'fourband.png'))
        self.b2.config(image=image1,command = self.new_window2)
        self.b2.image = image1
        self.b2.pack()
        
        self.b3 = tk.Button()
        image2 = ImageTk.PhotoImage(file=os.path.join(cwd, img_d, "fiveband.png"))
        self.b3.config(image=image2,command = self.new_window3)
        self.b3.image = image2
        self.b3.pack()        
        
        self.b4 = tk.Button()
        image3 = ImageTk.PhotoImage(file=os.path.join(cwd, img_d, "sixband.png"))
        self.b4.config(image=image3,command = self.new_window4)
        self.b4.image = image3
        self.b4.pack()          
        
        tk.Button(self, text = "Conversion", command=self.new_window5, fg='SlateBlue1',bg='ghost white', font=self.f1).pack(fill=tk.X)
        
        self._first_window = None
        self._second_window = None
        self._third_window = None
        self._fourth_window = None
        self._fifth_window = None
        
    ##### OPEN COMMANDS #####
    def new_window1(self):
        window.withdraw()
        self._first_window=fr.SubWindow1(self)        
        if self._first_window is not None:
            return

    def new_window2(self):
        window.withdraw()
        self._second_window=frb.SubWindow2(self)    
        if self._second_window is not None:
            return

    def new_window3(self):
        window.withdraw()
        self._third_window=fvb.SubWindow3(self)
        if self._third_window is not None:
            return
                
    def new_window4(self):
        window.withdraw()
        self._fourth_window=sxb.SubWindow4(self) 
        if self._fourth_window is not None:
            return
           
    def new_window5(self):
        window.withdraw()
        self._fifth_window=fw.SubWindow5(self)
        if self._fifth_window is not None:
            return
        
    ###### CLOSE COMMANDS #####
    def close1(self):
        if self._first_window is not None:
            self._first_window.destroy()
            self._first_window = None
            window.deiconify()

    def close2(self):
        if self._second_window is not None:
            self._second_window.destroy()
            self._second_window = None
            window.deiconify()

    def close3(self):
        if self._third_window is not None:
            self._third_window.destroy()
            self._third_window = None  
            window.deiconify()

    def close4(self):
        if self._fourth_window is not None:
            self._fourth_window.destroy()
            self._fourth_window = None 
            window.deiconify()

    def close5(self):
        if self._fifth_window is not None:
            self._fifth_window.destroy()
            self._fifth_window = None
            window.deiconify()

if __name__ == '__main__':
    window = MainWindow()
    width = 400
    height = 668
    x=(window.winfo_screenwidth()/2)-(width/2)
    y=(window.winfo_screenheight()/2)-(height/2)
    window.geometry("%dx%d+%d+%d" % (width,height,x,y))
    window.resizable(0,0)        
    window.iconbitmap(os.path.join(cwd, img_d, "resistor-512.ico"))    
    window.mainloop()      

