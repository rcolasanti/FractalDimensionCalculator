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
from Tkinter import Tk,LEFT, Menu,IntVar
from cagrid import *
from tkFileDialog   import askopenfilename
from os.path import join,split
from math import log
from pylab import *

class Fractal:
    def __init__(self):
        root = Tk()
        root.title("Fractal Dimension")
        root.geometry("200x200")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load data",command = self.load_data)
        
        self.ca=[]
        max_size = 128
        while max_size>0:
            self.ca.append(CaGrid(max_size,max_size))
            max_size = max_size/2

        root.mainloop()
        
    def load_data(self):
        # calls the file dialog box
        # calls the file dialog box
        name = askopenfilename() 
        resource = 0
        with open(name) as in_file:
            for line in in_file:
                newline = line.rstrip('\r\n')
                data = newline.split(',')
                if len(data)>1:
                    resource = int(data[3])
                    self.add_data(data[1],data[2])
                else:
                    print resource,",",self.ca[0].count_cells(),
                    self.calculate_slope()
                    for ca in self.ca:
                        ca.clear_cells()
                    
        
        
    def add_data(self,x,y):
        size = 1
        count = 0
        #print x,y
        while size<128:
            self.ca[count].set_on((int(x)+64)/size,(int(y)+64)/size)
            size=size*2
            count+=1
                
    def calculate_slope(self):
        size = 128
        data_x=[]
        data_y=[]
        i=0
        while size > 1:
            data_x.append(log(size))
            data_y.append(log(self.ca[i].count_cells()))
            size/=2
            i+=1
            #DEBUG print data_x,data_y
        fit = polyfit(data_x,data_y,1)
        print ",",fit[0]
                        
    def view_ca(self,scale):
        self.ca[self.current_view].grid_forget()
        self.ca[scale].grid(column=0, row=0)
        self.current_view=scale


        
def main():
    Fractal()
    return 0

if __name__ == '__main__':
    main()

