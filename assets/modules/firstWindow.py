# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:15:48 2018

@author: deoca
"""

import tkinter as tk
import PIL as p
from PIL import ImageTk

class SubWindow1(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
    
    ##### POSITION OF GUI #####    
        width = 571
        height = 500
        x=(self.winfo_screenwidth()/2)-(width/2)
        y=(self.winfo_screenheight()/2)-(height/2)
        self.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.resizable(0,0)
        self.title("Resistor")
        self.iconbitmap(default='assets/img/resistor-512.ico')

        self.lesson()
     
    ##### CLOSING COMMAND #####     
        self.protocol('WM_DELETE_WINDOW',master.close1)  
        
    ##### CREATION OF INTRODUCTION #####    
    def lesson(self):
        canvas = tk.Canvas(self, bg='white',height=500, width=571)
        canvas.pack(expand = tk.YES, fill=tk.BOTH)
        
        img= p.Image.open('assets/img/resistor.jpg')
        canvas.image = ImageTk.PhotoImage(img)
        canvas.create_image(0,0,image = canvas.image,anchor = tk.NW)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        