#!/usr/bin/env python

import sys
import json
import numpy as np

class letter:
    def __init__(name, orientation, position):
        self.name = name
        self.orientation = orientation
        self.position = position

C0 = {"name" = "C",
      "orientation" = 0,
      "pattern" =
      np.array([[1,1,1],
               [1,0,0],
               [1,0,0],
               [1,0,0],
               [1,1,1]])}
C90 = {"name" = "C",
      "orientation" = 1,
      "pattern" = np.rot90(C0)}
C180 = {"name" = "C",
      "orientation" = 2,
      "pattern" = np.rot90(C90)}
C270 = {"name" = "C",
      "orientation" = 3,
      "pattern" = np.rot90(C180)}

E0 = {"name" = "E",
      "orientation" = 0,
      "pattern" =
      np.array([[1,1,1],
               [1,0,0],
               [1,1,1],
               [1,0,0],
               [1,1,1]])}
E90 = {"name" = "E",
      "orientation" = 1,
      "pattern" = np.rot90(E0)}
E180 = {"name" = "E",
      "orientation" = 2,
      "pattern" = np.rot90(E90)}
E270 = {"name" = "E",
      "orientation" = 3,
      "pattern" = np.rot90(E180)}

O0 = {"name" = "O",
      "orientation" = 0,
      "pattern" =
      np.array([[1,1,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [1,1,1]])}
O90 = {"name" = "O",
      "orientation" = 1,
      "pattern" = np.rot90(O0)}
O180 = {"name" = "O",
      "orientation" = 2,
      "pattern" = np.rot90(O90)}
O270 = {"name" = "O",
      "orientation" = 3,
      "pattern" = np.rot90(O180)}

V0 = {"name" = "V",
      "orientation" = 0,
      "pattern" =
      np.array([[1,0,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [0,1,0]])}
V90 = {"name" = "V",
      "orientation" = 1,
      "pattern" = np.rot90(V0)}
V180 = {"name" = "V",
      "orientation" = 2,
      "pattern" = np.rot90(V90)}
V270 = {"name" = "V",
      "orientation" = 3,
      "pattern" = np.rot90(V180)}

LETTERS = {C0,C90,C180,C270,E0,E90,E180,E270,O0,O90,O180,O270,V0,V90,V180,V270}

puzzle = sys.argv[1]
teamName = "nom dequipe"
teamStreetAdress = "817, 54e avenue, Lachine"
solutions = [solvepuzzle(m) for m in puzzle]

with open("team.json", "r") as f:
    team_data = json.load(f)

output = {
    "teamName": teamName,
    "teamStreetAdress": teamStreetAdress,
    "participants": team_data["participants"]
}

print(json.dumps(output))

def solvepuzzle(m):
    letters = identifyletters(m)
    noise = findnoise(m, letters)
    letters = validate(letters, noise)
    return letters

