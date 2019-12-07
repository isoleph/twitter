#!/usr/bin/env python3
# manim script to animate the hamiltonian
from manimlib.imports import *

class Slide0(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq0a = TexMobject("\\delta S")
        eq0b = TexMobject("=")
        eq0c = TexMobject("\\delta \\int \\dd{t} \\cdot \\mathcal{L}(q, \\dot{q})")

        ScreenOne = VGroup(eq0a, eq0b, eq0c)
        ScreenOne.arrange(RIGHT)
        ScreenOne.scale(2)

        self.add(title)
        self.play(
            Write(ScreenOne)
        ); self.wait(3)


class Slide1(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq1a = TexMobject("\\delta S")
        eq1b = TexMobject("=")
        eq1c = TexMobject("\\int \\dd{t} \\cdot \\Big( \\pdv[]{\\mathcal{L}}{q} \\delta q + \\pdv[]{\\mathcal{L}}{\\dot{q}} \\delta \\dot{q} \\Big)")
        ScreenOne = VGroup(eq1a, eq1b, eq1c)
        ScreenOne.arrange(RIGHT)
        ScreenOne.scale(2)

        self.add(title)
        self.play(
            Write(ScreenOne)
        ); self.wait(3)

class Slide2(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq1a = TexMobject("\\pdv[]{\\mathcal{L}}{q}")
        eq1b = TexMobject("=")
        eq1c = TexMobject("\\dv[]{}{t}")
        eq1d = TexMobject(" \\pdv[]{\\mathcal{L}}{\\dot{q}}")
        
        eq2a = eq1a.copy()
        eq2b = eq1b.copy() 
        eq2c = eq1c.copy()
        eq2d = TexMobject("p")

        eq3a = eq2a.copy()
        eq3b = eq2b.copy()
        eq3c = TexMobject("\\dot{p}")
        ScreenOne = VGroup(eq1a, eq1b, eq1c, eq1d)
        ScreenTwo = VGroup(eq2a, eq2b, eq2c, eq2d)
        ScreenThree= VGroup(eq3a, eq3b, eq3c)

        ScreenOne.arrange(RIGHT)
        ScreenOne.scale(2)
        ScreenTwo.arrange(RIGHT)
        ScreenTwo.scale(2)
        ScreenThree.arrange(RIGHT)
        ScreenThree.scale(2)

        self.add(title)
        self.play(
            Write(ScreenOne)
        ); self.wait(2)

        self.play(
            Transform(ScreenOne, ScreenTwo),
        ); self.wait(2)

        self.remove(ScreenOne)
        self.play(
            Transform(ScreenTwo, ScreenThree)
        ); self.wait(3)

class Slide3(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq1a = TexMobject("\\delta S")
        eq1b = TexMobject("=")
        eq1c = TexMobject("\\int \\dd{t} \\cdot \\Big( \\pdv[]{\\mathcal{L}}{q} \\delta q + \\pdv[]{\\mathcal{L}}{\\dot{q}} \\delta \\dot{q} \\Big)")

        eq2a = eq1a.copy()
        eq2b = eq1b.copy()
        eq2c = TexMobject("\\int \\dd{t} \\cdot \\Big( \\dot{p} \\delta q + p \\delta \\dot{q} \\Big)")

        eq3a = eq2a.copy()
        eq3b = eq2b.copy()
        eq3c = TexMobject("\\int \\dd{t} \\cdot \\dv[]{t} (p \\delta q)")

        eq4a = eq3a.copy()
        eq4b = eq3b.copy()
        eq4c = TexMobject("p \\delta q")

        ScreenOne = VGroup(eq1a, eq1b, eq1c)
        ScreenOne.arrange(RIGHT)
        ScreenOne.scale(2)

        ScreenTwo = VGroup(eq2a, eq2b, eq2c)
        ScreenTwo.arrange(RIGHT)
        ScreenTwo.scale(2)

        ScreenThree = VGroup(eq3a, eq3b, eq3c)
        ScreenThree.arrange(RIGHT)
        ScreenThree.scale(2)

        ScreenFour = VGroup(eq4a, eq4b, eq4c)
        ScreenFour.arrange(RIGHT)
        ScreenFour.scale(2)

        self.add(title)
        self.play(
            Write(ScreenOne)
        ); self.wait(3)
        self.play(
            Transform(ScreenOne, ScreenTwo)
        ); self.wait(3)
        self.remove(ScreenOne)
        self.play(
            Transform(ScreenTwo, ScreenThree)
        ); self.wait(3)
        self.remove(ScreenTwo)
        self.play(
            Transform(ScreenThree, ScreenFour)
        ); self.wait(4)

class EqFrame(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq1a = TexMobject("\\pdv[]{\\mathcal{L}}{\\dot{q}} = p")
        eq1b = TexMobject("\\pdv[]{\\mathcal{L}}{q} = \\dot{p}")

        eq1a.arrange(RIGHT)
        eq1b.arrange(RIGHT)

        eq1a.move_to(UP)
        eq1b.next_to(eq1a, 4 * DOWN)
        eq1a.scale(1.5)
        eq1b.scale(1.5)

        ScreenOne = VGroup(eq1a, eq1b)
        self.add(title)
        self.play(
            Write(ScreenOne)
        ); self.wait(3)

class Slide4(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")
        eq1 = TexMobject("\\delta S = \\mathcal{L} \\delta t - p \\delta q = 0.")
        eq2 = TexMobject("\\delta S = \\mathcal{L} \\delta t - p \\dot{q} \\delta t ")
        eq3 = TexMobject("\\delta S = (\\mathcal{L} - p \\dot{q}) \\delta t")
        eq4 = TexMobject("\\pdv[]{\\mathcal{S}}{t} = \\mathcal{L} - p \\dot{q}")

        contents = VGroup(eq1, eq2, eq3, eq4)
        for obj in contents:
            obj.scale(2)

        self.add(title)
        self.play(
            Write(eq1)
        ); self.wait(2)

        self.play(
            Transform(eq1, eq2)
        ); self.wait(2)

        self.remove(eq1)
        self.play(
            Transform(eq2, eq3)
        ); self.wait(2)

        self.remove(eq2)
        self.play(
            Transform(eq3, eq4)
        ); self.wait(3)


class Lagrangian(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")
        lagr = TexMobject("\\mathcal{L} = \\frac{1}{2} \\dot{q}^2 - U(q)")
        lagr.scale(2)

        self.add(title)
        self.play(
            Write(lagr)
        ); self.wait(3)

class Slide5(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")
        eq1a = TexMobject("\\pdv[]{\\mathcal{S}}{t} = ")
        eq1b = TexMobject("\\mathcal{L} - p \\dot{q}")

        eq2a = eq1a.copy()
        eq3a = eq1a.copy()
        eq4a = eq1a.copy()

        eq2b = TexMobject("\\mathcal{L} - \\pdv{\\mathcal{L}}{\\dot{q}} \\dot{q}")
        eq3b = TexMobject("\\frac{1}{2} \\dot{q}^2 - U(q) - \\dot{q}^2")
        eq4b = TexMobject("- \\frac{1}{2} \\dot{q}^2 - U(q)")

        eq1 = VGroup(eq1a, eq1b)
        eq1.arrange(RIGHT)
        eq1.scale(2)

        eq2 = VGroup(eq2a, eq2b)
        eq2.arrange(RIGHT)
        eq2.scale(2)

        eq3 = VGroup(eq3a, eq3b)
        eq3.arrange(RIGHT)
        eq3.scale(2)

        eq4 = VGroup(eq4a, eq4b)
        eq4.arrange(RIGHT)
        eq4.scale(2)

        brace = Brace(eq4b, DOWN)
        bracetex = brace.get_tex("-H")

        self.add(title)
        self.play(
           Write(eq1) 
        ); self.wait(2)

        self.play(
            Transform(eq1, eq2)
        ); self.wait(4)

        self.remove(eq1)
        self.play(
            Transform(eq2, eq3)
        ); self.wait(4)

        self.remove(eq2)

        self.play(
            Transform(eq3, eq4),
            GrowFromCenter(brace),
            Write(bracetex)
        ); self.wait(4)

        self.remove(eq3)

        self.play(
        )

class Slide6(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        Hamiltonian = TexMobject("H = \sum_{i} p_{i} \\dot{q}_{i} - \\mathcal{L}")
        Hamiltonian2 = TexMobject("H = \\frac{1}{2} \\dot{q}^2 + U(q)")

        Hamiltonian.scale(2); Hamiltonian2.scale(2);

        self.add(title)
        self.play(
            Write(Hamiltonian)
        ); self.wait(3);

        self.play(
            Transform(Hamiltonian, Hamiltonian2)
        ); self.wait(3)

class Slide7(Scene):
    def construct(self):
        title = Title("Finding the Hamiltonian \t @astroparticular")

        eq1 = TexMobject("\\pdv[]{H}{p_{i}} = \\dot{q}_{i}")
        eq2 = TexMobject("\\pdv[]{H}{q_{i}} = -\\dot{p}_{i}")

        eq1.scale(2)
        eq2.scale(2)

        eq1.move_to(UP)
        eq2.next_to(eq1, 1.5 * DOWN)

        ScreenOne = VGroup(eq1, eq2)

        self.add(title)
        self.play(
            Write(ScreenOne),
        ); self.wait(4)

