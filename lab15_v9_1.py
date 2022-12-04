from math import *
from tkinter import *
root = Tk()
canv = Canvas(root, width = 300, height = 220)
canv.pack()
x0 = 40
y0 = 240
xmentry = Entry(foreground="black", background="grey", width=50, height=20)
ym = 20
Sm = 1.2
tm = 5
#def coord(x0, y0, xm, ym, fil_color):
#    canv.create_line(x0-10, y0, xm+10, y0, fill = fil_color, arrow = LAST)
#    canv.create_line(x0, ym-10, x0, 2*y0-ym+10, fill = fil_color, arrow = BOTH)
#def graph(f, fm, tm, x0, y0, xm, ym, fil_color):
#    xb = x0
#    t = 0
#    yb = y0+(ym-y0)*f(t)/fm
#    canv.create_line(xb, yb, xb, yb, fill = fil_color)
#    tm = float(tm)
#    for x in range (x0+2, xm, 2):
#        t = tm*(x-x0)/(xm-x0)
#        y = y0+(ym-y0)*f(t)/fm
#        canv.create_line(xb, yb, x, y, fill = fil_color)
#        xb = x
#        yb = y

        
#coord(x0, y0, xm, ym, 'blue')
#graph(sin, 1.2, 2*pi, x0, y0, xm, ym, 'red')
root.mainloop()