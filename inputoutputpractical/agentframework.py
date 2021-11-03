# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:39:31 2021

@author: Harri
"""

#Framework containing functions I will call upon in my main code. 

import random 

class Agent():
    
    def __init__(self, environment, rows, cols): 
        self.environment = environment #pass in a copy of a reference to the environment
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        self.store = 0 #agents will take some values from the environment and put them into their store. 
        self.rows = rows
        self.cols = cols
    
    def move(self): #moving changes the attributes of the x and y variables. 
        if random.random() < 0.5:
            self.y = (self.y + 1) % self.rows #self.rows/cols instead of a chosen number allows agents to use whole environment. 
        else:
            self.y = (self.y - 1) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols
        
    def eat(self): #function to make the agents take 10 from a value in the environment if that value is greater than 10. 
        #To test the following code, set the environment value (test has been commented out)
        #self.environment[self.y][self.x] = 6
        if self. environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10 #the 10 that is taken from the environment gets added to the store. 
        else: #get the agents to eat what's left. 
            #print("Adding value < 10") #for the test
            #print("Before self.environment[self.y][self.x]",  self.environment[self.y][self.x]) #also for the test
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
            #print("After self.environment[self.y][self.x]",  self.environment[self.y][self.x]) #also for the test
        if self.store >= 100: #we want the agents to be sick if they have eaten more than 100 values. 
            #print("Sick") #prints "sick" if value in store greater than or equal to 100.
            self.environment[self.y][self.x] += 100
            self.store = 0
        
    def __str__(self): #returns a string representation of agents
        return ("x=" + str(self.x) + ", y=" + str(self.y)
                + ", store=" + str(self.store))
        