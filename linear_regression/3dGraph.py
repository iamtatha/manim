from manim import *
import numpy as np

config.frame_width = 16
config.frame_height = 9
config.pixel_height = 1080
config.pixel_width = 1920

class Data3DPlot(ThreeDScene):
    def construct(self):
        # Define the data for the table
        data = [
            [25, 1, 30450], [30, 3, 35670], [47, 2, 31580],
            [32, 5, 40130], [43, 10, 47830], [51, 7, 41630],
            [28, 5, 41340], [33, 4, 37650], [37, 5, 40250],
            [39, 8, 45150], [29, 1, 27840], [47, 9, 46110],
            [54, 5, 36720], [51, 4, 34800], [44, 12, 51300],
            [41, 6, 38900], [58, 17, 63600], [23, 1, 30870],
            [44, 9, 44190], [37, 10, 48700]
        ]


        axes = ThreeDAxes(
            x_range=[0, 60],
            y_range=[0, 20],
            z_range=[250, 650],
            axis_config={"color": BLUE},
        ).scale(0.5).to_edge(DOWN)

        # Extract x, y, and z data
        x_vals = [point[0] for point in data]
        y_vals = [point[1] for point in data]
        z_vals = [point[2]/100 for point in data]


        points = [axes.c2p(x, y, z) for x, y, z in zip(x_vals, y_vals, z_vals)]
        dot_group = VGroup(*[Dot3D(point, color=RED) for point in points])

        self.set_camera_orientation(phi=2*PI/5, theta=PI/5)
        self.play(Create(axes))
        self.play(FadeIn(dot_group))

        self.wait(2)
