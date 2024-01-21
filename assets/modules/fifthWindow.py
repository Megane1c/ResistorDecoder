# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:26:49 2018

@author: deoca
"""

import tkinter as tk
import re
from decimal import Decimal

class SubWindow5(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
     
    ##### POSITION OF GUI #####    
        width = 300
        height = 110
        x=(self.winfo_screenwidth()/2)-(width/2)
        y=(self.winfo_screenheight()/2)-(height/2)
        self.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.resizable(0,0)
        self.title("Value Converter")
        self.iconbitmap(default='assets/img/resistor-512.ico')

        self.calculator()
        
        
    ##### CLOSING COMMAND #####
        self.protocol('WM_DELETE_WINDOW',master.close5)        
        
    ##### CONVERTER #####   
    def calculator(self):
        global OPTIONS, variable
        OPTIONS = {"Convert Ohm(Ω) to Abohm(abΩ)":float(10**(9)),   # 10^9
                   "Convert Ohm(Ω) to Gigaohm(GΩ)":float(10**(-9)), # 10^(-9)
                   "Convert Ohm(Ω) to Kiloohm(kΩ)":float(10**(-3)), # 10^(-3)
                   "Convert Ohm(Ω) to Megaohm(MΩ)":float(10**(-6)), # 10^(-6)
                   "Convert Ohm(Ω) to Microohm(µΩ)":float(10**(6)), # 10^(6)
                   "Convert Ohm(Ω) to Milliohm(mΩ)":float(10**(3)), # 10^(3)
                   "Convert Ohm(Ω) to Nanoohm(nΩ)":float(10**(9))}  # 10^(9)

        vcmd = (self.register(self.validate),'%P' )


        variable = tk.StringVar(self)
        variable.set(next(iter(OPTIONS))) # DEFAULT VALUE
             
        r=tk.OptionMenu(self, variable, *OPTIONS)
        r.grid(row=0,column=1)
        
        
        self.l1=tk.Label(self,text='Enter Value:')
        self.l1.grid(row=1)
        
        self.entry1=tk.Entry(self,validate='key',validatecommand = vcmd)
        self.entry1.grid(row=1,column=1)
        
        self.b1=tk.Button(self, text="Convert", command=self.calc)
        self.b1.grid(row=2,column=1)
  
        self.l1=tk.Label(self,text='Result:')
        self.l1.grid(row=3)
        
        self.label=tk.IntVar()
        inv_label=tk.Label(self, text=' ', textvariable=self.label) #invisible text box
        inv_label.grid(row=3,column=1)

    def validate(self, string): # VALIDATES IF THE INPUTTED VALUE IS A NUMBER
        regex = re.compile(r"(\+|\-|)?[0-9.]*$")
        result = regex.match(string)
        return (string == ""
            or (string.count('+') <= 1
                and string.count('-') <= 1
                and string.count('.') <= 1
                and result is not None
                and result.group(0) != ""))
    
    def on_validate(self,P):
        return self.validate(P) 
     
    def calc(self):
        val=float(self.entry1.get())
        value = OPTIONS[variable.get()] # VALUE ON DICTIONARY
        res=val*value
        decimal = '%.3E' % Decimal(res) # CONVERTS TO SCIENTIFIC NOTATION
        ans=self.label.set(format(decimal))
        return ans

        
    

        
        
        


