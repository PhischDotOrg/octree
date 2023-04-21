import numpy as np
import pandas as pd

import plotly.offline.graph_objects as go


# Create Pandas Frame with 10 random point in 3D space. Coordinates are between -100 and 100.
def create_points(numPoints = 10):
    # Create random points
    points = np.random.randint(-100, 100, size=(numPoints, 3))
    # Create Pandas Frame
    return pd.DataFrame(points, columns=['x', 'y', 'z'])

# 3D Scatter Plot of Pandas frame containing points using Plotly
def plot_points_plotly(points=None):
    if points is None:
        points = create_points()

    fig = go.Figure(data=[
        go.Scatter3d(
            x=points['x'],
            y=points['y'],
            z=points['z'],
            mode='markers')
        ])
    fig.show()

plot_points_plotly()

