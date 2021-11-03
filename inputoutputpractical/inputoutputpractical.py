# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:40:54 2021

Input Output Practical 

@author: Harri
"""
 
import random
import matplotlib.pyplot
import agentframework
import csv 
import time 

#Record time before running program
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
#Set a number of agents.
num_of_agents = 10
#Set a number of iterations (how many times something runs)
num_of_iterations = 100
#Create a neighbourhood
neighbourhood = 20
 
#make a for loop where random numbers are assigned to our agents.
#for each of the 10 agents (coordinates), random numbers are assigned and 
# these are put into the list.
for i in range(num_of_agents):
    #agents.append is what adds the agents to the list.
    agents_list.append(agentframework.Agent(environment, rows, cols)) 
    

#Use the move function in a for loop to shift the agents, change their assignments. 
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        print(i, "before move", agents_list[i].x, agents_list[i].y)
        agents_list[i].move()
        print(i, "after move", agents_list[i].x, agents_list[i].y)
        #Make the agents eat into the environment. 
        print("store pre meal", agents_list[i].store)
        agents_list[i].eat()
        print("store post meal", agents_list[i].store)

#Plot the environment after the agents have eaten bits of it (should have a distressed/ netting effect on environment).
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.ylim(0, cols) #cols and rows instead of chosen number displays whole environment. 
matplotlib.pyplot.xlim(0, rows)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents_list[i].x, agents_list[i].y)#plots a scatter graph of the agents
matplotlib.pyplot.show()#this shows the plot
#Expected output after agents are sick: environment should be more concentrated blue. 

#Print agents after all the moving and eating 
for i in range(num_of_agents):
    print("agents", agents_list[i])

#Print time as a calculation of time recorded at end minus time recorded at 
# beginning
end = time.time()

#print the time taken
print ("time" + str(end - start))