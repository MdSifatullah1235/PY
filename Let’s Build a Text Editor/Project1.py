from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.geometry("600x600")
window.title("Text Editor")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def openfile():
    filepath = askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        text_edit.insert(END,text)
        input_file.close()
    window.title(f"Text Editor - {filepath}")

def savefile():
    filepath = asksaveasfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text = text_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")

text_edit = Text(master=window)
button_frame = Frame(master=window,relief=RAISED,bd=2)
btn_open = Button(command=openfile,text="Open",master=button_frame)
btn_save = Button(command=savefile,text="Save As",master=button_frame)

button_frame.grid(row=0,column=0,sticky="ns")
text_edit.grid(row=1,column=0,sticky="nsew")

btn_open.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_save.grid(row=1,column=0,sticky="ew",padx=5,pady=5)

window.mainloop()