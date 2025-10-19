import tkinter as tk, random

def rysuj():
    c.delete("all")
    x1, y1 = random.randint(0, 300), random.randint(0, 300)
    x2, y2 = x1 + random.randint(50, 150), y1 + random.randint(50, 150)
    c.create_rectangle(x1, y1, x2, y2)

okno = tk.Tk()
c = tk.Canvas(okno, width=400, height=400)
#c = tk.Canvas(okno, width=400, height=400, bg="blue")
c.pack()
tk.Button(okno, text="Losowy prostokąt", command=rysuj).pack()
okno.mainloop()