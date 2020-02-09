#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from manimlib.imports import *


class S1(Scene):
    def construct(self):

        # credit
        credit = TextMobject("@astroparticular").scale(0.75)
        credit.to_corner(DOWN + RIGHT)

        # objects
        objs = VGroup(
            TexMobject("\\div{\\vb{E}} = \\frac{\\rho}{\\epsilon_{0}}"),
            TexMobject("\\div{\\vb{B}} = 0"),
            TexMobject("\\curl{\\vb{E}} = - \\pdv{\\vb{B}}{t}"),
            TexMobject("\\curl{\\vb{B}} = \\mu_{0} \\vb{J} +"
                       "\\frac{1}{\\mu_{0} \\epsilon_{0}} \\pdv{{\\vb{E}}}{t}")
        )

        nobjs = VGroup(
            TexMobject("\\div{\\vb{E}} = \\frac{\\rho_{e}}{\\epsilon_{0}}"),
            TexMobject("\\div{\\vb{B}} = \\mu_{0}", "\\rho_{m}").set_color_by_tex(
                       "\\rho_{m}", "#8B0000"),
            TexMobject("\\curl{\\vb{E}} = - \\pdv{\\vb{B}}{t} - \\mu_{0}",
                       "\\vb{j}_{m}").set_color_by_tex("\\vb{j}_{m}", "#00008B"),
            TexMobject("\\curl{\\vb{B}} = \\mu_{0}", " \\vb{j}_{e}", 
                       " + \\frac{1}{\\mu_{0} \\epsilon_{0}} \\pdv{{\\vb{E}}}{t}")
        )

        # placing
        objs.scale(1.1)
        objs.move_to(DOWN)
        objs.arrange(DOWN)

        nobjs.scale(1.1)
        nobjs.move_to(DOWN)
        nobjs.arrange(DOWN)

        # scene
        self.add(credit)
        self.play(
            Write(objs),
        ); self.wait(3)

        self.play(
            Transform(objs, nobjs),
        ); self.wait(3)
