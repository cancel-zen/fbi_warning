# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 22:26:41 2019

@author: cs
"""

import tkinter as tk

window=tk.Tk()
window.title('FBI WARINING')
window.geometry('400x300')
window.configure(background='black')

b1=tk.Label(window,text='FBI WARNING',bg='red',fg='white')
b1.pack()

b2=tk.Label(window,text='\n\nFederal Law provides severe civil and criminal penalties for',bg='black',fg='white')
b2.pack()                         
b3=tk.Label(window,text='the unauthorized reproduction, distribution, or exhibition of',bg='black',fg='white')
b3.pack()
b4=tk.Label(window,text='copyrighted motion pictures (Title 17, United States Code,',bg='black',fg='white')
b4.pack()
b3=tk.Label(window,text='Sections 501 and 508). The Federal Bureau of Investigation',bg='black',fg='white')

b3.pack()
b4=tk.Label(window,text='investigates allegations of criminal copyright infringement',bg='black',fg='white')
b4.pack()
b5=tk.Label(window,text='(Title 17, United States Code, Section 506).',bg='black',fg='white')
b5.pack()
window.mainloop()