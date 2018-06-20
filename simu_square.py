#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 10:24:22 2018

@author: hugo
"""

# =============================================================================
# Packages
# =============================================================================

from tkinter import *
import numpy as np


class erosion_simu(Tk):
    
    def __init__(self,parent,size):
        Tk.__init__(self,parent)     
        self.parent=parent
        self.size=size # size of the array
        self.canvas=Canvas(self, width=str(self.size)+'m', height=str(self.size)+'m',bg='white')
        self.canvas.pack()
        self.pos_obj=[(int(self.size/4),int(self.size/4)),(int(self.size/4+self.size/2),int(self.size/4+10))]
        self.time=0
        self.id_rect=[]
        self.matrix=np.zeros((self.size,self.size),dtype=np.int8)
        self.InitiateMatrix()
        self.CreateObject()
        self.DisplayObject()
        for i in range(10):
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
        self.canvas.delete(self.id_rect)
        rm_x=[]
        rm_y=[]
        for x in range(1,self.size-1):
            for y in range(1,self.size-1):
                if self.matrix[x-1,y]==0 or self.matrix[x+1,y]==0 or self.matrix[x,y+1]==0 or self.matrix[x,y-1]==0:
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
                    self.id_rect=self.id_rect+[self.canvas.create_rectangle(str(x)+'m',str(y)+'m',str(x+1)+'m',str(y+1)+'m',fill='blue',width=0)]#,disabledoutline=True)]
        self.DisplayObject()

                    
        
if __name__ == "__main__":
    size=100
    displayer=erosion_simu(None,size)
    displayer.mainloop()
        
        
        
        