from manim import *

class AliAvaruus(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y")).shift(UP * 1.8)
        z_label = axes.get_z_axis_label(Tex("z")).shift(OUT * 0.5)


        
        self.set_camera_orientation(zoom=0.5)

        self.play(FadeIn(axes), FadeIn(x_label), FadeIn(y_label), FadeIn(z_label))

        # luodaan vektorit
        vector2 = Vector(axes.c2p(0, 0, 1), color=RED)
        vector2.save_state()
        v2_label = MathTex("\overline{v}_2=(0, 0, 1)", color=RED).next_to(vector2, 3*UP)
        
        vector1 = Vector(axes.c2p(1, 1, 0), color=GREEN)
        vector1.save_state()
        v1_label = MathTex("\overline{v}_1=(1, 1, 0)", color=GREEN).next_to(vector1, RIGHT)
        
        # nää pitää noi labelit paikoillaa
        v1_label.add_updater(
            lambda mobject: self.add_fixed_in_frame_mobjects(v1_label)
        )
        v2_label.add_updater(
            lambda mobject: self.add_fixed_in_frame_mobjects(v2_label)
        )

        # näytetää eka vektori
        self.play(Create(vector1), Write(v1_label))
        self.wait(1)
        self.play(ApplyMethod(v1_label.to_corner, UL))
        v1_label.save_state()
        self.wait(1.5)

        #viiva-avaruus
        line = Line3D(start=axes.c2p(6, 6, 0), end=axes.c2p(-6, -6, 0), color=BLUE)
        line_label = MathTex("span(\overline{v}_1)", color=BLUE).shift(2*UP)
        self.play(Create(line), runtime=2)
        self.wait()
        self.add_fixed_in_frame_mobjects(line_label)
        self.play(Write(line_label))
        self.wait()
        self.play(ApplyMethod(line_label.to_corner, DL))
        self.wait()

        # käännetää kamera
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1, run_time=1.5)
        self.play(Create(vector2), Write(v2_label))
        self.wait(1)
        self.play(v2_label.animate.next_to(v1_label, DOWN))
        v2_label.save_state()
        self.wait(1.5)
        self.play(Unwrite(line_label),FadeOut(line), runtime=1)
        self.wait()

        # pyörimine alkaa
        self.begin_ambient_camera_rotation(rate=0.35)

        
        
        surface = Surface(
            lambda u, v: axes.c2p(u, u, v),
            u_range=(-4, 4),
            v_range=(-4, 4),
            fill_opacity=0.3,
            resolution=15,
        )
        s_label = MathTex("span(\overline{v}_1,\overline{v}_2)", color=BLUE)


        # näytetää aliavaruus
        self.play(FadeIn(surface))
        self.wait()
        self.add_fixed_in_frame_mobjects(s_label)
        s_label.to_corner(UR)
        self.wait(1.5)

        # luodaa pisteet
        dot1 = Dot3D(axes.c2p(2,2,-1))
        dot1.save_state()
        dot1.generate_target()
        dot1_label = MathTex("(2,2,-1)").shift(2*DOWN + 3*LEFT)
        dot1_label.add_updater(
            lambda mobject: self.add_fixed_in_frame_mobjects(dot1_label)
        )
        dot1_label.save_state()
        dot1_label.generate_target()
        self.stop_ambient_camera_rotation()
        self.wait(1)
        
        self.play(Create(dot1),Write(dot1_label))
        
        self.wait(2)
        self.play(Indicate(dot1), runtime=1.5)
        self.wait()
        self.play(Indicate(dot1), runtime=1.5)
        self.wait()
        self.play(dot1_label.animate.next_to(v2_label, DOWN))
        self.wait()

        # muokkaillaa vektoreita
        vector1.generate_target()
        vector1.target = Vector(axes.c2p(2, 2, 0), color=GREEN)
        v1_label.generate_target()
        v1_label.target = MathTex("2\overline{v}_1=(2, 2, 0)", color=GREEN).to_corner(UL)
        self.play(MoveToTarget(vector1),MoveToTarget(v1_label))
        self.wait()
        vector2.generate_target()
        vector2.target = Vector(axes.c2p(0, 0, -1), color=RED).shift(axes.c2p(2, 2, 0))
        v2_label.generate_target()
        v2_label.target = MathTex("-1 \overline{v}_2=(0, 0, -1)", color=RED).next_to(v1_label,DOWN)
        self.play(MoveToTarget(vector2),MoveToTarget(v2_label))

        self.begin_ambient_camera_rotation(rate=0.55)
        self.wait(5.5)
        self.stop_ambient_camera_rotation()


        self.play(Restore(vector1), Restore(v1_label), Restore(vector2), Restore(v2_label), runtime=1.5)
        self.wait(1.5)

        #siirretää pistettä
        dot1_label.target = MathTex("(-3,-3,2)").next_to(v2_label, DOWN)
        dot1.target = Dot3D(axes.c2p(-3,-3,2))
        self.play(MoveToTarget(dot1))
        self.play(MoveToTarget(dot1_label))
        self.wait()
        self.play(Indicate(dot1), runtime=1.5)
        self.wait()
        self.play(Indicate(dot1), runtime=1.5)
        self.wait(1.5)

        #luodaa vektoreille uudet targetit ja  siirettää ne niihi
        vector1.generate_target()
        vector1.target = Vector(axes.c2p(-3, -3, 0), color=GREEN)
        v1_label.generate_target()
        v1_label.target = MathTex("-3\overline{v}_1=(-3, -3, 0)", color=GREEN).to_corner(UL)
        self.play(MoveToTarget(vector1),MoveToTarget(v1_label))
        self.wait()
        vector2.generate_target()
        vector2.target = Vector(axes.c2p(0, 0, 2), color=RED).shift(axes.c2p(-3, -3, 0))
        v2_label.generate_target()
        v2_label.target = MathTex("2 \overline{v}_2=(0, 0, 2)", color=RED).next_to(v1_label,DOWN)
        self.play(MoveToTarget(vector2),MoveToTarget(v2_label))
        self.wait(1)
        self.begin_ambient_camera_rotation(rate=0.55)
        self.wait(5.5)
        self.stop_ambient_camera_rotation()
        self.wait(3.5)


