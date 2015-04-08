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
from Tkinter import Tk, LEFT, Menu,Label
from tkFileDialog   import askopenfilename
from os.path import join,split
"""Split the microbial growth data from the ABM program in to separate files"""
class SplitData:
    def __init__(self):
        root = Tk()
        root.title("split data")
        root.geometry("200x200")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load data",command = self.load_data)
        self.notifcation = Label(root,text="")
        self.notifcation.grid(row=0,column=0)

        root.mainloop()
        
    def load_data(self):
        # calls the file dialog box
        name = askopenfilename() 
        (d_path,d_name)=split(name)
        fparts = d_name.split('.')
        count=0
        l_file = join(d_path,'run'+str(count)+fparts[0]+'.csv')
        out_f = open(l_file, 'w')
        with open(name) as in_f:
            for line in in_f:
                data = line.split(',')
                if len(data)>1:
                    out_f.write(line)
                else:
                    out_f.close()
                    count+=1
                    l_file = join(d_path,'run'+str(count)+fparts[0]+'.csv')
                    out_f = open(l_file, 'w')
        self.notifcation.config(text="Done")
        
def main():
    SplitData()
    return 0

if __name__ == '__main__':
    main()

