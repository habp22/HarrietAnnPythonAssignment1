# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:39:31 2021

@author: Harri
"""

#Framework containing functions I will call upon in my main code. 

import random 

class Agent():
    
    #When Agent gets called, this function runs.
    def __init__(self, environment, rows, cols, agents, i): 
        #Pass in a copy of a reference to the environment
        self.environment = environment 
        self.x = random.randint(0, 99)
        self.y = random.randint(0, 99)
        #Agents will take some values from the environment and put them into 
        # their store.
        self.store = 0
        self.rows = rows
        self.cols = cols
        self.agents = agents
        #I refers to unique number for each of the agents
        self.i = i
    
    #Move function to change the attributes of the x and y variables.
    def move(self):  
        if random.random() < 0.5:
            #Self.rows/cols instead of a chosen number allows agents to use 
            # whole environment.
            self.y = (self.y + 1) % self.rows
        else:
            self.y = (self.y - 1) % self.rows

        if random.random() < 0.5:
            self.x = (self.x + 1) % self.cols
        else:
            self.x = (self.x - 1) % self.cols
    
    #Function to make the agents take 10 from a value in the environment if 
    # that value is greater than 10.    
    def eat(self):
        if self. environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            #The 10 that is taken from the environment gets added to the store.
            self.store += 10
        #Get the agents to eat what is left.    
        else: 
            self.store += self.environment[self.y][self.x]
            self.environment[self.y][self.x] = 0
        #Make agents sick if they have eaten more than 100 values
        if self.store >= 100: 
            print("Sick") #Prints "sick" if value in store >= 100.
            self.environment[self.y][self.x] += 100
            self.store = 0
            
    #Make the calculation for distance between as a function
    def distance_between(self, b):
        return (((self.x - b.x)**2) + ((self.y - b.y)**2))**0.5

    #Make a function to get the agents share with share with their neighbours.
    def share_with_neighbours(self, neighbourhood): 
        #check that neighbourhood variable is populated.
        print("neighbourhood", neighbourhood)  
        #Loop through the agents so that the agents communicate with eachother.
        for i in range (len(self.agents)):
            #Calculate the distance between each agent and the first agent. 
            distance = self.distance_between(self.agents[i])
            if distance < neighbourhood: 
                print("distance", distance) #test distance is working 
                #Get agents to share resources by adding together their stores.
                sum = self.store + self.agents[i].store
                #Then to calculate the average across agents 
                average = sum / 2
                #Set the two stores to be the value of the average 
                self.store = average 
                self.agents[i].store = average 
                
    def __str__(self): #Returns a string representation of the agents.
        return ("id =" + str(self.i) + ", x=" + str(self.x) + ", y=" 
                + str(self.y) + ", store=" + str(self.store))
    
    def getID(self): #function to assing ID to agents so we know they are shuffling. 
        return self.i    