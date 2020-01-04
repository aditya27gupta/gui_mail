import csv
import os
import smtplib
import tkinter as tk
from tkinter import filedialog
from email.message import EmailMessage

root = tk.Tk()

filename = ''
greetings = ['Hi', 'Hello', 'Dear', 'Respected', 'Sir', '']
option_greeting = tk.StringVar()
option_greeting.set(greetings[0])
# Set user input and password
email_address = tk.StringVar(value='akancha@psycus.com')
email_password = tk.StringVar(value='emidbsbxnpvyctmd')
subject = tk.StringVar(value='Test Mail')
mail_content = tk.StringVar(value='Checking GUI App functionality.')


def openfile():
    try:
        arg, filename = filedialog.askopenfilename(initialdir='/', title='Select file',
        filetypes=(('csv files', '*.csv'),('all files', '*.*'))).rsplit('/', 1)
        del arg
        label4 = tk.Label(frame, text=filename, relief = 'ridge', width = 15).grid(row=2, column=1, columnspan=2)
    except:
        pass


frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

label1 = tk.Label(frame, text='Email', width = 15)
Entry1 = tk.Entry(frame, bd =2, textvariable = email_address, width = 30)


label2 = tk.Label(frame, text='Password', width = 15)
Entry2 = tk.Entry(frame, bd =2, show='*', textvariable = email_password, width = 30)

label3 = tk.Label(frame, text='File Location', width = 15)
openfile = tk.Button(frame, text='Open File', padx=2, pady=2, fg='white', bg='#263D42', command = openfile) #, command=addApps

label5 = tk.Label(frame, text='Select Greeting', width = 15)
drop = tk.OptionMenu(frame, option_greeting, *greetings)

label6 = tk.Label(frame, text='Subject', width = 15)
Entry3 = tk.Entry(frame, bd =2, textvariable = subject, width = 30)

label7 = tk.Label(frame, text='Message', width = 15)
Entry4 = tk.Entry(frame, bd =2, textvariable = mail_content, width = 30)
label8 = tk.Label(frame, text='', width = 15)
label9 = tk.Label(frame, text='', width = 15)
label10 = tk.Label(frame, text='', width = 15)


label1.grid(row=0, column=0, columnspan=1)
Entry1.grid(row=0, column=1, columnspan=3)

label2.grid(row=1, column=0, columnspan=1)
Entry2.grid(row=1, column=1, columnspan=3)

label3.grid(row=2, column=0, columnspan=1)
openfile.grid(row=2, column=3, columnspan=1)

label5.grid(row=3, column=0, columnspan=1)
drop.grid(row=3, column=1, columnspan=3)

label6.grid(row=4, column=0, columnspan=1)
Entry3.grid(row=4, column=1, columnspan=3)

label7.grid(row=5, column=0, columnspan=1)
Entry4.grid(row=5, column=1, columnspan=3, rowspan=4)
label8.grid(row=6, column=0, columnspan=1)
label9.grid(row=7, column=0, columnspan=1)
label10.grid(row=8, column=0, columnspan=1)


root.mainloop()
