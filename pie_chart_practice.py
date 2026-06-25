import matplotlib.pyplot as plt

# Defining the dataset values and category labels
y = [20, 50, 80, 60]
mylabels = ["grapes", "apple", "cherry", "banana"]

# Plotting the data with correct labels argument mapping
plt.pie(y, labels=mylabels)

# Rendering the visualization plot window
plt.show()
