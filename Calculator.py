import tkinter as tk
from tkinter import font as tkFont
import random


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.numPressed = []
        self.geometry("365x355+100+100")
        self.buttonFont = tkFont.Font(family="Arial", size=40)
        self.label = tk.Label(self, text="", bg = "White", height = 3)
        self.label.grid(row=0,column=0, columnspan = 4, sticky = "WE")
        self.button = tk.Button(self, text = "1", font=self.buttonFont, width = 2, bg = "Yellow", command = lambda: self.digitPressed(1))
        self.button2 = tk.Button(self, text = "2", font=self.buttonFont, width= 2, bg = "Yellow", command = lambda: self.digitPressed(2))
        self.button3 = tk.Button(self, text = "3", font=self.buttonFont, width = 2, bg = "Yellow", command = lambda: self.digitPressed(3))
        self.button4 = tk.Button(self, text = "+", font=self.buttonFont, width = 2, bg = "Yellow")
        self.button5 = tk.Button(self, text = "4", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(4))
        self.button6 = tk.Button(self, text = "5", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(5))
        self.button7 = tk.Button(self, text = "6", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(6))
        self.button8 = tk.Button(self, text = "-", font=self.buttonFont, bg = "Yellow")
        self.button9 = tk.Button(self, text = "7", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(7))
        self.button10 = tk.Button(self, text = "8", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(8))
        self.button11 = tk.Button(self, text = "9", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(9))
        self.button12 = tk.Button(self, text = "x", font=self.buttonFont, bg = "Yellow")
        self.button13 = tk.Button(self, text = "del", font=self.buttonFont, bg = "Yellow")
        self.button14 = tk.Button(self, text = "0", font=self.buttonFont, bg = "Yellow", command = lambda: self.digitPressed(0))
        self.button15 = tk.Button(self, text = "=", font=self.buttonFont, bg = "Yellow")
        self.button16 = tk.Button(self, text = "/", font=self.buttonFont, bg = "Yellow")

        self.buttons = [self.button, self.button2,self.button3,self.button4,self.button5,self.button6,self.button7,self.button8,self.button9,self.button10,self.button11,self.button12,self.button13,self.button14,self.button15,self.button16]
        for i in range(16):

            self.buttons[i].grid(row= i//4 +1 , column = i%4, sticky = "WE")
        tk.mainloop()

        
    def digitPressed(self,num): 

        self.numPressed.append(num)
        numtext = "".join([str(d) for d in self.numPressed])
        self.label.config(text = numtext)
   
   

      

app = App()
