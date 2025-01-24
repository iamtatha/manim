from manim import *

class Regression1(Scene):
    def construct(self):
        # 1. White background
        self.camera.background_color = WHITE
        
        # 2. Draw a square in the middle
        square = Square(side_length=4, color=BLACK).move_to(ORIGIN)
        self.play(Create(square))

        # 3. Add 15 data points
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

        # Create and display dots
        dots = [Dot(point=eachpoint, color=BLACK) for eachpoint in all_points]
        for dot in dots:
            self.play(FadeIn(dot), run_time=0.1)
        
        # 4. Fit a regression line (dummy linear regression line approximation)
        regression_line = Line(
            start=LEFT * 2 + DOWN * 0.5,
            end=RIGHT * 2 + UP * 0.5,
            color=GREEN
        )
        self.play(Create(regression_line))

        regression_line2 = Line(
            start=LEFT * 2 + DOWN * 1,
            end=RIGHT * 2 + UP * 2,
            color=BLUE
        )
        self.play(Create(regression_line2))

        regression_line3 = Line(
            start=LEFT * 2 + DOWN * 1.5,
            end=RIGHT * 2 + UP * 1.5,
            color=RED
        )
        self.play(Create(regression_line3))


        # 5. Add text to the top-right corner
        top_right_text = Text(
            "So which one is more accurate?",
            font_size=24,
            color=BLACK
        ).to_corner(UR)  # Position text to the Upper-Right (UR) corner
        self.play(Write(top_right_text))

        # 5. Move the whole square with contents to the bottom left
        # group = VGroup(square, *dots, regression_line, regression_line2, regression_line3)
        # self.play(group.animate.shift(LEFT * 4 + DOWN * 1.8))
        
        # Hold the final scene
        self.wait(2)



class Regression2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        text = Text("Well, the accuracy is measured through the cost!", font_size=48, color=BLACK)
        self.play(Write(text))  # Directly adds the text to the scene
        self.wait(2)

        self.remove(text)

        text = Text("Let's take the previous example again.", font_size=48, color=BLACK)
        self.play(Write(text))  # Directly adds the text to the scene
        self.wait(2)

        self.remove(text)

        square = Square(side_length=4, color=BLACK).move_to(ORIGIN)
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

        dots = [Dot(point=eachpoint, color=BLACK) for eachpoint in all_points]
        for dot in dots:
            self.add(dot)
        

        regression_line = Line(
            start=LEFT * 2 + DOWN * 0.5,
            end=RIGHT * 2 + UP * 0.5,
            color=GREEN
        )
        self.play(Create(regression_line))

        # regression_line2 = Line(
        #     start=LEFT * 2 + DOWN * 1,
        #     end=RIGHT * 2 + UP * 2,
        #     color=BLUE
        # )
        # self.play(Create(regression_line2))

        # regression_line3 = Line(
        #     start=LEFT * 2 + DOWN * 1.5,
        #     end=RIGHT * 2 + UP * 1.5,
        #     color=RED
        # )
        # self.play(Create(regression_line3))



        # # 5. Move the whole square with contents to the bottom left
        # # group = VGroup(square, *dots, regression_line, regression_line2, regression_line3)
        # # self.play(group.animate.shift(LEFT * 4 + DOWN * 1.8))


        perpendiculars = []
        for point in all_points:
            # Project the point onto the line
            projection = self.get_projection_point(point, regression_line)
            # Draw the perpendicular line
            perp_line = DashedLine(start=point, end=projection, color=GREEN)
            perpendiculars.append(perp_line)
            self.play(Create(perp_line), run_time=0.5)

        self.wait(2)


    def get_projection_point(self, point, line):
        line_start = line.get_start()[:2]  # Line start (2D vector)
        line_end = line.get_end()[:2]  # Line end (2D vector)
        line_vec = line_end - line_start  # Line direction vector
        point_vec = point[:2] - line_start  # Vector from line start to the point
        line_unit_vec = line_vec / np.linalg.norm(line_vec)  # Normalize the line vector
        projection_length = np.dot(point_vec, line_unit_vec)  # Scalar projection
        projection = line_start + projection_length * line_unit_vec  # Projection point
        return np.array([projection[0], projection[1], 0])  # Return as a 3D vector


