# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:39:31 2021

Agent Framework 

@author: Harri
"""

#Framework containing functions I will call upon in my main code. 

import random 

class Agent():
    
    def __init__(self):
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
    
    def move(self): #moving changes the attributes of the x and y variables. 
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
       
        