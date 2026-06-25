import matplotlib.pyplot as plt

# Defining the extended dataset values and labels
y = [20, 50, 80, 60, 90, 15, 120]
myimages = ["grapes", "apple", "cherry", "banana", "strawberry", "tomato", "mango"]

# Highlighting the 'banana' slice by applying an explosion gap
myexplode = [0, 0, 0, 0.2, 0, 0, 0]

# Mapping custom aesthetic colors to each fruit category
mycolors = ["green", "red", "darkred", "yellow", "red", "hotpink", "gold"]

# Plotting the customized pie chart with explicit mapping parameters
plt.pie(y, labels=myimages, explode=myexplode, colors=mycolors, autopct="%1.1f%%")

# Displaying chart legend for data reference
plt.legend()

# Rendering the visualization
plt.show()
