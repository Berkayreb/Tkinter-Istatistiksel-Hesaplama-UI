# -*- coding: utf-8 -*-
"""
@author: Berkay
"""


from tkinter import *
import statistics as st
import pandas as pd
import xlrd
from scipy import stats as s
from tkinter import filedialog


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


master = Tk()
master.title("Basit İstatistik Değerleri")

labelfile = Label(master,text="Analiz Etmek İstediğiniz Dosyayı Seçin:" ).grid(row=0,column=0,sticky=W,pady=2)

    

button = Button(master, text="Dosyayı Aç", command=load_file , width=10)
button.grid(row=0, column=1, sticky=W)

labeliki = Label(master,text="Dosya konumu : " ).grid(row=1,column=0,sticky=W,pady=2)

text = StringVar()
labeluc = Label(master,textvariable=text).grid(row=1,column=1,sticky=W,pady=2)

meanlbl = Label(master,text="Ortalama: ").grid(row=2,column=0,sticky=W,pady=2)
mean = StringVar()
labelmean = Label(master,textvariable=mean).grid(row=2,column=1,sticky=W,pady=2)

modelbl = Label(master,text="Mode").grid(row=3,column=0,sticky=W,pady=2)
mode = StringVar()
labelmode = Label(master,textvariable=mode).grid(row=3,column=1,sticky=W,pady=2)

medianlbl = Label(master,text="Medyan: ").grid(row=4,column=0,sticky=W,pady=2)
median = StringVar()
labelmedian = Label(master,textvariable=median).grid(row=4,column=1,sticky=W,pady=2)

stlbl = Label(master,text="Standart Sapma: ").grid(row=5,column=0,sticky=W,pady=2)
standart = StringVar()
labelstd = Label(master,textvariable=standart).grid(row=5,column=1,sticky=W,pady=2)

carpikliklbl = Label(master,text="Çarpıklık(Skewness): ").grid(row=6,column=0,sticky=W,pady=2)
carpiklik = StringVar()
labelcarpiklik = Label(master,textvariable=carpiklik).grid(row=6,column=1,sticky=W,pady=2)

kurtosislbl = Label(master,text="Basıklık(Kurtosis): ").grid(row=7,column=0,sticky=W,pady=2)
kurtosis = StringVar()
labelkurtosis = Label(master,textvariable=kurtosis).grid(row=7,column=1,sticky=W,pady=2)



def load_file():
    fname = filedialog.askopenfilename()
    text.set(fname)
    #df = pd.read_excel(fname)   
    
    wb = xlrd.open_workbook(fname)
    ws = wb.sheet_by_index(0)
    mylist = ws.col_values(0)
    
    
    #print(df)
    
    mean.set(st.mean(mylist))
    
    try:
         mode.set(int(s.mode(mylist)[0]))
    except:       
         mode.set("Verisetinde mode değeri yoktur")   
         
    median.set(st.median(mylist))
    
    standart.set(st.stdev(mylist))
    
    carpiklik.set(s.skew(mylist))
    
    kurtosis.set(s.kurtosis(mylist))
    
    f = Figure(figsize=(3,3), dpi=100)
    canvas = FigureCanvasTkAgg(f, master=master)
    canvas.get_tk_widget().grid(row=0, column=3, rowspan=6)

    p = f.gca()
    p.set_title('Box Plot')
    p.boxplot(mylist)
    
    canvas.show()



mainloop()




