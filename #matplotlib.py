#matplotlib
import matplotlib.pyplot as pl
year=['2015','2016','2017','2018','2019'] # list of years
p=[98.50,70.25,55.20,90.5,61.50] #list of pass percentage
j=['b','g','r','m','c'] # color code of bar charts
pl.bar(year, p, width=0.2, color=j) # bar( ) function to create the bar chart
pl.xlabel("year") # label for x-axis
pl.ylabel("Pass%") # label for y-axis
pl.show( ) # function to display bar chart