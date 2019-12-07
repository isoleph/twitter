#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from manimlib.imports import *

class Slide0(Scene):
    def construct(self):
        title = Title("Dirac Delta @astroparticular")

        dirac_defn = TexMobject(r"\int_{-\infty}^{\infty} \delta(x - a) f(x) \dd{x} = f(a)")
        dirac_defn2 = TexMobject(r"\int_{-\infty}^{\infty} \delta(x) \dd{x} = 1")
        dirac_defn.scale(2)
        dirac_defn2.scale(2)

        self.add(title)
        self.play(
            Write(dirac_defn)
        ); self.wait(3)
        self.play(
            FadeOutAndShiftDown(dirac_defn),
        )
        self.play(
            Write(dirac_defn2),
        ); self.wait(3)

class Slide1(Scene):
    def construct(self):
        title = Title("Dirac Delta @astroparticular")
        
        delta = TexMobject(r"\delta(x) = ")
        eq1 = TexMobject(r"\lim_{n\to \infty} \sqrt{\frac{n}{\pi}} e^{-nx^2}")
        eq2 = TexMobject(r"\lim_{n\to \infty} \frac{\sin(nx)}{\pi x}")
        eq1.move_to(4 * RIGHT)

        delta.move_to(3 * LEFT)
        eqs = VGroup(eq1, eq2)
        eqs.arrange(1.5 * DOWN)
        eqbrace = Brace(eqs, LEFT)

        self.add(title)
        self.play(
            Write(delta),
            GrowFromCenter(eqbrace),
            Write(eqs),
        ); self.wait(3)

class Slide2(Scene):
    def construct(self):
        title = Title("Dirac Delta @astroparticular")
        
        delta = TexMobject(r"\delta(x - a) = ")
        eq1 = TexMobject(r"\infty,\  x = a")
        eq2 = TexMobject(r"0,\  x \neq a")
        eq1.move_to(4 * RIGHT)

        delta.move_to(3 * LEFT)
        eqs = VGroup(eq1, eq2)
        eqs.arrange(1.5 * DOWN)
        eqbrace = Brace(eqs, LEFT)

        self.add(title)
        self.play(
            Write(delta),
            GrowFromCenter(eqbrace),
            Write(eqs),
        ); self.wait(3)
