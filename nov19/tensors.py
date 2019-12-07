#!/usr/bin/env python

from manimlib.imports import *
title = Title("What are Tensors?    @astroparticular")

# How to make a scalar?
class Slide1(Scene):
    def construct(self):
        G  = Matrix([["0", "B_x", "B_y", "B_z"], 
                    ["-B_x", "0", "E_z", "-E_y"],
                    ["-B_y", "-E_z", "0", "E_x"],
                    ["-B_z", "E_y", "-E_x", "0"]]);

        F = Matrix([["0", "-E_x", "-E_y", "-E_z"], 
                    ["E_x", "0", "-B_z", "B_y"],
                    ["E_y", "B_z", "0", "-B_x"],
                    ["E_z", "-B_y", "B_x", "0"]]);

        # other equation objects
        times = TexMobject("\\otimes");
        eqsn = TexMobject(" = ");
        product = TexMobject("4 \\vec{B} \\cdot \\vec{E}");

        # position settings
        matrices = VGroup(G, times, F, eqsn, product);
        matrices.arrange(0.05 * RIGHT)
        for obj in matrices:
            obj.scale(0.8);

        # braces settings
        Gbrace = Brace(G, DOWN); Gtex = Gbrace.get_tex("G_{\\mu \\nu}");
        Fbrace = Brace(F, DOWN); Ftex = Fbrace.get_tex("F^{\\mu \\nu}");

        # create video
        self.add(title)
        self.play(
            FadeIn(matrices),
        );
        self.play(
            GrowFromCenter(Gbrace),
            Write(Gtex),
        );
        self.play(
            GrowFromCenter(Fbrace),
            Write(Ftex)
        );
        self.wait();

class Slide2(Scene):
    def construct(self):
        GF = TexMobject("G_{\\mu \\nu} F^{\\mu \\nu} = - 4 \\vec{B} \\cdot \\vec{E}");
        ab = TexMobject("a_{\\mu} b^{\\mu} = - a_{0} b^{0} + \\vec{a} \\cdot \\vec{b}");
        GF.scale(2); ab.scale(2);

        self.add(title);
        self.play(
            Write(GF),
        ); self.wait(2);
        self.play(
            Transform(GF, ab),
        );
        self.wait(2);

class Slide3(Scene):
    def construct(self):
        ab = TexMobject("g_{\\mu \\nu} a^{\\mu} b^{\\nu} = a^{\\mu} b_{\\mu}");
        ab.scale(2);

        self.add(title);
        self.play(
            Write(ab),
        ); self.wait(2);

class Slide4(Scene):
    def construct(self):
        metric = Matrix([[-1, 0, 0, 0],
                         [ 0, 1, 0, 0],
                         [ 0, 0, 1, 0],
                         [ 0, 0, 0, 1]]);

        g = TexMobject("\\eta_{\\mu \\nu}");
        gcopy = g.copy();

        eqsn = TexMobject(" = ");
        eqsncopy = eqsn.copy();
        mink = VGroup(g, eqsn, metric);
        mink.arrange(RIGHT);

        b = Matrix([["b_0", "b_1", "b_2", "b_3"]]);
        bT = Matrix([["-b_0"],["b_1"],["b_2"],["b_3"]]);
        eq1 = VGroup(gcopy, b, eqsncopy, bT);
        eq1.arrange(RIGHT);

        b_brace = Brace(b, DOWN); btex = b_brace.get_tex("b^{\\nu}");
        bT_brace = Brace(bT, DOWN); bTtex = bT_brace.get_tex("b_{\\mu}");
        eq1scene = VGroup(eq1, b_brace, bT_brace, btex, bTtex);

        ab = TexMobject("\\eta_{\\mu \\nu} a^{\\mu} b^{\\nu} = a_{\\mu} b^{\\mu} = - a_{0} b^{0} + \\vec{a} \\cdot \\vec{b}");
        ab.scale(1.5);

        self.add(title);
        self.play(
            FadeIn(mink),
        ); self.wait(4);
        self.play(FadeOut(mink));

        self.play(
            FadeIn(eq1),
        ); self.wait();
        self.play(
            GrowFromCenter(b_brace), Write(btex),
            GrowFromCenter(bT_brace), Write(bTtex),
        ); self.wait(4);
        self.play(
            FadeOut(eq1scene),
        );

        self.play(
            Write(ab),
        ); self.wait(7);


