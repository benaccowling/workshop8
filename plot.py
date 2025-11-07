# These libraries contain useful tools we will use to load, processes and plot data
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from os.path import splitext
from inspect import getfullargspec

# This allows us to pass arguments to our program
from sys import argv
# The first argument is always the name of the program; we will remove it
files = argv[1:]

# A list of all the files we wish to process
# Comment this line to use command line arguments
files = ['20_deg_C.csv']

i = 0
# We will create a plot from every csv file passed to the program
for fname in files:
    # If the filename is not a csv file, it will be skipped
    if fname[-4:] != '.csv': continue
    i += 1

    # Load the x and y data from the csv file. Note that the column indexes start from 0, not 1.
    try:
        data = np.loadtxt(fname,delimiter=",",skiprows=1)
    except:
        print("Could not process file",fname,". This is probably because it contains text outside of the header line. It has been skipped.")
        continue
    x = data[:,0]
    y = data[:,1]
    
    # ----- DATA MANIPULATION --------------------------------------------------------------
    # Uncomment the relevent line from this section or add your own code

    # Convert time from seconds to minutes
    # x = x/60

    # Convert y to ln(y)
    # y = np.log(y)

    # --------------------------------------------------------------------------------------


    # ----- PLOTTING DETAILS ---------------------------------------------------------------
    
    # Create the figure
    fig = plt.figure()
    # Create the "Axes", which contains information for the graph
    ax = plt.axes()

    # This creates a line graph, adding a straight line between each point
    # in the input data file
    ax.plot(x,y,label='Data')

    # Add labels to the x and y axes
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Absorbance")

    # Add a title to the graph; by default this is the
    # name of the input data file
    ax.set_title(fname)

    # --------------------------------------------------------------------------------------

    fig.savefig(splitext(fname)[0]+".png")

print('Successfully plotted '+str(i)+' file(s).')
