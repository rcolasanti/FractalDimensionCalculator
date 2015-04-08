#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <code.colasanti@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from Tkinter import Canvas,Label,Frame,Tk,BOTH,LEFT,TOP,BOTTOM
from tkFileDialog   import askopenfilename
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from matplotlib import * 
from pylab import *

class TkinterGraph(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.figure = Figure(figsize=(10,10), dpi=50)
        self.title= self.figure.suptitle('', fontsize=20)
        self.graph_a = self.figure.add_subplot(111)
        self.graph_a.set_ylabel('ln(numberof filled boxes)')
        self.graph_a.set_xlabel('ln(Box size)')
        
       
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.show()
        self.canvas._tkcanvas.pack(side=TOP)#,fill=BOTH, expand=1)
        

    def change_data(self,data_x,data_y):
        self.graph_a.clear()
        #self.graph_a.scatter(data_x,data_y)
        fit = polyfit(data_x,data_y,1)
        #DEBUG print fit
        self.title.set_text('Fractal dimension: %.3f' % fit[0])
        fit_fn = poly1d(fit)
        self.graph_a.plot(data_x,data_y, 'yo', data_x, fit_fn(data_x), '--k')
        self.canvas.draw()

        


def main():
    root = Tk()
    root.title("CaCanvas test")
    root.geometry("850x500+500+500")
    tkplot = TkinterGraph(root)
    tkplot.pack(side=LEFT)
    root.mainloop()
    return 0

if __name__ == '__main__':
    main()

