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

class CaGrid:
    def __init__(self,x_max,y_max):
        self.x_max = x_max
        self.y_max = y_max
        self.cell_count = [[0 for x in range(x_max)] for y in range(y_max)]
    
    def set_on(self,x,y):
        self.cell_count[x][y]=1

        
    def set_off(self,x,y):
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
    ca = CaCanvas(40,40)
    return 0

if __name__ == '__main__':
    main()

