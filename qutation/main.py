from tkinter import Tk, Button, ttk

window = Tk()
window.geometry("600x500")
window.title("Qutation")

button = ttk.Button(text="TEST")

button.grid(column=0, row=1)

window.mainloop()

