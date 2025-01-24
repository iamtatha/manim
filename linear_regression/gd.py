from manim import *
from linearregression import lr

config.frame_width = 16
config.frame_height = 9
config.pixel_height = 1080
config.pixel_width = 1920


class LR1(Scene):
    def construct(self):
        lambdaa = MathTex(r"\lambda", color=BLUE).scale(3)
        psi = MathTex(r"\psi", color=GOLD).scale(3)
        lambdaa.to_edge(LEFT, buff=3)
        psi.to_edge(RIGHT, buff=3)

        self.play(Write(lambdaa), Write(psi))

        text = (
            Text(
                "Hey ψ, you know today at school we plotted \npoints on a graph paper for a straight line?",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )

        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))

        text = (
            Text(
                "Amazing λ! Show me.",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))

        self.play(lambdaa.animate.shift(LEFT * 2), psi.animate.shift(RIGHT * 2))

        
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 2],
            axis_config={"color": BLUE},
            tips=False
        ).add_coordinates().scale(0.6)

        x_label = MathTex("X\\text{-axis}").scale(0.6).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = MathTex("Y\\text{-axis}").scale(0.6).next_to(axes.y_axis, LEFT, buff=0.2)
        self.play(Create(axes), Write(x_label), Write(y_label))

        x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y_values = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        noisy_y_values = [2.8, 5.3, 6.5, 9.1, 10.8, 13.7, 15.2, 16.5, 18.7]



        points = [
            Dot(axes.coords_to_point(x, y), color=RED).scale(0.7) for x, y in zip(x_values, noisy_y_values)
        ]
        self.play(*[FadeIn(point) for point in points])

        self.wait(2)
        graph = VGroup(axes, x_label, y_label, *points)

        text = (
            Text(
                "Huh! Doesn't look \nlike a straight line.",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
            .shift(LEFT * 1)
        )
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))


        text = (
            Text(
                "Yeah I know! \nProbably I messed up.",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))


        self.play(FadeOut(graph))
        self.play(lambdaa.animate.shift(RIGHT * 2), psi.animate.shift(LEFT * 2))


        text = (
            Text(
                "Is there a way to get the line back again?",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))


        text = (
            Text(
                "Yeah! Linear Regression!",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )
        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text))



        self.play(FadeOut(lambdaa))



        data = [
            ["Age", "Experience", "Income"],
            [25, 1, 30450],
            [47, 2, 31580],
            [32, 5, 40130],
            [43, 10, 47830],
            [39, 8, 45150],
            [29, 1, 27840],
            [44, 12, 51300]
        ]
        data_str = [[str(item) for item in row] for row in data]

        table = Table(
            data_str,
            include_outer_lines=True
        ).scale(0.4).shift(LEFT * 3)

        table.move_to(ORIGIN)



        text = (
            Text(
                "Another such data example!",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
    
        )
        self.play(Write(text))
        self.play(Create(table))
        self.wait(2)
        self.play(FadeOut(text))


        text = (
            Text(
                "Let's see how the graph will look!",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
    
        )
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))


        self.play(FadeOut(table), FadeOut(psi))


class LR2(Scene):
    def construct(self):
        lambdaa = MathTex(r"\lambda", color=BLUE).scale(3)
        psi = MathTex(r"\psi", color=GOLD).scale(3)
        lambdaa.to_edge(LEFT, buff=3)
        psi.to_edge(RIGHT, buff=3)

        self.play(Write(lambdaa))

        text = (
            Text(
                "So basically the Income is \ndetermined by age and experience!",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )

        self.play(Write(text))
        self.wait(1.5)
        self.play(FadeOut(text)) 







        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 2],
            axis_config={"color": BLUE},
            tips=False
        ).add_coordinates().scale(0.6)

        x_label = MathTex("X\\text{-axis}").scale(0.6).next_to(axes.x_axis, DOWN, buff=0.2)
        y_label = MathTex("Y\\text{-axis}").scale(0.6).next_to(axes.y_axis, LEFT, buff=0.2)
        self.play(Create(axes), Write(x_label), Write(y_label), lambdaa.animate.shift(LEFT))

        x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y_values = [3, 5, 7, 9, 11, 13, 15, 17, 19]
        noisy_y_values = [2.8, 5.3, 6.5, 9.1, 10.8, 13.7, 15.2, 16.5, 18.7]
        

        text = (
            Text(
                "Let's try to find out \nthe straight line!",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(LEFT * 0.5)
        )

        self.play(Write(text))
        self.wait(1)


        points = [
            Dot(axes.coords_to_point(x, y), color=RED).scale(0.7) for x, y in zip(x_values, noisy_y_values)
        ]
        self.play(*[FadeIn(point) for point in points])

        self.wait(2)
        graph = VGroup(axes, x_label, y_label, *points)



        final_theta, costs, thetas = lr()

        theta = thetas[0]

        regression_line = axes.plot(
            lambda x: theta[1][0] * x + theta[0][0],
            color=YELLOW_E
        )

        self.play(Create(regression_line))


        self.play(FadeOut(text))
        text = (
            Text(
                "Well! Definitely \nnot that one.",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(lambdaa, UP, buff=0.5)
            .shift(LEFT * 0.5)
        )

        self.play(Write(text))
        self.wait(1)


        self.play(FadeIn(psi))
        self.play(FadeOut(text))
        text = (
            Text(
                "Compute the loss like this",
                font_size=24,
                line_spacing=0.8,
            )
            .next_to(psi, UP, buff=0.5)
            .shift(RIGHT * 0.5)
        )

        self.play(Write(text))
        self.wait(1)




        distance_lines = []
        for x, y in zip(x_values, noisy_y_values):
            y_on_line = theta[1][0] * x + theta[0][0]  # y value on the regression line
            line = Line(
                axes.coords_to_point(x, y),
                axes.coords_to_point(x, y_on_line),
                color=RED,
            )
            distance_lines.append(line)

        self.play(*[Create(line) for line in distance_lines])
        self.wait(2)