#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:11:57 2018

@author: hugo
"""

# =============================================================================
# Packages
# =============================================================================

from tkinter import *
import numpy as np
from matplotlib.pyplot import imshow

class erosion_simu(Tk):
    
    def __init__(self,parent,size):
        Tk.__init__(self,parent)     
        self.parent=parent
        self.size=size # size of the array
        self.canvas=Canvas(self, width=str(self.size)+'m', height=str(self.size)+'m',bg='white')
        self.canvas.pack()
        self.pos_obj=[(int(self.size/4),int(self.size/4)),(int(self.size/4+self.size/2),int(self.size/4+10))]
        self.time=0
        self.id_hex=[]
        self.matrix=np.zeros((self.size,self.size),dtype=np.int8)
        self.InitiateMatrix()
        self.CreateObject()
        self.DisplayObject()
        for i in range(15):
            self.Erode()
        self.DisplayMatrix()
    
        
    def CreateObject(self):
        """pos_obj=[(x0,y0),(x1,y1)], (x0,y0)= top left, (x1,y1)= bottom right"""
        [(x0,y0),(x1,y1)]=self.pos_obj
        self.matrix[x0:x1,y0:y1]=1
        
    def InitiateMatrix(self):
        [(x0,y0),(x1,y1)]=self.pos_obj
        self.matrix[0:self.size,y1:self.size]=1
        
    def DisplayObject(self):
        [(x0,y0),(x1,y1)]=self.pos_obj
        self.canvas.create_rectangle(str(x0)+'m',str(y0)+'m',str(x1)+'m',str(y1)+'m',fill='black',width=0)

    
    def Erode(self):
        self.canvas.delete(self.id_hex)
        rm_x=[]
        rm_y=[]
        
        for y in range(2,self.size-2):
            for x in range(1,self.size-1):
                    if self.matrix[x,y-2]==0 or self.matrix[x+1,y-1]==0 or self.matrix[x+1,y+1]==0 or self.matrix[x,y+2]==0 or self.matrix[x-1,y+1]==0 or self.matrix[x-1,y-1]==0:
                        rm_x.append(x)
                        rm_y.append(y)
                    
                            
        rm_x=np.array(rm_x)
        rm_y=np.array(rm_y)
        self.matrix[rm_x,rm_y]=0
        self.CreateObject()
        self.time+=1
        
    def DisplayMatrix(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x,y]:
                    R=1/np.cos(np.pi/60)
                    if y%2==0:                        
                        self.id_hex=self.id_hex+[self.canvas.create_polygon(str(x-R)+'m',str(y)+'m',str(x-R/2)+'m',str(y-1)+'m',str(x+R/2)+'m',str(y-1)+'m',str(x+R)+'m',str(y)+'m',str(x+R/2)+'m',str(y+1)+'m',str(x-R/2)+'m',str(y+1)+'m',fill='blue',width=0)]
                    else:
                        xp=x+np.sqrt(3)
                        
                        self.id_hex=self.id_hex+[self.canvas.create_polygon(str(x-R)+'m',str(y)+'m',str(x-R/2)+'m',str(y-1)+'m',str(x+R/2)+'m',str(y-1)+'m',str(x+R)+'m',str(y)+'m',str(x+R/2)+'m',str(y+1)+'m',str(x-R/2)+'m',str(y+1)+'m',fill='blue',width=0)]#,disabledoutline=True)]
        self.DisplayObject()

                    
        
if __name__ == "__main__":
    size=100
    displayer=erosion_simu(None,size)
    displayer.mainloop()
    matrix=displayer.matrix
    imshow(matrix)
        
        