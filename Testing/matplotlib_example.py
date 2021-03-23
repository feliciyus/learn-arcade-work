"""
Line chart with four values.
The x-axis defaults to start at zero.
"""
import matplotlib.pyplot as plt
import numpy

x = [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

plt.annotate('Here',
             xy = (2, 3),
             xycoords = 'data',
             xytext = (-40, 20),
             textcoords = 'offset points',
             arrowprops = dict(arrowstyle="->",
                               connectionstyle="arc,angleA=0,armA=30,rad=10"),
             )

# First character: Line style
# One of '-', '--',  '-.', ':', 'None', ' ', "

# Second character: color
# http://matplotlib.org/1.4.2/api/colors_api.html

# Third character: marker shape
# http://matplotlib.org/1.4.2/api/markers_api.html

plt.plot(x, y1, '-ro', label="Series 1")
plt.plot(x, y2, '--g', label="Series 2")

labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']
plt.xticks(x, labels)

legend = plt.legend(loc='upper center', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()

"""
How to do a bar chart.
"""
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

plt.bar(x, y)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()

"""
Using the numpy package to graph a function over
a range of values.
"""

x = numpy.arange(0.0, 2.0, 0.001)
y = numpy.sin(2 * numpy.pi * x)

plt.plot(x, y)

# 'b' means blue. 'alpha' is the transparency.
plt.fill(x, y, 'b', alpha=0.3)

plt.ylabel('Element Value')
plt.xlabel('Element')

plt.show()

"""
Create a pie chart
"""

# Labels for the pie chart
labels = ['C', 'Java', 'Objective-C', 'C++', 'C#', 'PHP', 'Python']

# Sizes for each label. We use this to make a percent
sizes = [17, 14, 9, 6, 5, 3, 2.5]

# For list of colors, see:
# https://matplotlib.org/examples/color/named_colors.html
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'darkcyan', 'aquamarine', 'rosybrown']

# How far out to pull a slice. Normally zero.
explode = (0, 0.0, 0, 0, 0, 0, 0.2)

# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

# Finally, plot the chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.show()
