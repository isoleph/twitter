#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import animation 
from numpy import pi


# elements in plot 
fig = plt.figure()
fig.set_size_inches(10, 5, True)
ax = plt.axes(xlim=(-3, 3), ylim=(0, 20))
line, = ax.plot([], [], lw=2, 
        label=r"$g_{n} = \frac{\sin(nx)}{\pi x}$")

# text container indicates iteration of n = _
n_text = ax.text(0.875, 0.825, "", transform=ax.transAxes)

# initializing function for animation
def init():
    line.set_data([], [])
    n_text.set_text("")
    return line, n_text

# function to describe animation
def animate(n):
    x = np.linspace(-5, 5, 1000)
    y = 1/pi * np.sin(n*x)/x 
    line.set_data(x, y)
    n_text.set_text("n = %i" % n)
    return line, n_text

# main code to execute
def main():
    plt.title("Generalized Distribution: Normalized Sinc")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend()
    plt.grid(True)

    # create animation
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=80,
            interval=30, blit=True)
    anim.save("sinc_animation.mp4", fps=30, 
            extra_args=["-vcodec", "libx264"], dpi=250)
    return 0

main()
