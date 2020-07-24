from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as tkFont

#root= ThemedTk(theme="scid themes")
root= ThemedTk(theme="radiance")
#root= ThemedTk(theme="elegance")
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


def getPNG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = ttk.Button(text = "        Import JPG File        ", command = getPNG)
browseButton_PNG.place(x = 100, y = 120)

def convertToJPG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

saveAsButton_JPG = ttk.Button(text = '   Convert  JPG to PNG    ', command = convertToJPG)
saveAsButton_JPG.place(x = 100, y = 190)

labelslider()
root.mainloop()