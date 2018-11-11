"""
MetaGame
An interactive video cd ~
game!

Authors: Cynthia Yong, Sabrina Pereira, Sophie Schaffer
"""
import pygame


class Room():
    """needs to accept name, picture, """
    def __init__(self, name = "room", picture = "picture"):
        self.name = name
        self.picture = picture
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

class Artifact():
    """needs to accept name, description, picture"""
    def __init__(self, location="location", name="name", description="description", picture="picture"):
        self.location = location
        self.name = name
        self.description = description
        self.picture = picture
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

Room1 = Room()
A1R1 = Artifact()
A2R1 = Artifact()
A3R1 = Artifact()

RoomScreens = { Room1 : [A1R1, A2R1, A3R1]
}

print(RoomScreens[Room1])
