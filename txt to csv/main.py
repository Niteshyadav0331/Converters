import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as tkFont

#root= ThemedTk(theme="scid themes")
#root= ThemedTk(theme="radiance")
root= ThemedTk(theme="elegance")
#root= ThemedTk(theme="clearlooks")
#root= ThemedTk(theme="breeze")
#root= ThemedTk(theme="aquativo")
root.geometry('400x300+400+230')
root.title('File Conversion Tool')
count = 0
sliderwords = ''

def labelslider():
    global count, sliderwords
    text= 'File Conversion Tool'
    if(count >= len(text)):
        count = 0
        sliderwords = ''
    sliderwords += text[count]
    count  += 1 
    label1.configure(text = sliderwords)
    label1.after(150, labelslider)


fontStyle = tkFont.Font(family="Lucida Grande", size=25)

label1 = ttk.Label(root, text = 'File Conversion Tool',  width = 32, font = ("Courier New", 20, "italic bold"))
label1.place( y = 20)

def getTxt ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_csv(import_file_path)


browsebutton = ttk.Button(root, text = "        Import Excel File         ", command = getTxt)
browsebutton.place(x = 135, y = 110)

def convertToCsv ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None)

saveasbutton = ttk.Button(root, text = "      Convert TXT to CSV      ", command = convertToCsv)
saveasbutton.place(x = 135, y = 160)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()

exitbutton = ttk.Button(root, text = "          Exit Application         ",command = exitApplication)
exitbutton.place(x = 135, y = 210)

labelslider()
root.mainloop()
