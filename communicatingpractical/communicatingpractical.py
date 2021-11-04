# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:29:59 2021

Communicating Practical 

@author: Harri
"""

import random
import matplotlib.pyplot
import agentframework
import csv 
import time 

#Record the time at the beginning of the code
start = time.time() 

#setting the random seed for reproducibility, produce same results. 
random.seed(0)

#create list for csv data, it will be a master list of all the rows.
environment = []  

#Read the data from the text file and place it into environment list
with open('iotextfile.csv', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    
#Reading in the rows to a list named rowlist, for each row we want a new list 
    for row in reader:
        #Create the empty list
        rowlist = [] 
        for value in row:
            #The append function attaches the value to the rowlist.
            rowlist.append(value)
            #Attach rowlist to environment
        environment.append(rowlist)  
#Environment list is now populated

#Check the environment, ensure it has as many values as in text file. 
rows = len(environment) 
cols = len(environment[0])
print("rows", rows)
print("cols", cols)

#Create an empty list for our agents to go into.
agents_list = []  
#Assign an integer variable as the number of agents (10).
num_of_agents = 10
#Assign an integer variable as the number of iterations (100) (how many times something runs)
num_of_iterations = 100
#Create a neighbourhood
neighbourhood = 20
 
#make a for loop where random numbers are assigned to our agents.
#for each of the 10 agents, random numbers are assigned and 
# these are put into the list.
for i in range(num_of_agents):
    #agents.append is what adds the agents to the list.
    agents_list.append(agentframework.Agent(environment, rows, cols, agents_list, i)) 
    
#Use the move function in a for loop to shift the agents, change their assignments. 
for j in range(num_of_iterations):
    #At end of each iteration, shuffle the agents
    #Test so that we can see what's happening in each iteration. 
    print("Iteration", j)  
    #Printing iteration helps to see that the agents are shuffling. 
    random.shuffle(agents_list)
    for i in range(num_of_agents):
        print(i, "before move", agents_list[i].x, agents_list[i].y) #Test
        agents_list[i].move()
        #Test that the agents have moved.
        print(i, "after move", agents_list[i].x, agents_list[i].y)  
        #Now we want to make the agents eat
        print("store pre meal", agents_list[i].store) #Test
        agents_list[i].eat()
        #Test that the agents have stored what they have eaten
        print("store post meal", agents_list[i].store)  
        #Now we want the agents to share with what's around them
        agents_list[i].share_with_neighbours(neighbourhood)
        
#Plot the environment after the agents have eaten bits of it 
# should have a distressed/ netting effect on environment if agents haven't
# been sick. 
matplotlib.pyplot.imshow(environment)
#cols and rows instead of chosen number displays whole environment.
matplotlib.pyplot.ylim(0, cols) 
matplotlib.pyplot.xlim(0, rows)
for i in range(num_of_agents):
    #Plot a scatter graph of the agents
    matplotlib.pyplot.scatter(agents_list[i].x, agents_list[i].y)
#Show the plot
matplotlib.pyplot.show()
#Environment should be more concentrated blue if the agents have been sick. 

#Print agents after all the moving, eating, sharing and shuffling
print("Final agents")

##Print time as a calculation of time recorded at end minus time recorded at 
# beginning
end = time.time()

#print the time taken
print ("time" + str(end - start))