class Regression3(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        text = Text("But still.. Which one was the best line?", font_size=48, color=BLACK)
        self.play(Write(text))
        self.wait(2)

        self.remove(text)

        square = Square(side_length=4, color=BLACK).move_to(ORIGIN)
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

        dots = [Dot(point=eachpoint, color=BLACK) for eachpoint in all_points]
        for dot in dots:
            self.add(dot)
        

        regression_line = Line(
            start=LEFT * 2 + DOWN * 0.5,
            end=RIGHT * 2 + UP * 0.5,
            color=GREEN
        )
        self.play(Create(regression_line))

        perpendiculars1 = []
        for point in all_points:
            projection = self.get_projection_point(point, regression_line)
            perp_line = DashedLine(start=point, end=projection, color=GREEN)
            perpendiculars1.append(perp_line)
            self.add(perp_line)
        
        group = VGroup(square, *dots, regression_line, *perpendiculars1)
        self.play(group.animate.shift(LEFT * 4 + DOWN * 2.1).scale(0.5))





        square = Square(side_length=4, color=BLACK).move_to(ORIGIN)
        self.add(square)

        dots = [Dot(point=eachpoint, color=BLACK) for eachpoint in all_points]
        for dot in dots:
            self.add(dot)

        regression_line2 = Line(
            start=LEFT * 2 + DOWN * 1,
            end=RIGHT * 2 + UP * 2,
            color=BLUE
        )
        self.play(Create(regression_line2))

        perpendiculars2 = []
        for point in all_points:
            projection = self.get_projection_point(point, regression_line2)
            perp_line = DashedLine(start=point, end=projection, color=BLUE)
            perpendiculars2.append(perp_line)
            self.add(perp_line)
        
        group = VGroup(square, *dots, regression_line2, *perpendiculars2)
        self.play(group.animate.shift(RIGHT * 4 + DOWN * 2.1).scale(0.5))





        square = Square(side_length=4, color=BLACK).move_to(ORIGIN)
        self.add(square)

        dots = [Dot(point=eachpoint, color=BLACK) for eachpoint in all_points]
        for dot in dots:
            self.add(dot)


        regression_line3 = Line(
            start=LEFT * 2 + DOWN * 1.5,
            end=RIGHT * 2 + UP * 1.5,
            color=RED
        )
        self.play(Create(regression_line3))

        perpendiculars3 = []
        for point in all_points:
            projection = self.get_projection_point(point, regression_line3)
            perp_line = DashedLine(start=point, end=projection, color=RED)
            perpendiculars3.append(perp_line)
            self.add(perp_line)
        
        group = VGroup(square, *dots, regression_line3, *perpendiculars3)
        self.play(group.animate.shift(DOWN * 2.1).scale(0.5))





        text = Text("Can we calculate that using the perpendiculars?", font_size=48, color=BLACK)
        self.play(Write(text))
        self.wait(2)

        self.wait(2)


    def get_projection_point(self, point, line):
        line_start = line.get_start()[:2]  # Line start (2D vector)
        line_end = line.get_end()[:2]  # Line end (2D vector)
        line_vec = line_end - line_start  # Line direction vector
        point_vec = point[:2] - line_start  # Vector from line start to the point
        line_unit_vec = line_vec / np.linalg.norm(line_vec)  # Normalize the line vector
        projection_length = np.dot(point_vec, line_unit_vec)  # Scalar projection
        projection = line_start + projection_length * line_unit_vec  # Projection point
        return np.array([projection[0], projection[1], 0])  # Return as a 3D vector