# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Get the data
from pyodide.http import open_url
url = 'https://raw.githubusercontent.com/alanjones2/uk-historical-weather/main/data/Heathrow.csv'
url_content = open_url(url)
df = pd.read_csv(url_content)

# filter the data for the year 2020
df = df[df['Year']==2021]

# Function to plot the chart
def plot(chart):
   fig, ax = plt.subplots()
   df.plot(y=chart, x='Month', figsize=(8,4),ax=ax)
   pyscript.write("chart",fig)
   
# Set up a proxy to be called when a 'change'
# event occurs in the select control
from js import document
from pyodide import create_proxy
# Read the value of the select control
# and call 'plot'
def selectChange(event):
   choice = document.getElementById("select").value
   plot(choice)

# set the proxy
def setup():
   # Create a JsProxy for the callback function
   change_proxy = create_proxy(selectChange)
   e = document.getElementById("select")
   e.addEventListener("change", change_proxy)

setup()

# Intitially call plot with 'Tmax'
plot('Tmax')