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
from Tkinter import Canvas,Frame,Tk

class CaCanvas(Frame):
    def __init__(self,root,ca_width,ca_height,x_max,y_max):
        Frame.__init__(self,root)
        self.x_max = x_max
        self.y_max = y_max
        self.canvas = Canvas(self,width=ca_width,height=ca_height,bg='white')
        self.canvas.pack()
        self.cell = [[None for x in range(x_max)] for y in range(y_max)]
        self.cell_count = [[0 for x in range(x_max)] for y in range(y_max)]
        self.x_scale = ca_width/x_max
        self.y_scale = ca_height/y_max
        self.create_grid()
    
    def create_grid(self):
        for x in range(self.x_max):
            for y in range(self.y_max):
                self.cell[x][y] = self.canvas.create_rectangle((x*self.x_scale,y*self.y_scale,(x+1)*self.x_scale,(y+1)*self.y_scale),outline='white',fill='white')
                
    def set_on(self,x,y):
        self.canvas.itemconfig(self.cell[x][y], fill="black")
        self.cell_count[x][y]=1

        
    def set_off(self,x,y):
        self.canvas.itemconfig(self.cell[x][y], fill="white")
        self.cell_count[x][y]=0

    def count_cells(self):
        count = 0
        for x in range(self.x_max):
            for y in range(self.y_max): 
                count+=self.cell_count[x][y]
        return count
        
    def clear_cells(self):
        for x in range(self.x_max):
            for y in range(self.y_max): 
                self.set_off(x,y)

def main():
    root = Tk()
    root.title("CaCanvas test")
    ca = CaCanvas(root,400,400,40,40)
    ca.pack()
    ca.set_on(5,5)
    root.mainloop()
    return 0

if __name__ == '__main__':
    main()

