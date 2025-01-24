from manim import *
import math

config.frame_width = 9
config.frame_height = 16
config.pixel_height = 1920
config.pixel_width = 1080 

class mse(Scene):
    def construct(self):
        self.camera.background_color = BLACK

        text = Text("What is Root Mean Squared Error?", font_size=44, color=WHITE)
        self.play(Write(text))
        self.wait(1)
        self.remove(text)

        text1 = Text("Let's take some points", font_size=40, color=WHITE)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(text1.animate.shift(UP * 6).scale(0.65))
        self.remove(text1)
        text2 = Text("And fit a line through them", font_size=40, color=WHITE)
        self.play(Write(text2))
        self.wait(0.5)
        self.play(text2.animate.shift(UP * 5).scale(0.65))
        self.remove(text2)




        square = Square(side_length=4, color=WHITE).move_to(ORIGIN)
        self.add(square)

        normal_points = [
            np.array([x, y, 0]) for x, y in [
                (-1.5, -1.2), (-1.0, -0.8), (-0.5, -0.2), (0, 0),
                (0.5, 0.2), (1.0, 0.8), (1.5, 1.2), (-1.0, 0.5),
                (1.0, -0.6), (0.2, 0.3), (-0.6, -0.1), (0.8, 0.5)
            ]
        ]
        outlier_points = [
            np.array([1.8, 1.5, 0]), np.array([1.5, -1.8, 0]), np.array([-1.8, 1.8, 0])
        ]
        all_points = normal_points + outlier_points

        dots = [Dot(point=eachpoint, color=WHITE) for eachpoint in all_points]
        for dot in dots:
            self.play(FadeIn(dot), run_time=0.1)
        

        regression_line = Line(
            start=LEFT * 2 + DOWN * 0.5,
            end=RIGHT * 2 + UP * 0.5,
            color=YELLOW_E
        )
        self.play(Create(regression_line))

        text3 = Text("Drawing the distances from the\n actual points to predicted line.", font_size=30, color=WHITE).to_edge(UP)
        self.play(Write(text3))
        self.wait(1)
        self.remove(text3)

        perpendiculars = []
        for point in all_points:
            projection = self.get_projection_point(point, regression_line)
            perp_line = Line(start=point, end=projection, color=RED_E)
            perpendiculars.append(perp_line)
            self.play(Create(perp_line), run_time=0.1)

        
        equation = MathTex(r"\text{distance} = (y_i - y'_i)", font_size=48).to_edge(DOWN).shift(UP * 1)
        explanation = Text("y is actual point and y' is predicted point on the line", font_size=24)
        explanation.next_to(equation, DOWN, buff=0.2)
        self.play(Write(equation))
        self.play(Write(explanation))
        self.wait(1)
        self.remove(equation)
        self.remove(explanation)


        mse_tot = 0
        count = 0
        for point in all_points:
            projection = self.get_projection_point(point, regression_line)
            projection_start = projection[0]
            projection_end = projection[1]
            
            squared_error = np.linalg.norm(projection_start - projection_end)**2
            
            mse_tot += squared_error
            count += 1

        rmse = math.sqrt(mse_tot/count)
        
        
        
        group = VGroup(square, *dots, regression_line, *perpendiculars)
        group2 = VGroup(square, *dots, regression_line)
        self.play(group2.animate.shift(UP * 6).scale(0.6))



        text = Text("Distances can be positive and negative both", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text))
        self.wait(1.5)
        self.remove(text)

        text = Text("Hence, take the square of the distances", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text))
        self.wait(1.5)
        self.remove(text)



        perpendicular_group = VGroup(*perpendiculars)
        scale_factors = [line.get_length() ** 1.2 for line in perpendicular_group]
        self.play(
            *[line.animate.scale(scale_factor) for line, scale_factor in zip(perpendicular_group, scale_factors)], run_time=0.5
        )


        equation = MathTex(r"\text{distance squared} = (y_i - y'_i)^2", font_size=48).to_edge(DOWN).shift(UP * 1)
        explanation.next_to(equation, DOWN, buff=0.2)
        self.play(Write(equation))
        self.wait(2)
        self.remove(equation)




        text = Text("Adding up the squared distances", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text))
        self.wait(1.5)
        self.remove(text)



        center_x = 0
        shifts = [center_x - line.get_center()[0] for line in perpendicular_group]

        # Animate all lines moving horizontally to the center
        self.play(
            *[line.animate.shift(RIGHT * shift) for line, shift in zip(perpendicular_group, shifts)], run_time=0.5
        )



        merged_line = Line(ORIGIN + UP * 3.5, ORIGIN + DOWN * 3.5, color=RED)
        merged_line.move_to(ORIGIN)
        self.play(
            FadeOut(perpendicular_group),  # Fade out the individual lines
            Create(merged_line)  # Create the wide line
        )




        
        equation = MathTex(r"\text{Total distance squared} = \sum_{i=1}^{n} (y_i - y'_i)^2", font_size=48).to_edge(DOWN).shift(UP * 1)
        explanation.next_to(equation, DOWN, buff=0.2)
        self.play(Write(equation))
        self.wait(2)
        self.remove(equation)




        text = Text("Since it is sum of all the squared distances", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text))
        self.wait(1.5)
        self.remove(text)


        text = Text("Let's take the mean", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text), run_time=0.7)
        self.wait(1.5)
        self.remove(text)




        self.play(merged_line.animate.scale(0.8), run_time=0.8)

        equation = MathTex(r"\text{Mean Squared Error} = \frac{1}{n} \sum_{i=1}^{n} (y_i - y'_i)^2", font_size=48).to_edge(DOWN).shift(UP * 1)
        explanation.next_to(equation, DOWN, buff=0.2)
        self.play(Write(equation))
        self.wait(2)
        self.remove(equation)




        text = Text("At last, we will take the square root", font_size=30).to_edge(DOWN).shift(UP * 1)
        self.play(Write(text))
        self.wait(1.5)
        self.remove(text)


        self.play(merged_line.animate.scale(0.8), run_time=0.5)

        rmse_formula = MathTex(
            r"\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}",
            font_size=48
        ).to_edge(DOWN).shift(UP * 1)
        self.play(Write(rmse_formula))
        self.wait(1.5)

        self.remove(group)
        self.remove(group2)
        self.remove(merged_line)
        self.play(rmse_formula.animate.shift(UP * 5.5))

        self.wait(1)


        self.remove(rmse_formula)

        text = Text("Created By:", font_size=25).to_edge(DOWN).shift(UP * 7.5)
        self.play(Write(text))

        text2 = Text("Tathagata Dey", font_size=35).to_edge(DOWN).shift(UP * 6.5)
        text2.next_to(text, DOWN, buff=0.2)

        self.play(Write(text2))
        self.wait(1.5)




    def get_projection_point(self, point, line):
        line_start = line.get_start()[:2]  # Line start (2D vector)
        line_end = line.get_end()[:2]  # Line end (2D vector)
        
        # Find the slope of the line
        if line_end[0] != line_start[0]:  # Avoid division by zero
            slope = (line_end[1] - line_start[1]) / (line_end[0] - line_start[0])
            intercept = line_start[1] - slope * line_start[0]
            
            # Projection point with the same x value as the original point
            projection_x = point[0]
            projection_y = slope * projection_x + intercept  # Using the line equation y = mx + b
            
            # Return the projection point as a 3D vector
            return np.array([projection_x, projection_y, 0])
        else:
            # If the line is vertical, the projection point has the same x but the line's y-coordinate
            projection_x = point[0]
            projection_y = line_start[1]  # Line is vertical, so use the y of the line
            
            # Return the projection point as a 3D vector
            return np.array([projection_x, projection_y, 0])


    