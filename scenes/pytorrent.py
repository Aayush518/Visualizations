from manim import *

class PyTorrentAnimation(Scene):
    def construct(self):
        self.show_title()
        self.show_initialization()
        self.show_connecting_to_tracker()
        self.show_peer_connection()
        self.show_downloading_pieces()
        self.show_seeding_and_upload()
        self.show_conclusion()

    def show_title(self):
        title = Text("Understanding PyTorrent", font_size=60, color=BLUE)
        subtitle = Text("A Detailed Explanation", font_size=40, color=BLUE_D)
        title.move_to(UP*1.5)
        subtitle.move_to(UP*0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

    def show_initialization(self):
        title = Text("Torrent Initialization", font_size=48, color=GREEN).to_edge(UP)
        explanation = """
        When starting PyTorrent, 
        the client loads a .torrent file 
        to gather metadata about the torrent.
        """
        text = Text(explanation, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text))

    def show_connecting_to_tracker(self):
        title = Text("Connecting to Tracker", font_size=48, color=GREEN).to_edge(UP)
        explanation = """
        The client connects to a tracker 
        to get a list of peers sharing 
        the same file (torrent).
        """
        text = Text(explanation, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        client = Circle(color=BLUE, radius=0.7)
        tracker = Circle(color=GREEN, radius=0.7)
        tracker.next_to(client, RIGHT*3)

        arrow = Arrow(client.get_right(), tracker.get_left(), buff=0.1, color=YELLOW)
        
        self.play(Write(title))
        self.play(Write(text))
        self.play(GrowArrow(arrow))
        self.play(Create(client), Create(tracker))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text), FadeOut(client), FadeOut(tracker), FadeOut(arrow))

    def show_peer_connection(self):
        title = Text("Peer Connection and Handshake", font_size=48, color=GREEN).to_edge(UP)
        explanation = """
        The client establishes connections 
        with multiple peers and performs 
        a handshake to exchange 
        capabilities and status.
        """
        text = Text(explanation, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        client = Circle(color=BLUE, radius=0.7)
        peers = [Circle(color=GREEN, radius=0.7) for _ in range(3)]
        for i, peer in enumerate(peers):
            peer.next_to(client, RIGHT*(i-1.5))

        arrows = [Arrow(client.get_right(), peer.get_left(), buff=0.1, color=YELLOW) for peer in peers]

        self.play(Write(title))
        self.play(Write(text))
        self.play(Create(client))
        self.play(*[Create(peer) for peer in peers])
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text), *[FadeOut(peer) for peer in peers], FadeOut(client), *[FadeOut(arrow) for arrow in arrows])

    def show_downloading_pieces(self):
        title = Text("Downloading Pieces", font_size=48, color=GREEN).to_edge(UP)
        explanation = """
        The client downloads pieces of 
        the file from connected peers 
        simultaneously to complete 
        the download faster.
        """
        text = Text(explanation, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        client = Circle(color=BLUE, radius=0.7)
        peers = [Circle(color=GREEN, radius=0.7) for _ in range(3)]
        for i, peer in enumerate(peers):
            peer.next_to(client, RIGHT*(i-1.5))

        pieces = [Square(color=ORANGE, side_length=1) for _ in range(3)]
        for i, piece in enumerate(pieces):
            piece.next_to(peers[i], DOWN*2)

        arrows = [Arrow(peer.get_bottom(), piece.get_top(), buff=0.1, color=YELLOW) for peer, piece in zip(peers, pieces)]

        self.play(Write(title))
        self.play(Write(text))
        self.play(Create(client))
        self.play(*[Create(peer) for peer in peers])
        self.play(*[Create(piece) for piece in pieces])
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text), *[FadeOut(piece) for piece in pieces], *[FadeOut(peer) for peer in peers], FadeOut(client), *[FadeOut(arrow) for arrow in arrows])

    def show_seeding_and_upload(self):
        title = Text("Seeding and Upload", font_size=48, color=GREEN).to_edge(UP)
        explanation = """
        After downloading the file, 
        the client can seed (upload) 
        parts of the file to other peers 
        who are downloading it.
        """
        text = Text(explanation, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        client = Circle(color=BLUE, radius=0.7)
        peers = [Circle(color=GREEN, radius=0.7) for _ in range(3)]
        for i, peer in enumerate(peers):
            peer.next_to(client, RIGHT*(i-1.5))

        pieces = [Square(color=ORANGE, side_length=1) for _ in range(3)]
        for i, piece in enumerate(pieces):
            piece.next_to(client, RIGHT*(i-1.5))

        arrows = [Arrow(client.get_right(), peer.get_left(), buff=0.1, color=YELLOW) for peer in peers]

        self.play(Write(title))
        self.play(Write(text))
        self.play(Create(client))
        self.play(*[Create(peer) for peer in peers])
        self.play(*[Create(piece) for piece in pieces])
        self.play(*[GrowArrow(arrow) for arrow in arrows])
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text), *[FadeOut(piece) for piece in pieces], *[FadeOut(peer) for peer in peers], FadeOut(client), *[FadeOut(arrow) for arrow in arrows])

    def show_conclusion(self):
        title = Text("Conclusion", font_size=48, color=GREEN).to_edge(UP)
        conclusion_text = """
        PyTorrent enables efficient 
        file sharing using the 
        BitTorrent protocol, 
        benefiting from 
        decentralized peer-to-peer 
        connections.
        """
        text = Text(conclusion_text, font_size=28, color=WHITE).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(text))
        self.wait(3)
        self.play(FadeOut(title), FadeOut(text))

# Main script
if __name__ == "__main__":
    module_name = PyTorrentAnimation.__name__
    scene_instance = PyTorrentAnimation()
    scene_instance.render()
