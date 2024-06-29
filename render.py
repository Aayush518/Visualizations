from manim import *
from scenes.campus_network_scene import CampusNetwork

def main():
    config.pixel_height = 900  # Adjust as needed
    config.pixel_width = 1600   # Adjust as needed
    config.frame_height = 9
    config.frame_width = 16

    scene = CampusNetwork()
    scene.render()

if __name__ == "__main__":
    main()
