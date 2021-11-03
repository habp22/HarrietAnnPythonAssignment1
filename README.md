# Repository: Python Assignment 1 (30%)
## Introduction
This project creates a list of agents (which are sheep) and plots them into an environment. Additionally, the sheep move, eat away at the environment and shuffle within iterations. The environment is mapped behind the plot of the sheep displaying a river system. As the sheep eat away at the environment, this is seen on the plot as areas of the environment that have a distressed/ netted effect. When the sheep eat, 10 values are added to a store. After all iterations, sheep with over 100 values in their store are sick and empty their store. Additionally, this project creates a Graphical User Interface for the program. Within this, the program is animated so we can watch the stages of all the previous practicals play out on one page. 
## Technologies
Language Used: Python 3.6 
## Launch
To run the program, the files should be opened in Spyder. 
Preferably enter '%matplotlib qt' into the kernel so that the plots show fully as a pop-out. 
## Contents:
  ### 1. Agents Practical
        This practical includes both a framework (containing the functions to be used in the program) and the main program. 
        The aim of this practical was to create a class of agents (which are sheep), assign random values to them and plot these sheep on a scatterplot.
  ### 2. Input/Output Practical
        As with the sheep practical, this contains both a framework and the main program. 
        The aim of this practical was the import data from a csv file into a 2D list (List 1: environment, List 2: list of rows from the csv) into our program. 
        The list we are entering the data into is called our environment and this maps the data from the CSV file showing a river system and the surrounding valleys.  
        The sheep are mapped onto the environment. 
        The code gets the sheep to move around in a for-loop through a dictated number of iterations. 
        The code also gets the sheep to eat the environment and store values from what it eats. 
        At the end, sheep who have been greedy and ended up with a store of more than 100 values will be sick and empty their stores. This will be reflected in the plot of the           environment.        
  ### 3. Communicating Practical
        Again, this practical contains a framework and the main program. 
        The aim of this practical is to get the sheep to interact with one another by sharing resources between them. 
        In this practical, we also get the sheep to shuffle. In order to ensure we can see the sheep shuffling, we assign an ID to them.     
  ### 4. GUI Practical
         The aim of this practical was to give a Graphical User Interface (GUI) to our program. The aim here is to have our program open in a separate window with a menu. 
         This menu should dropdown to offer a 'Run Model' option.
         In this practical, the program is animated so that all the stages carried out in previous practicals can be seen. This program features a stopping condition which makes          the animation stop when the random number is less than 0.1.       
## Sources
https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd 


