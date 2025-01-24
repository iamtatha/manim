from manim import *

class IotaPhiTalking(Scene):
    def construct(self):
        # Create symbols for iota and phi
        iota = MathTex(r"\lambda", color=BLUE).scale(3) 
        phi = MathTex(r"\psi", color=GOLD).scale(3) 
        iota.to_edge(LEFT, buff=1)
        phi.to_edge(RIGHT, buff=1)


        iota_bubble = SVGMobject("speech_bubble.svg").scale(1.5).next_to(iota, UP, buff=0.5)
        phi_bubble = SVGMobject("speech_bubble.svg").scale(1.5).flip().next_to(phi, UP, buff=0.5)


        iota_text = Text("Hello, φ! How are you?", font_size=24).move_to(iota_bubble.get_center())
        phi_text = Text("Hi, ι! I'm great, thank you!", font_size=24).move_to(phi_bubble.get_center())


        self.play(Write(iota), Write(phi))
        self.wait(1)


        # Iota speaks
        self.play(FadeIn(iota_bubble), Write(iota_text))
        self.wait(2)
        self.play(FadeOut(iota_bubble), FadeOut(iota_text))

        # Phi speaks
        self.play(FadeIn(phi_bubble), Write(phi_text))
        self.wait(2)
        self.play(FadeOut(phi_bubble), FadeOut(phi_text))

        # Add closing animation
        closing_text = Text("They are learning Manim too!", font_size=36).move_to(DOWN)
        self.play(Write(closing_text))
        self.wait(2)
