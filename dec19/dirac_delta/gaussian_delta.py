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
        label=r"$g_{n} = \sqrt{\frac{n}{\pi}} e^{-nx^2}$")

# text container indicates iteration of n = _ 
n_text = ax.text(0.875, 0.825, "", transform=ax.transAxes)

# initializing function for animation
def init():
    line.set_data([], [])
    n_text.set_text("")
    return line, n_text

# function to describe animation
def animate(n):
    i = 10 * n # use multiples of n instead
    x = np.linspace(-5, 5, 1000)
    y = (i/pi)**(1/2) * np.exp(-i*x**2) 
    line.set_data(x, y)
    n_text.set_text("n = %i" % i)
    return line, n_text

# main code to execute
def main():
    # plot specs
    plt.title("Generalized Distribution: Normalized Gaussian")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.legend()
    plt.grid(True)

    # create animation
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=1,
            blit=True)
    anim.save("gauss_animation.mp4", fps=60, 
            extra_args=["-vcodec", "libx264"], dpi=250)
    return 0

main()
