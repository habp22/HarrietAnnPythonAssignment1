# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:40:54 2021

Agents Practical 

@author: Harri
"""

#Import necessary modules
import random
import matplotlib.pyplot
import agentframework
import time

#Record time at start of program
start = time.time()

#Setting the random seed for reproducibility.
random.seed(0)

#Assign an integer variable as the number of agents (10)
num_of_agents = 10
#Assign an integer variable as the number of agents (100)
num_of_iterations = 100
#create an empty list for our agents to be populated with our agents
agents_list = []

#Initialising an Agent from our agentframework module and assigning it to
# variable a
a = agentframework.Agent() 

#Testing that the module has been imported and that we can access x and y
print(a)
print(a.x)
print(a.y)

#Testing that the move function is working 
print("move")
a.move()
print(a.x)
print(a.y)

#Make a for loop where random numbers are assigned to our agents.
#For each of the 10 agents (coordinates), random numbers are assigned and these
# are put into the list.
for i in range(num_of_agents):
    #Agents_list.append is what adds the agents to the list.
    agents_list.append(agentframework.Agent())
    
#Use the move function in a for loop to shift the agents, change their assignments. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        #This will output each looped agents' x and y coordinates before move.
        print(i, "before move", agents_list[i].x, agents_list[i].y)
        agents_list[i].move()
        #This will output each looped agents' x and y coordinates after move.
        print(i, "after move", agents_list[i].x, agents_list[i].y)

#Plot the agents on a graph using matplotlib
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
    #Plot a scatter graph of the agents
    matplotlib.pyplot.scatter(agents_list[i].x, agents_list[i].y)
#This shows the plot    
matplotlib.pyplot.show()

#Print time as a calculation of time recorded at end minus time recorded at 
# beginning
end = time.time()

#print the time taken
print ("time" + str(end - start))