class VektoriYhteenlasku(Scene):
    def construct(self):
        grid = NumberPlane() 

        # alkusetit
        vector1 = Vector([3, 1, 0], color=BLUE)
        v1_label = MathTex("\overline{v}_1=(3,1)", color=BLUE).next_to(vector1, DOWN)
        vector2 = Vector([1, 2, 0], color=GREEN)
        v2_label = MathTex("\overline{v}_2=(1,2)", color=GREEN).next_to(vector2, UP)

        
        vector1.shift(grid.get_center())
        vector2.shift(grid.get_center())
        
        # piirrä vektorit
        self.add(grid)
        self.play(Create(vector1))
        self.wait(1)
        self.play(Write(v1_label))
        self.wait(1)
        self.play(Create(vector2))
        self.wait(1)
        self.play(Write(v2_label))
        self.wait(1)

        # vektori2 liikkuu
        end_point = grid.coords_to_point(4, 3)  
        self.play(vector2.animate.shift(end_point - vector2.get_end()), run_time=3)  
        
        # summavektori
        sum_vector = Vector([4, 3, 0], color=ORANGE)
        sum_label = MathTex("\overline{v}_1", "+", "\overline{v}_2", "=(4,3)", color=ORANGE).next_to(sum_vector, UP)
        
        self.play(Create(sum_vector), run_time=2.5)
        self.wait(1)
        self.play(Write(sum_label))
        self.wait(2.5)

        # vektori2 takas 
        end_point2 = grid.coords_to_point(1,2)
        self.play(vector2.animate.shift(end_point2 - vector2.get_end()), run_time=2)

        # vektori1 eestaas ja sumlabel muutos
        """sum_label.generate_target()"""
        sum_labelnew = MathTex("\overline{v}_2", "+", "\overline{v}_1", "=(4,3)", color=ORANGE).next_to(sum_vector, UP)
        end_point1 = grid.coords_to_point(3,1)
        self.play(vector1.animate.shift(end_point - vector1.get_end()), run_time=3)
        self.wait()
        self.play(TransformMatchingTex(sum_label,sum_labelnew), runtime=1.5)
        self.wait(2.5)
        self.play(vector1.animate.shift(end_point1 - vector1.get_end()), run_time=2)

        # poistetaa kaks vektorii
        self.play(FadeOut(vector2,sum_vector),Unwrite(sum_labelnew),FadeOut(v2_label))

        # siirretää vektorii
        vector1.save_state()
        vector1.generate_target()
        vector1.target = Vector([6, 2, 0], color=BLUE)
        self.play(MoveToTarget(vector1), run_time=2)

        # luodaa ja lisätää tulovektori
        product_label = MathTex("2\overline{v}_1=(6,2)",color=BLUE).next_to(vector1,UP)
        self.play(Write(product_label),FadeOut(v1_label),run_time=2)

        self.wait(2.5)

        self.play(Restore(vector1),FadeIn(vector2),Unwrite(product_label), runtime=1.5)
        self.play(Write(v2_label))
        self.wait()
        vector2.save_state()
        vector2.generate_target()
        v2_label.save_state()
        v2_label.generate_target()
        vector2.target = Vector([-1, -2, 0], color=GREEN)
        v2_label.target = MathTex("-\overline{v}_2=(-1,-2)", color=GREEN).next_to(vector2.target, DOWN)
        self.play(MoveToTarget(vector2),MoveToTarget(v2_label), run_time=2.5)
        end_point2 = grid.coords_to_point(3,1)
        self.play(vector1.animate.shift(vector2.target.get_end()), run_time=3)
        self.wait()
        sum_label2 = MathTex("-\overline{v}_2 + \overline{v}_1=(2,-1)",color=PURPLE).next_to(vector2.target,UP)
        sum_vector2 = Vector([2,-1,0],color=PURPLE)
        self.wait(2)
        self.play(FadeIn(sum_vector2), runtime=1.5)
        self.wait(1)
        self.play(Write(sum_label2))
        self.wait(2.5)


