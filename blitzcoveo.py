#!/usr/bin/env python

import sys
import json
import numpy as np

class letter:
    def __init__(name, orientation, position):
        self.name = name
        self.orientation = orientation
        self.position = position

vletterdict = {
    "[1 1 1 1 0 0 1 0 0 1 0 0 1 1 1]": ["C",0],
    "[1 1 1 0 0 1 0 0 1 0 0 1 1 1 1]": ["C",2],
    "[1 1 1 1 0 1 1 0 1 1 0 1 1 1 1]": ["O",0],
    "[1 0 1 1 0 1 1 0 1 1 0 1 0 1 0]": ["V",0],
    "[0 1 0 1 0 1 1 0 1 1 0 1 1 0 1]": ["V",2],
    "[1 1 1 1 0 0 1 1 1 1 0 0 1 1 1]": ["E",0],
    "[1 1 1 0 0 1 1 1 1 0 0 1 1 1 1]": ["E",2]
}

hletterdict = {
    "[1 0 0 0 1 1 0 0 0 1 1 1 1 1 1]": ["C",1],
    "[1 1 1 1 1 1 0 0 0 1 1 0 0 0 1]": ["C",3],
    "[1 1 1 1 1 1 0 0 0 1 1 1 1 1 1]": ["O",1],
    "[1 1 1 1 0 0 0 0 0 1 1 1 1 1 0]": ["V",1],
    "[0 1 1 1 1 1 0 0 0 0 0 1 1 1 1]": ["V",3],
    "[1 0 1 0 1 1 0 1 0 1 1 1 1 1 1]": ["E",1],
    "[1 1 1 1 1 1 0 1 0 1 1 0 1 0 1]": ["E",3]
}


def solvepuzzle(m):
    letters, noise = identifyletters(m)
    letters = validate(letters, noise)
    return letters

def identifyletters(m):
    h = m.shape[0]
    w = m.shape[1]
    letters = []
    
    for i in range(h-4):
        for j in range(w-4):
            l = hletterdict.get(str(m[i:i+4,j:j+2].flatten),False)
            if l:
                letters.append(letter(l[0],l[1],[i,j]))
                m[i:i+4,j:j+2]=np.zeros((3,5))
                continue
                
            l = vletterdict.get(str(m[i:i+2,j:j+4].flatten),False)
            if l:
                letters.append(letter(l[0],l[1],[i,j]))
                m[i:i+2,j:j+4]=np.zeros((5,3))
                continue
            
        for j in range(w-4, w-2):
            continue
    for i in range(h-4, h-2):
        for j in range(w-4):
            continue
    
    return [letters,[]]

def validate(letters, noise):
    return letters

if __name__ == '__main__' :

    puzzle = sys.argv[1]
    with open(puzzle, "r") as f:
        puzzle = json.load(f)
    teamName = "nom dequipe"
    teamStreetAdress = "817, 54e avenue, Lachine"

    solutions = [solvepuzzle(np.array([[x=="X" for x in l] for l in m], dtype='int')) for m in puzzle]
    print(solutions)

    #with open("team.json", "r") as f:
    #    team_data = json.load(f)

    output = {
        "teamName": teamName,
        "teamStreetAdress": teamStreetAdress,
    #    "participants": team_data["participants"]
    }

    print(json.dumps(output))
