from manim import *

class CampusNetwork(Scene):
    def construct(self):
        # Define colors (replace with your desired color codes)
        BLUE = "#0080FF"
        GREEN = "#00FF00"
        RED = "#FF0000"
        YELLOW = "#FFFF00"
        CYAN = "#00FFFF"
        PURPLE = "#800080"
        ORANGE = "#FFA500"
        PINK = "#FFC0CB"
        TEAL = "#008080"
        GRAY = "#808080"
        BROWN = "#A52A2A"

        # Define buildings and components
        gate = Circle(color=WHITE, radius=0.5)
        wrc_administration = Rectangle(width=2, height=1, color=BLUE)
        ric_building = Rectangle(width=4, height=3, color=RED)
        cit_hall = Rectangle(width=3, height=2, color=GREEN)
        library = Square(side_length=2, color=YELLOW)
        geomatics = Square(side_length=2, color=CYAN)
        applied_science = Square(side_length=2, color=PURPLE)
        civil_engineering = Square(side_length=2, color=ORANGE)
        mechanical_engineering = Square(side_length=2, color=PINK)
        boys_hostel = Rectangle(width=3, height=2, color=TEAL)
        girls_hostel = Rectangle(width=3, height=2, color=GRAY)
        teachers_cottage = Rectangle(width=2, height=1, color=BROWN)

        # Positioning buildings
        gate.move_to(LEFT * 5)
        wrc_administration.next_to(gate, RIGHT, buff=1)
        ric_building.next_to(wrc_administration, RIGHT, buff=1)
        cit_hall.next_to(ric_building, RIGHT, buff=1)
        library.next_to(cit_hall, RIGHT, buff=1)
        geomatics.next_to(library, RIGHT, buff=1)
        applied_science.next_to(geomatics, RIGHT, buff=1)
        civil_engineering.next_to(applied_science, RIGHT, buff=1)
        mechanical_engineering.next_to(civil_engineering, RIGHT, buff=1)
        boys_hostel.next_to(mechanical_engineering, RIGHT, buff=1)
        girls_hostel.next_to(boys_hostel, RIGHT, buff=1)
        teachers_cottage.next_to(girls_hostel, RIGHT, buff=1)

        # Create lines for connections (simplified)
        connections = VGroup(
            Line(gate.get_right(), wrc_administration.get_left()),
            Line(wrc_administration.get_right(), ric_building.get_left()),
            Line(ric_building.get_right(), cit_hall.get_left()),
            Line(cit_hall.get_right(), library.get_left()),
            Line(library.get_right(), geomatics.get_left()),
            Line(geomatics.get_right(), applied_science.get_left()),
            Line(applied_science.get_right(), civil_engineering.get_left()),
            Line(civil_engineering.get_right(), mechanical_engineering.get_left()),
            Line(mechanical_engineering.get_right(), boys_hostel.get_left()),
            Line(boys_hostel.get_right(), girls_hostel.get_left()),
            Line(girls_hostel.get_right(), teachers_cottage.get_left())
        )

        # Labels for buildings
        labels = VGroup(
            Text("Gate", font_size=14).next_to(gate, DOWN),
            Text("WRC Admin", font_size=14).next_to(wrc_administration, DOWN),
            Text("RIC Building", font_size=14).next_to(ric_building, DOWN),
            Text("CIT Hall", font_size=14).next_to(cit_hall, DOWN),
            Text("Library", font_size=14).next_to(library, DOWN),
            Text("Geomatics", font_size=14).next_to(geomatics, DOWN),
            Text("Applied Science", font_size=14).next_to(applied_science, DOWN),
            Text("Civil Engg", font_size=14).next_to(civil_engineering, DOWN),
            Text("Mech. Engg", font_size=14).next_to(mechanical_engineering, DOWN),
            Text("Boys' Hostel", font_size=14).next_to(boys_hostel, DOWN),
            Text("Girls' Hostel", font_size=14).next_to(girls_hostel, DOWN),
            Text("Teachers' Cottage", font_size=14).next_to(teachers_cottage, DOWN)
        )

        # Traffic packet (example)
        packet = Dot(color=RED).move_to(gate.get_center())

        # Animation sequence
        self.play(Create(gate))
        self.play(Create(wrc_administration))
        self.play(Create(ric_building))
        self.play(Create(cit_hall))
        self.play(Create(library))
        self.play(Create(geomatics))
        self.play(Create(applied_science))
        self.play(Create(civil_engineering))
        self.play(Create(mechanical_engineering))
        self.play(Create(boys_hostel))
        self.play(Create(girls_hostel))
        self.play(Create(teachers_cottage))
        self.play(*[Create(connection) for connection in connections])
        self.play(*[Write(label) for label in labels])

        # Zoom in on RIC building
        self.wait(1)
        self.camera.frame_center.move_to(ric_building.get_center()).scale(0.5)
        self.wait(2)

        # Further animations or actions
        self.wait()
