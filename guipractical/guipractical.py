# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:10:39 2021

GUI Practical

@author: Harri
"""

import agentframework
#Import beautiful soup which will be used to parse data from a website. 
import bs4 
import csv
import matplotlib
matplotlib.use('TkAgg') #backend for using matplotlib with tkinter
import matplotlib.animation
import matplotlib.pyplot
import time
#Import tkinter which is the framework for creating GUIs in Python. 
import tkinter
import random
import requests

#Record time before the code starts running. 
start = time.time()

#Set the random seed for repeatability
random.seed(0)

# This section of code takes the data from the leeds website and extracts out
# the y and x values from the resource
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
#Use beautiful soup to parse data from the above website
soup = bs4.BeautifulSoup(content, 'html.parser')
#Below td refers to the data from a table
td_ys = soup.find_all(attrs={"class" : "y"}) #find all y values
td_xs = soup.find_all(attrs={"class" : "x"}) #find all x values

#Print the y and x values. 
print(td_ys)
print(td_xs)

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
#Assign an integer variable as the number of iterations (100)(how many times something runs)
num_of_iterations = 100
#Create a neighbourhood
neighbourhood = 20

#Add a function that, within the GUI, will run our model
#This will be in the drop-down menu in the GUI
def run(): 
    matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
    #use canvas. to draw a window with the above animation in it.
    canvas.draw()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# This code sets up our drop down menu in the window
root = tkinter.Tk()
root.wm_title("Menu")
menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
#Label the drop down menu
menu.add_cascade(label="Menu", menu=model_menu)
#Label the option to run model in the drop down menu. 
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Quit model", command=root.destroy)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#ax.set_autoscale_on(False)
carry_on = True

# assign the y and x values to an Agent and populating the agents list with them
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents_list.append(agentframework.Agent(environment, rows, cols, agents_list, i))

def update(frame_number): #in this function we work out the stopping condition. 

    fig.clear()
    #Global allows us to use carry_on outside of this function
    global carry_on
    #Map a plot of the environment 
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, cols)
    matplotlib.pyplot.ylim(0, rows)

    print("Iteration", frame_number)
    for i in range(num_of_agents):
        #print(agents_list[i])
        #print(i, "before move", agents_list[i].x, agents_list[i].y)
        agents_list[i].move()
        #print(i, "after move", agents_list[i].x, agents_list[i].y)
   # for i in range(num_of_agents):    
       #print("store before eat", agents_list[i].store)
        agents_list[i].eat()
        #print("store after eat", agents_list[i].store)
    #for i in range(num_of_agents):    
        agents_list[i].share_with_neighbours(neighbourhood) 
        
    for i in range(num_of_agents):
        #Add agents to the plot
        matplotlib.pyplot.scatter(agents_list[i].x,agents_list[i].y)
        

#Frames = 10 stops the code running after 10 iterations. 
animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)


#Give each agent a unique name
def getID():
    return agents_list.i

# Print what is left after all iterations
print("Final agents")  

#Record time when the code finishes running 
end = time.time()

#Print time as a calculation of time recorded at end minus time recorded at 
# beginning
print ("time" + str(end - start))

#Stop the code running 
tkinter.mainloop()