class VectorAddition(Scene):
    def construct(self):
        # Luo koordinaatisto
        axes = Axes(
            x_range=[-1, 7],
            y_range=[-3, 4],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=7,
            tips=False
        )

        # Luo vektorit alkamaan origosta
        v1 = Vector([3, 1], color=BLUE).shift(axes.c2p(0, 0))
        v2 = Vector([1, 2], color=GREEN).shift(axes.c2p(0, 0))

        # Luo vektori -v2 + v1
        neg_v2_plus_v1 = Vector([2, -1], color=PURPLE).shift(axes.c2p(0, 0))

        # Piirrä koordinaatisto ja vektorit
        self.play(Create(axes), Create(v1), Create(v2))

        # Odota hetki
        self.wait(2)

        # Lisää vektorien MathTex-merkinnät
        v1_label = MathTex("\\vec{v}_1", color=BLUE).next_to(v1, RIGHT)
        v2_label = MathTex("\\vec{v}_2", color=GREEN).next_to(v2, UP)
        neg_v2_plus_v1_label = MathTex("-\\vec{v}_2 + \\vec{v}_1", color=PURPLE).next_to(neg_v2_plus_v1, DOWN)

        # Laske vektorien summa
        sum_vector = Vector([4, 3], color=RED).shift(axes.c2p(0, 0))
        sum_label = MathTex("\\vec{v}_1 + \\vec{v}_2", color=RED).next_to(sum_vector, UP)
        self.play(Transform(v1.copy().shift(v2.get_end()), sum_vector), Write(sum_label), run_time=3)
        self.wait(1)

        # Siirrä v1 alkamaan v2 loppupisteestä
        self.play(Transform(v1, Vector([3, 1], color=BLUE).shift(v2.get_end())), run_time=3)
        self.wait(1)

        # Kertominen negatiivisella luvulla (muunna vektori v2 käänteisvektoriksi)
        v2_negative = Vector([-1, -2], color=GREEN).shift(axes.c2p(0, 0))
        v2_negative_label = MathTex("-\\vec{v}_2", color=GREEN).next_to(v2_negative, DOWN)
        self.play(Transform(v2, v2_negative), Write(v2_negative_label), run_time=3)
        self.wait(1)

        # Piirrä vektori -v2 + v1
        self.play(Transform(v2.copy().shift(v1.get_end()), neg_v2_plus_v1), Write(neg_v2_plus_v1_label), run_time=3)
        self.wait(1)

        # Näytä, että v1 + v2 on summan tulos
        self.play(Transform(sum_vector, neg_v2_plus_v1), Transform(sum_label, neg_v2_plus_v1_label), run_time=3)
        self.wait(2)

        # Poista tarpeettomat vektorit ja tekstit
        self.play(FadeOut(v1), FadeOut(v2), FadeOut(v1_label), FadeOut(v2_label), FadeOut(neg_v2_plus_v1), FadeOut(neg_v2_plus_v1_label), FadeOut(sum_vector), FadeOut(sum_label))