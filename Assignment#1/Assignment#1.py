import wbdata as wb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the indicator for GNI per Capita
indicator = {'NY.GNP.PCAP.CD': 'GNI per Capita'}

# Set up the regions
regions = ['SSF', 'MEA', 'ECS', 'SAS', 'EAS', 'NAC', 'LCN']

# Create the dataframe
df = wb.get_dataframe(indicator, country=regions, convert_date=False)
df = df.reset_index()

# Adjust the figure and the text sizes
fig, ax = plt.subplots(figsize=(18, 8))
plt.xticks(fontsize=14)
plt.yticks(fontsize=11)

# Fixed colors for each region. Used later when creating the bar chart.
colors_dict = {
    'East Asia & Pacific': '#97f0aa',
    'Europe & Central Asia': '#ff9595',
    'Latin America & Caribbean': '#86c4ff',
    'Middle East & North Africa': '#a3e2e8',
    'South Asia': '#fdff99',
    'Sub-Saharan Africa': '#d7b3ff'
}

# Function to create a chart for a given year
# Puts the title and year as text
# Query the data frame by year sorted by ascending values
# Draw the bar chart using `barh`
# Learned the details of beautiful bar chart and gif creation here:
# https://towardsdatascience.com/bar-chart-race-in-python-with-matplotlib-8e687a5c8a41
def bar_chart(year):
    ax.clear()
    ax.grid(which='major', axis='x', linestyle='-')
    ax.text(0, 1.05, 'GNI per Capita by region from 1975 to 2018',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(1, 0.4, year, transform=ax.transAxes, size=35, ha='right')

    df1 = df.query("date == '{}'".format(year)).sort_values(by='GNI per Capita', ascending=True)
    colors = [colors_dict[country] for country in df1['country']]
    ax.barh(df1['country'], df1['GNI per Capita'], color=colors)

    plt.box(False)

animator = animation.FuncAnimation(fig, bar_chart, frames=range(1975, 2019))
animator.save('./GNI.gif', fps=2)