class Slide5(Scene):
    def construct(self):
        title = Title("What are tensors?    @astroparticular");
        F_tensor = Matrix([[0, "-E_{x}", "-E_{y}", "-E_{z}"],
                           ["E_{x}", 0, "-B_{z}", "B_{y}"],
                           ["E_{y}", "B_{z}", 0, "-B_{x}"],
                           ["E_{z}", "-B_{y}", "B_{x}", 0]]);

        G_tensor = Matrix([["0", "-B_x", "-B_y", "-B_z"], 
                           ["B_x", "0", "E_z", "-E_y"],
                           ["B_y", "-E_z", "0", "E_x"],
                           ["B_z", "E_y", "-E_x", "0"]]);

        F_tensor.move_to(0);
        Fbrace = Brace(F_tensor, DOWN); Ftex = Fbrace.get_tex("F^{\\mu \\nu}");
        scene_one = VGroup(F_tensor);

        eq3 = TexMobject(
            "F^{0i} = -E^{i}");
        eq3b = TexMobject(
            "F^{i0} = E^{i}");
        eq4 = TexMobject(
            "F^{ij} = -\\epsilon^{ijk} B_{k}");
        eq4b = TexMobject(
            "F^{ji} = \\epsilon^{ijk} B_{k}");
        Fsym = TexMobject(
            "F^{\\mu \\nu} = - F^{\\nu \\mu}");

        eq3.move_to(UP + 2.5 * LEFT);
        eq4.next_to(eq3, 3 * DOWN);
        eq3b.move_to(UP + 2.5 * RIGHT);
        eq4b.next_to(eq3b, 3 * DOWN);
        Fsym.move_to(2 * DOWN);
        scene_two = VGroup(eq3, eq3b, eq4, eq4b, Fsym);

        G_tensor.move_to(0);
        Gbrace = Brace(G_tensor, DOWN); Gtex = Gbrace.get_tex("G^{\\mu \\nu}");
        scene_three = VGroup(G_tensor);
        eq5 = TexMobject( "G^{0i} = -B^{i}")
        eq5b = TexMobject("G^{i0} = B^{i}");
        eq6 = TexMobject( "G^{ij} = -\\epsilon^{ijk} E_{k}")
        eq6b = TexMobject("G^{ji} = \\epsilon^{ijk} E_{k}");
        Gsym = TexMobject(
            "G^{\\mu \\nu} = - G^{\\nu \\mu}");

        eq5.move_to(UP + 2.5 * LEFT);
        eq6.next_to(eq5, 3 * DOWN);
        eq5b.move_to(UP + 2.5 * RIGHT);
        eq6b.next_to(eq5b, 3 * DOWN);
        Gsym.move_to(2 * DOWN);
        scene_four = VGroup(eq5, eq6, eq5b, eq6b, Gsym);

        self.add(title);
        self.play(
            FadeIn(scene_one),
            GrowFromCenter(Fbrace), Write(Ftex),
        ); self.wait(4);

        self.play(
            FadeOut(Ftex), FadeOut(Fbrace),
            Transform(scene_one, scene_two),
        ); self.wait(4);
        self.play(
            FadeOut(scene_one, scene_two),
        );

        self.play(
            FadeIn(scene_three),
            GrowFromCenter(Gbrace), Write(Gtex),
        ); self.wait(4);

        self.play(
            FadeOut(Gtex), FadeOut(Gbrace),
            Transform(scene_three, scene_four),
        ); self.wait(4);



class Slide6(Scene):
    def construct(self):
        eq1 = TexMobject("\\partial_{\\mu} F^{\\mu \\nu} = J^{\\nu}");
        eq2 = TexMobject("\\partial_{\\mu} G^{\\mu \\nu} = 0")

        tensors = VGroup(eq1, eq2);
        tensors.scale(2);
        tensors.arrange(DOWN, buff = 1);
        tensors.move_to(0.5 * DOWN);

        m1 = TexMobject(
            "\\nabla \\cdot \\vec{E} = \\rho"
        );
        m2 = TexMobject(
            "\\nabla \\cross \\vec{B} = \\vec{J} + \\frac{\\partial \\vec{E}}{\\partial t}"
        );
        m3 = TexMobject(
            "\\nabla \\cdot \\vec{B} = 0"
        );
        m4 = TexMobject(
            "\\nabla \\cross \\vec{E} = - \\frac{\\partial \\vec{B}}{\\partial t}"
        );
        Maxwells = VGroup(m1, m2, m3, m4);
        Maxwells.arrange(DOWN, buff = 0.3);

        self.add(title);
        self.play(
            Write(tensors),
        ); self.wait(4);
        self.play(
            Transform(tensors, Maxwells),
        ); self.wait(4),

