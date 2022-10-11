import xml_to_xsl as xtx
from tkinter import Tk, Button, ttk

window = Tk()
window.geometry("600x500")
window.title("Qutation")

def convert():
    print('convert')
    xtx.save_excel()

button = ttk.Button(text="TEST", command=convert)

button.grid(column=4, row=1)

window.mainloop()
