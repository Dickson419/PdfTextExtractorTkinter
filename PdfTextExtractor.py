"""
A program to extract text from a PDF file with a GUI.

Documentation = https://pypdf.readthedocs.io/en/stable/

"""

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk #allows the use of an image/logo
from tkinter.filedialog import askopenfile

"""
Window object to hold all future elements of the interface
    root = TK.Tk() = start
    root.mainloop() = end
Anything writen above or below these lines will not work!

Canvas = resize the window. PARAMETERS: root = window object, width, height
Initialise canvas with grid. PARAMETERS: columnspan number can be specified
GRID: allows for specified number of invisible columns where elements can be specified with precision.

Logo: 
Add and convert a file, ie PNG, to be used in TKinter

Instructions:
Create a label and give the user an option

StringVar = StringVar is a way to create and manage a string variable that can be linked to Tkinter widgets, 
            allowing you to display and update dynamic text in your GUI application
            
Make it pretty!
- Uneven gaps = row span
    canvas.grid(columnspan=3) = canvas.grid(columnspan=3, rowspan=3)
- Button
    More parameters can be set
    browse_button = tk.Button(root, textvariable=browse_text, font="Raleway") = browse_button = tk.Button(root, textvariable=browse_text, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
- Margin
    Gets added on at the bottom. Essentially copy/paste your canvas size settings

---------- Functionality ----------
Let's click the button and make something happen!

command --> added to a button (label, widget etc). inside the command will be the function
            we want to run. Lamda functions will also be used. lamda:function_name
            
askopenfile = part of tkinter lib. Used to open a file :P
            'opens a file dialog box that allows the user to select a file to open.'
            
USEFUL PDF methods:
        # reader = PdfReader("example.pdf")
        # number_of_pages = len(reader.pages)
        # page = reader.pages[0]
        # text = page.extract_text()
        
To make test appear in the app:
        text_box = tk.Text(root, height= 10, width=65, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)




"""
root = tk.Tk()#create window

canvas = tk.Canvas(root, width=600, height=300) #window size
canvas.grid(columnspan=3, rowspan=3) #initilise. Add rowspan to make it pretty

#Logo
logo = Image.open('logo.png') #open an image file
#convert to TK image
logo = ImageTk.PhotoImage(logo) #convert it to a TK image
logo_label = tk.Label(image=logo) #make it a label - can be placed on canvas
logo_label.image = logo
logo_label.grid(column=1, row=0) #set image in place

#Instructions
instructions = tk.Label(root, text="Select a PDF file to extract ALL of the text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1) #span over three columns. Middle alligned.

#Functionality - need to declare before button using it!
def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode="rb", title="Choose a file", filetypes=[("Pdf file", "*.pdf")]) #rb = read only
    if file: #or while True...
        read_pdf = PyPDF2.PdfReader(file) #pdf becomes variable read_pdf
        page = read_pdf.pages[0] #get the first page
        page_content = page.extract_text()


        print(page_content) #display page content in terminal - but really we want this in the app...

        text_box = tk.Text(root, height= 10, width=65, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.grid(column=1, row=3)

        #reset the browse text
        browse_text.set("Browse")



#Browse Button
browse_text = tk.StringVar() #Dynamically set a string i.e a message, time etc
browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)#fg=font colour
browse_text.set("Browse")
browse_button.grid(column=1, row=2)

#Margin
canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)








root.mainloop() #run window and all elements

