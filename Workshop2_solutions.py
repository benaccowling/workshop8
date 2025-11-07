#!/usr/bin/env python
# coding: utf-8

# # Workshop 2
# 
# In this exercise we will use the python notebook to select, manipulate and plot data from a data frame. We will be using two datasets: one on different kinds of renewable energy generation by country, and another on meteorite sightings.
# 

# ### Step 1
# 
# Using the same approach as in the previous workshop, read the data file `renewables.csv` from this folder and store it in a variable called `renewables`.
# 
# Display the contents of the data frame using a print statement.
# 
# 

# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
renewables = pd.read_csv("renewables.csv")
print(renewables)


# ### Step 2
# 
# Next import the `IPython.display` module and give it the nickname `ipd`. Use the `display` function from this module to show the data frame in a more readable format.

# In[28]:


import IPython.display as ipd
ipd.display(renewables)


# ### Step 3
# 
# The last 21 rows of the data frame contain data for the United States. Use `.iloc[,]` to select the last 10 rows and store then in a data frame called `usa10`.

# In[29]:


usa10 = renewables.iloc[-10:,:]
print(usa10)


# ### Step 4
# 
# Now use `.mean()` to produce a dataframe called `usa_decade` with one row containing mean values for the last decade. Print the result. Check that the mean Renewables-pc is 8.183%.
# 
# If you get an error message, check the documentation for the mean function blow, and in particular the `numeric_only` argument. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html

# In[30]:


usa_decade = usa10.mean(numeric_only=True)
print(usa_decade)


# ### Step 5
# 
# In the lectures the following code was made to print the rows for the year 2020:
# 
# `print( emissions[emissions["Year"]==2020] )`
# 
# Use a similar approach to create a dataframe called renew2020 containing the renewables data for the year 2020.

# In[31]:


renew2020 = renewables[renewables["Year"]==2020]
print(renew2020)


# ### Step 6
# 
# Pandas can plot a bar chart using the function
# `dataframe.plot.bar(x="x column",y="y column")`
# where dataframe and the column names need to be changed. Plot a bar chart of the `Electricity-renewables-TWh` column by country using the data frame `renew2020`. Make sure the bars are labelled.
# 
# Find out how to label the y axis with the units `TWh`.

# In[32]:


ax = renew2020.plot.bar(x="Entity",y="Electricity-renewables-TWh")
ax.set_ylabel("TWh")
plt.show()


# ### Step 7
# 
# Using plotly.express and the function shown in the vizualisation lecture, plot three choropleth maps (a map with countries colored by value) of each of the three electricity generation columns.
# 
# In order to display all three maps, you will need to assign the output of the plot function to a variable (say `fig`) and then use
#  `fig.show()` in between each plot.

# In[33]:


import plotly.express as px
fig = px.choropleth(renew2020,locations="Entity",locationmode="country names",color="Electricity-renewables-TWh")
fig.show()


# 
# ### Step 8
# 
# Read in the file `meteorites.csv` and plot the observations colored by year.
# 
# (If you don't want to use color, add the argument `color_continuous_scale="greys"`.)
# 
# 

# In[34]:


import numpy as np
meteors = pd.read_csv("meteorites.csv")
# plot as scatter plot
fig = px.scatter_map(meteors,lon="long",lat="lat",color="year",zoom=1,color_continuous_scale="greys")
fig.update_layout(mapbox_style="open-street-map")
fig.show()


# ### Step 9
# 
# Now set the point size to show the mass of the meterorite. You will probably get an error. Read the error message and see if you can deduce the cause of the problem.
# 
# The following function may help in fixing it:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
# 
# The smallest meteorites observed are now impossible to see. Make a new column, set to log(mass+1) (where the +1 avoids errors from taking log(0)), and use this as the point size.

# In[38]:


import numpy as np
meteors = pd.read_csv("meteorites.csv")
meteors = meteors.fillna(0.0)
# convert to log mass
meteors["mass1"] = np.round(np.log(meteors["mass"]+1))
print(meteors.describe())
# plot as scatter plot
fig = px.scatter_map(meteors,lon="long",lat="lat",color="year",size="mass1",zoom=1)
fig.update_layout(mapbox_style="open-street-map")
fig.show()


# In[ ]:




