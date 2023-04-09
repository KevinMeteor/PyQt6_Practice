"""
Introduction :
    A star-shape scatter plot created by using the PlotWidget widget
---------------------------------------------------------
Set parameter :
used_device : boalean (default False) 
    set True, if using GPU, import cupy  
    set False, if using CPU, import numpy 
---------------------------------------------------------
Origianl Code Source : https://gist.github.com/Lauszus/16d37c476f24596f8bf43a74847a2fc0

Program Rewriting Author : LIN, KAI-LUN at NATIONAL TAIPEI UNIVERSITY

Rewriting Date : 2023/04/09
---------------------------------------------------------
"""
import sys
import pyqtgraph as pg

# set parameter 
used_device = False

if used_device == True:
    import cupy as xp
else:
    import numpy as xp


# 2D rotate matrix 
def retate_matrix_2D(X, theta, xp=xp):
    M = xp.array([
        [xp.sin(theta), -xp.cos(theta)],
        [xp.cos(theta),  xp.sin(theta)]
    ])
    return M @ X 


# Set white background and black foreground
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

# Generate standard t random sample
n = 10**6
df = 2.3
data1 = xp.random.standard_t(df, size=(2, n))
data2 = retate_matrix_2D(xp.random.standard_t(df, size=(2, n)) , theta=xp.pi/4)


if used_device == True:
    data = (data1 + data2).get()
else:
    data = data1 + data2


# Create the main application instance
app = pg.mkQApp()

# Create the view
view = pg.PlotWidget()
view.resize(680, 480)
view.setWindowTitle('Scatter Plot of a Star')
view.setAspectLocked(True)
view.show()

# Create the scatter plot and add it to the view
pen = pg.mkPen(width=5, color='tomato')
scatter = pg.ScatterPlotItem(pen=pen, symbol='o', size=1)
view.addItem(scatter)


# Convert data array into a list of dictionaries with the x,y-coordinates
scatter.setData(data[0,:], data[1,:])


if __name__ == "__main__":
    # Gracefully exit the application
    sys.exit(app.exec())