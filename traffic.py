#!/usr/bin/python
import time
import os
import RPi.GPIO as GPIO
import Tkinter as tk
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.output(22, False)
GPIO.output(2, False)
GPIO.output(3, False)
GPIO.output(4, False)
def start1():
 try:	  	 	
  sc.update()
  br.config(bg='white')
  by.config(bg='white')
  bgr.config(bg='white')
  sc.update()
  while 1:
   GPIO.output(2, True)
   br.config(bg='yellow')
   by.config(bg='white')
   bgr.config(bg='white')
   sc.update()
   i=30
   while(i>=1):
    l2.config(text=i)
    sc.update()
    time.sleep(1)
    i=i-1
   GPIO.output(2, False)
   GPIO.output(3, True)
   by.config(bg='red')
   br.config(bg='white')
   bgr.config(bg='white')
   sc.update()
   i=60
   while(i>=1):
    if(i%2==0):
     j=i/2
     l2.config(text=str(int(j)))
     sc.update()
    if(IO.input(17)==True):
     GPIO.output(22, True) 
    time.sleep(0.5)
    i=i-1
   GPIO.output(22, False)
   GPIO.output(3, False)
   GPIO.output(4, True)
   bgr.config(bg='green')
   br.config(bg='white')
   by.config(bg='white')
   sc.update()
   i=30
   while(i>=1):
    l2.config(text=i)
    sc.update()
    time.sleep(1)
    i=i-1
   GPIO.output(4, False)
 except:
  GPIO.output(2, False)
  GPIO.output(3, False)
  GPIO.output(4, False)
  return
 return
  
def gui():
 global sc
 sc=tk.Tk()
 sc.title('Traffic Signal')
 sc.minsize(500,500)
 sc.maxsize(500,500)
 f=tk.Frame(sc)
 f.pack(side=tk.TOP,fill=tk.BOTH)
 l=tk.Label(f,text="SIGNAL",bg="brown",fg="white",font=('bold',27))
 l.pack(fill=tk.X)
 f1=tk.Frame(sc)
 f1.pack(fill=tk.BOTH)
 global b
 b=tk.Button(f1,text="START",command=start1,bg="blue",fg="white")
 b.pack(side=tk.LEFT,fill=tk.X,pady=45,padx=10)
 global l2
 l2=tk.Label(f1,text="",font=('bold',20))
 l2.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f2=tk.Frame(sc)
 f2.pack(fill=tk.BOTH)
 global br
 br=tk.Button(f2,text="",bg="yellow",fg="white")
 br.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f3=tk.Frame(sc)
 f3.pack(fill=tk.BOTH)
 global by
 by=tk.Button(f3,text="",bg="red",fg="white")
 by.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 f4=tk.Frame(sc)
 f4.pack(fill=tk.BOTH)
 global bgr
 bgr=tk.Button(f4,text="",bg="green",fg="white")
 bgr.pack(side=tk.LEFT,fill=tk.X,pady=15,padx=10)
 sc.mainloop()
 return
gui()

