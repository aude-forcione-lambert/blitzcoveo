#!/usr/bin/env python

import sys
import json
import numpy as np

C0 = np.array([[1,1,1],
               [1,0,0],
               [1,0,0],
               [1,0,0],
               [1,1,1]])
C90 = np.rot90(C0)
C180 = np.rot90(C90)
C270 = np.rot90(C180)

E0 = np.array([[1,1,1],
               [1,0,0],
               [1,1,1],
               [1,0,0],
               [1,1,1]])
E90 = np.rot90(E0)
E180 = np.rot90(E90)
E270 = np.rot90(E180)

O0 = np.array([[1,1,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [1,1,1]])
O90 = np.rot90(O0)
O180 = np.rot90(O90)
O270 = np.rot90(O180)

V0 = np.array([[1,0,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [0,1,0]])
V90 = np.rot90(V0)
V180 = np.rot90(V90)
V270 = np.rot90(V180)

LETTRES = {C0,C90,C180,C270,E0,E90,E180,E270,O0,O90,O180,O270,V0,V90,V180,V270}

puzzle = sys.argv[1]
teamName = "nom dequipe"
teamStreetAdress = "adresse"
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

