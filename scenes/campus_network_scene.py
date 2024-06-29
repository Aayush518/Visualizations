from manim import *

class CampusNetwork(Scene):
    def construct(self):
        # Define colors
        BLUE = "#0080FF"
        GREEN = "#00FF00"
        RED = "#FF0000"
        YELLOW = "#FFFF00"
        GRAY = "#808080"
        ORANGE = "#FFA500"
        PURPLE = "#800080"

        # Create campus map function
        def create_building(width, height, color, label):
            building = VGroup(
                Rectangle(width=width, height=height, fill_color=color, fill_opacity=0.5, stroke_color=WHITE),
                Text(label, font_size=10).move_to(Rectangle(width=width, height=height).get_center())
            )
            return building

        # Function to create network components
        def create_network_components():
            # Create buildings
            ric = create_building(1.2, 1, RED, "RIC")
            cit = create_building(1, 0.8, YELLOW, "CIT")
            library = create_building(0.8, 0.6, BLUE, "Library")
            admin = create_building(0.8, 0.6, GRAY, "Admin")
            civil = create_building(0.8, 0.6, GREEN, "Civil")
            mech = create_building(0.8, 0.6, ORANGE, "Mech")
            hostel = create_building(1, 0.6, PURPLE, "Hostel")

            # Arrange buildings
            buildings = VGroup(ric, cit, library, admin, civil, mech, hostel)
            buildings.arrange_in_grid(rows=3, cols=3, buff=1)
            buildings.move_to(ORIGIN)

            # Create routers and connections
            routers = VGroup(*[Dot(color=RED, radius=0.03) for _ in range(7)])
            for router, building in zip(routers, buildings):
                router.move_to(building.get_top() + UP * 0.1)

            connections = VGroup()
            for i in range(len(routers) - 1):
                connections.add(Line(routers[i], routers[i+1], stroke_width=1, color=YELLOW))

            return buildings, routers, connections

        # Function to animate campus overview
        def animate_campus_overview():
            buildings, routers, connections = create_network_components()
            self.play(Create(buildings))
            self.wait(1)
            self.play(Create(routers), Create(connections))
            self.wait(1)

        # Function to zoom into RIC building
        def zoom_to_ric_building():
            buildings, routers, connections = create_network_components()
            self.play(FadeOut(buildings), FadeOut(routers), FadeOut(connections))
            self.wait(1)

            ric = create_building(1.2, 1, RED, "RIC")
            self.play(Create(ric))
            self.wait(1)

            # Define floors and components inside RIC
            ric_floors = VGroup(
                Rectangle(width=4, height=0.2, fill_color=GRAY, fill_opacity=0.5),    # Underground
                Rectangle(width=4, height=0.5, fill_color=BLUE, fill_opacity=0.5),    # 1st floor
                Rectangle(width=4, height=0.5, fill_color=GREEN, fill_opacity=0.5),   # 2nd floor
                Rectangle(width=4, height=0.5, fill_color=RED, fill_opacity=0.5)      # 3rd floor
            ).arrange(DOWN, buff=0.2).move_to(ric.get_center())

            floor_labels = VGroup(
                Text("Underground", font_size=14),
                Text("1st Floor (Electrical)", font_size=14),
                Text("2nd Floor (Computer)", font_size=14),
                Text("3rd Floor (Electronics)", font_size=14)
            ).arrange(DOWN, buff=0.2).next_to(ric, RIGHT, buff=0.5)

            # Animation for RIC building details
            self.play(Create(ric_floors), Write(floor_labels))
            self.wait(2)

        # Run animations
        animate_campus_overview()
        zoom_to_ric_building()
        self.wait(1)
