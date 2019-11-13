# importing the required module
import matplotlib.pyplot as plt

# V and I values for Ohmic Conductor
V1 = [0.00, 0.5, 0.75, 1.00, 1.25, 1.75, 2.50, 2.75,  3.25, 3.50]
I1 = [0, 50, 75, 100, 125, 175, 250, 275, 325, 350]

# plotting the points
plt.plot(V1, I1)

# naming the x and y axis
plt.xlabel('Voltage')
plt.ylabel('Current')

# giving a title to my graph
plt.title('Ohmic Conductor')

# function to show the plot
plt.show()

# V and I values for Non-Ohmic Conductor
V2 = [0.00, 0.10, 0.15, 0.20, 0.35, 0.60, 1.00, 1.30,  1.70, 2.50]
I2 = [0, 50, 80, 120, 160, 200, 240, 260, 280, 300]

# plotting the points
plt.plot(V2, I2)

# naming the x and y axis
plt.xlabel('Voltage')
plt.ylabel('Current')

# giving a title to my graph
plt.title('Non-Ohmic Conductor')

# function to show the plot
plt.show()
