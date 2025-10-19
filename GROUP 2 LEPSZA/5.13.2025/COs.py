from tkinter import *
tk = Tk()
grafika = Canvas(tk, width=400, height=200)
def f():
	print("zartowalem nie bij!!")

grafika.pack()
przycisk = Button(tk, text="tu debilu klikni mnie", command = f)
przycisk.pack()
tk.mainloop()

grafika.create_rectangle(160, 60, 240, 160)

