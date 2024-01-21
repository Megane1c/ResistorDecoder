# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 01:17:02 2018

@author: deoca
"""

import tkinter as tk

colors = ["black","brown","red","orange","yellow",
         "green","royal blue","purple4","gray","white"]

class SubWindow3(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        
     ##### POSITION OF GUI #####       
        width = 400
        height = 470
        x=(self.winfo_screenwidth()/2)-(width/2)
        y=(self.winfo_screenheight()/2)-(height/2)
        self.geometry("%dx%d+%d+%d" % (width,height,x,y))
        self.resizable(0,0)
        self.title("5-Band-Resistor Value Finder")
        self.iconbitmap(default='assets/img/resistor-512.ico')        
        
        self.current_colors = ["brown","green","red","royal blue","purple4"] # DEFAULT VALUE
        
        self.create_elements()
        
     ##### CLOSING COMMAND #####   
        self.protocol('WM_DELETE_WINDOW',master.close3)
        
    ##### CREATION OF RESISTOR #####     
    def create_elements(self):
        self.resistor = tk.Canvas(self, width=400, height=100)
        self.resistor.config(bg="white smoke")
        self.resistor.create_rectangle((10,10,360,90), fill="#F3C967")
        self.resistor.place(relx=1, rely=1, anchor="center")
        self.resistor.grid(row=0,column=0,columnspan=3)

        tk.Label(self, text = "First band:").grid(row=1, column=0)
        self.band1 = tk.Canvas(self, width=200, height=50)
        self.band1.create_rectangle((0,0,21,50),fill="brown", outline="brown")        
        self.band1.create_rectangle((22,0,46,50),fill="red", outline="red")
        self.band1.create_rectangle((45,0,67,50),fill="orange", outline="orange")
        self.band1.create_rectangle((68,0,90,50),fill="yellow", outline="yellow")
        self.band1.create_rectangle((91,0,113,50),fill="green", outline="green")        
        self.band1.create_rectangle((114,0,136,50),fill="royal blue", outline="royal blue")
        self.band1.create_rectangle((137,0,159,50),fill="purple4", outline="purple4")        
        self.band1.create_rectangle((160,0,182,50),fill="gray", outline="gray")
        self.band1.create_rectangle((183,0,206,50),fill="white", outline="white")
        self.band1.grid(row=1,column=1, columnspan = 2)
        self.band1.bind("<Button 1>", self.b1)

        tk.Label(self, text = "Second band:").grid(row=2, column=0)
        self.band2 = tk.Canvas(self, width=200, height=50)
        self.draw_colors(self.band2)
        self.band2.grid(row=2,column=1, columnspan = 2)
        self.band2.bind("<Button 1>", self.b2)

        tk.Label(self, text = "Third band:").grid(row=3, column=0)
        self.band3 = tk.Canvas(self, width=200, height=50)
        self.draw_colors(self.band3)
        self.band3.grid(row=3,column=1, columnspan = 2)
        self.band3.bind("<Button 1>", self.b3)

        tk.Label(self, text = "Fourth band:").grid(row=4, column=0)
        self.band4 = tk.Canvas(self, width=200, height=50)
        self.band4.create_rectangle((0,0,16,50),fill="black", outline="black")
        self.band4.create_rectangle((17,0,33,50),fill="brown", outline="brown")        
        self.band4.create_rectangle((34,0,51,50),fill="red", outline="red")
        self.band4.create_rectangle((52,0,68,50),fill="orange", outline="orange")
        self.band4.create_rectangle((69,0,85,50),fill="yellow", outline="yellow")
        self.band4.create_rectangle((86,0,103,50),fill="green", outline="green")        
        self.band4.create_rectangle((104,0,118,50),fill="royal blue", outline="royal blue")
        self.band4.create_rectangle((119,0,134,50),fill="purple4", outline="purple4")        
        self.band4.create_rectangle((135,0,150,50),fill="gray", outline="gray")
        self.band4.create_rectangle((151,0,167,50),fill="white", outline="white")
        self.band4.create_rectangle((168,0,184,50),fill="gold", outline="gold")
        self.band4.create_rectangle((185,0,211,50),fill="#C0C0C0", outline="#C0C0C0")
        self.band4.grid(row=4,column=1, columnspan = 2)
        self.band4.bind("<Button 1>", self.b4)        

        tk.Label(self, text = "Fifth band:\nTolerance").grid(row=5, column=0)
        self.band5 = tk.Canvas(self, width=200, height=50)
        self.band5.create_rectangle((0,0,30,50),fill="brown", outline="brown")
        self.band5.create_rectangle((25,0,60,50),fill="red", outline="red")
        self.band5.create_rectangle((50,0,90,50),fill="green", outline="green")
        self.band5.create_rectangle((75,0,120,50),fill="royal blue", outline="royal blue")
        self.band5.create_rectangle((100,0,150,50),fill="purple4", outline="purple4")
        self.band5.create_rectangle((125,0,180,50),fill="gray", outline="gray")
        self.band5.create_rectangle((150,0,210,50),fill="gold", outline="gold")
        self.band5.create_rectangle((175,0,240,50),fill="#C0C0C0", outline="#C0C0C0")        
        self.band5.grid(row=5,column=1, columnspan = 2)
        self.band5.bind("<Button 1>", self.b5) 

        self.result = tk.Text(self, width=36, height=1)
        self.result.grid(row=6,column=0, columnspan=3)
 
        self.min= tk.Text(self, width=36, height=1)
        self.min.grid(row=7,column=0,columnspan=3,padx=10, pady=10)
        
        self.max= tk.Text(self, width=36, height=1)
        self.max.grid(row=8,column=0,columnspan=3,padx=5, pady=5)      

              
        self.update()

    ##### DISPLAY COLOR #####
    def draw_colors(self, canv):
        for i in range(10):
            canv.create_rectangle((20*i,1,20+20*i,60),fill=colors[i], outline=colors[i])

    ##### VALUE UPDATE #####
    def update(self):
        for i in range(5):
            self.resistor.create_rectangle((60*i+40,10,60*i+70,90), fill=self.current_colors[i])
        self.result.delete(0.0, tk.END)
        self.result.insert(tk.END,"Value: "+str(self.calculate())+"Ω "+"±"+self.ch()+"%")


        self.min.delete(0.0,tk.END)
        self.min.insert(tk.END,"Minimum Value: "+str(self.Min())+"Ω ")

        
        self.max.delete(0.0,tk.END)
        self.max.insert(tk.END,"Maximum Value: "+str(self.Max())+"Ω ") 


    def change(self, band, color):
        self.current_colors[band-1] = color
        self.update()
        
        
    ##### BAND 1 #####      
    def b1(self, event):
        if event.x <=22:
            self.change(1, "brown")
        elif event.x <=45:
            self.change(1,"red")
        elif event.x <=68:
            self.change(1,"orange")
        elif event.x <=91:
            self.change(1,"yellow")
        elif event.x <=114:
            self.change(1,"green")
        elif event.x <=137:
            self.change(1,"royal blue") 
        elif event.x <=160:
            self.change(1,"purple4")
        elif event.x <=183:
            self.change(1,"gray")
        else:
            self.change(1,"white")
            
    ##### BAND 2 #####          
    def b2(self, event):
        self.change(2, self.xVal(event.x))
    
    ##### BAND 3 #####  
    def b3(self, event):
        self.change(3, self.xVal(event.x))
        
    ##### BAND 4 #####  
    def b4(self, event):
        if event.x <= 17:
            self.change(4, "black")
        elif event.x <=34:
            self.change(4, "brown")
        elif event.x <=52:
            self.change(4,"red")
        elif event.x <=69:
            self.change(4,"orange")
        elif event.x <=86:
            self.change(4,"yellow")
        elif event.x <=104:
            self.change(4,"green")
        elif event.x <=119:
            self.change(4,"royal blue") 
        elif event.x <=135:
            self.change(4,"purple4")
        elif event.x <=151:
            self.change(4,"gray")
        elif event.x <=168:
            self.change(4,"white")
        elif event.x <=185:
            self.change(4,"gold")                
        else:
            self.change(4,"#C0C0C0")
    
    ##### BAND 5 #####                      
    def b5(self, event):
        if event.x <= 25:
            self.change(5, "brown")
        elif event.x <=50:
            self.change(5, "red")
        elif event.x <=75:
            self.change(5,"green")
        elif event.x <=100:
            self.change(5,"blue")
        elif event.x <=125:
            self.change(5,"purple4")
        elif event.x <=150:
            self.change(5,"gray")
        elif event.x <=175:
            self.change(5,"gold")              
        else:
            self.change(5,"#C0C0C0")

    ##### VALUE CALCULATION #####  
    def calculate(self):
        val = str(colors.index(self.current_colors[0]))+str(colors.index(self.current_colors[1]))+str(colors.index(self.current_colors[2]))
        ans = float(val)
        band4 = str(self.current_colors[3])
        if band4 == "black":
            rslt = ans*1
            return round(rslt,5)
        elif band4 == "brown":
            rslt = ans*10
            return round(rslt,5)
        elif band4 == "red":
            rslt = ans*10**2
            return round(rslt,5)
        elif band4 == "orange":
            rslt = ans*10**3
            return round(rslt,5)
        elif band4 == "yellow":
            rslt = ans*10**4
            return round(rslt,5)
        elif band4 == "green":
            rslt = ans*10**5
            return round(rslt,5)
        elif band4 == "royal blue":
            rslt = ans*10**6
            return round(rslt,5)
        elif band4 == "purple4":
            rslt = ans*10**7
            return round(rslt,5)
        elif band4 == "gray":
            rslt = ans*10**8
            return round(rslt,5)
        elif band4 == "white":
            rslt = ans*10**9
            return round(rslt,5)
        elif band4 == "gold":
            rslt = ans*(10**(-1))
            return round(rslt,5)
        else:
            rslt = ans*(10**(-2))
            return round(rslt,5)
    
    def ch(self):
        band = str(self.current_colors[4])
        if band == 'brown':
            return '1'
        elif band == 'red':
            return '2'
        elif band == 'green':
            return '0.5'
        elif band == 'royal blue':
            return '0.25'
        elif band == 'purple4':
            return '0.1'
        elif band == 'gray':
            return '0.05'
        elif band == 'gold':
            return '5'
        else:
            return '10'    
    
    def Min(self):
        ans = int(self.calculate()) - (int(self.calculate())*(float(self.ch())/100))
        return ans
    
    def Max(self):
        ans = int(self.calculate()) + (int(self.calculate())*(float(self.ch())/100))
        return ans    
    
    def xVal(self, x):
        return colors[int(x/20)] #converts x value on the color selector to a color
    
