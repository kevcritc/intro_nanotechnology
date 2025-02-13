#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:19:09 2024

@author: phykc
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter


plt.rcParams['animation.ffmpeg_path'] = '/Users/phykc/anaconda3/bin/ffmpeg'

# Create an FFMpeg writer object
writer = FFMpegWriter(fps=30, metadata=dict(artist='Me'), bitrate=1800)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Remove the axis for a cleaner view
ax.axis('off')

# Proton (represented as a red dot)
proton, = ax.plot(0, 0, 'ro', markersize=12, label='Proton')

# Electron (represented as a blue dot)
electron, = ax.plot([], [], 'bo', markersize=6, label='Electron')

# Elliptical orbit parameters
orbit_a = 1.0  # Semi-major axis
orbit_b = 0.9  # Semi-minor axis
orbit_speed = 2

# Generate the path of the elliptical orbit
t = np.linspace(0, 2*np.pi, 300)
x_path = orbit_a * np.cos(t)
y_path = orbit_b * np.sin(t)

# Plot the dotted line for the orbit path
ax.plot(x_path, y_path, 'k--', alpha=0.5)  # 'k--' creates a black dotted line

# Initialize the position of the electron
def init():
    electron.set_data([], [])
    return electron,

# Update function for the animation
def update(frame):
    # Calculate the position of the electron on an elliptical orbit
    x = orbit_a * np.cos(orbit_speed * frame)
    y = orbit_b * np.sin(orbit_speed * frame)
    electron.set_data(x, y)
    return electron,

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200), init_func=init, blit=True, interval=20)
ani.save('orbit_animation.mp4', writer=writer)

# Display the animation
plt.show()