from manim import *
from scenes.campus_network_scene import CampusNetwork

# Render the scene
def render():
    config.pixel_height = 720  # Adjust as needed
    config.pixel_width = 1280  # Adjust as needed
    config.frame_rate = 30  # Adjust as needed
    config.quality = "medium_quality"  # Use one of the valid quality settings

    scene = CampusNetwork()
    scene.render()

if __name__ == "__main__":
    render()
