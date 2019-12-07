#!/usr/bin/env python3
# manim script to animate the hamiltonian
from manimlib.imports import *


class Slide0(Scene):
    def construct(self):

        title = Title("Squaring the Dirac Equation @astroparticular")
        dirac = TexMobject(r"(i\gamma^{\mu} \partial_{\mu} - m)\psi = 0.")
        dirac.scale(2)

        dirac2 = TexMobject(r"(i\gamma^{\mu} \partial_{\mu} - m)(- i\gamma^{\nu} \partial_{\nu} - m)\phi = 0")
        dirac2.scale(1.5)

        dirac3 = TexMobject(r"(\gamma^{\mu}\gamma^{\nu}\partial_{\mu}\partial_{\nu} + m^2)\phi = 0")
        dirac3.scale(2)

        dirac4 = TexMobject(r"(\partial_{\mu}\partial^{\mu} + m^2)\phi = 0.")
        dirac4.scale(2)

        dirac5 = TexMobject(r"(\partial_{t}^2 - \laplacian +m^2)\phi = 0.")
        dirac5.scale(2)

        dirac6 = TexMobject(r"(\Box + m^2)\phi = 0.")
        dirac6.scale(2)

        self.add(title)
        self.play(
            Write(dirac)
        ); self.wait(2)

        self.play(
            Transform(dirac, dirac2),
        ); self.wait(3);

        self.remove(dirac)
        self.play(
            Transform(dirac2, dirac3),
        ); self.wait(3)

        self.remove(dirac2)
        self.play(
            Transform(dirac3, dirac4),
        ); self.wait(3)
        
        self.remove(dirac3)
        self.play(
            Transform(dirac4, dirac5),
        ); self.wait(3);

        self.remove(dirac4)
        self.play(
            Transform(dirac5, dirac6),
        ); self.wait(3);


class Slide1(Scene):
    def construct(self):
        title = Title("Squaring the Dirac Equation @astroparticular")

        gammas = TexMobject(r"\gamma^{\mu}\gamma^{\nu}} + \gamma^{\nu}\gamma^{\mu} = 2g^{\mu\nu} 1")
        gammas.scale(2)

        self.add(title)
        self.play(
            Write(gammas),
        ); self.wait(3)
