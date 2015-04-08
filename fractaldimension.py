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
from Tkinter import LEFT, Menu,IntVar
from tkplotlib import *
from cacanvas import *
from tkFileDialog   import askopenfilename
from os.path import join,split
from math import log
from numpy import polyfit

class Fractal:
    def __init__(self):
        root = Tk()
        root.title("Fractal Dimension")
        root.geometry("1000x500+500+500")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        view_menu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        menu.add_cascade(label="View", menu=view_menu)
        filemenu.add_command(label="Load data",command = self.load_data)
        view_menu.add_command(label="Canvas 128",command = lambda:self.view_ca(0))
        view_menu.add_command(label="Canvas 64",command = lambda:self.view_ca(1))
        view_menu.add_command(label="Canvas 32",command = lambda:self.view_ca(2))
        view_menu.add_command(label="Canvas 16",command = lambda:self.view_ca(3))
        view_menu.add_command(label="Canvas 8",command = lambda:self.view_ca(4))
        view_menu.add_command(label="Canvas 4",command = lambda:self.view_ca(5))
        view_menu.add_command(label="Canvas 2",command = lambda:self.view_ca(6))
        view_menu.add_command(label="Canvas 1",command = lambda:self.view_ca(7))
            
        self.ca=[]
        max_size = 128
        while max_size>0:
            self.ca.append(CaCanvas(root,500,500,max_size,max_size))
            max_size = max_size/2
            
        self.current_view = 0
        
        self.ca[self.current_view].grid(row=0,column=0)
        self.tkplot = TkinterGraph(root)
        self.tkplot.grid(row=0,column=1)
        root.mainloop()
        
    def load_data(self):
        # calls the file dialog box
        name = askopenfilename() 
        out_f = open(name, 'r')
        max_time = 0
        data_x=[]
        data_y=[]
        with open(name) as in_f:
            for line in in_f:
                newline = line.rstrip('\r\n')
                data = newline.split(',')
                if max_time< data[3]:
                    max_time = data[3] 
        
        for ca in self.ca:
            ca.clear_cells()
        
                    
        with open(name) as in_f:
            for line in in_f:
                newline = line.rstrip('\r\n')
                data = newline.split(',')
                if data[3] == max_time:
                    size = 1
                    count = 0
                    while size<128:
                        self.ca[count].set_on((int(data[1])+64)/size,(int(data[2])+64)/size)
                        size=size*2
                        count+=1
        size = 128
        data_x=[]
        data_y=[]
        for i in range(count):
            data_x.append(log(size))
            data_y.append(log(self.ca[i].count_cells()))
            size/=2
        # DEBUG print data_x,data_y
        self.tkplot.change_data(data_x,data_y)
                        
    def view_ca(self,scale):
        self.ca[self.current_view].grid_forget()
        self.ca[scale].grid(column=0, row=0)
        self.current_view=scale


        
def main():
    Fractal()
    return 0

if __name__ == '__main__':
    main()

