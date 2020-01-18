#!/usr/bin/env python

import sys
import json
import numpy as np

class letter:
    def __init__(self, name, orientation, x, y):
        self.name = name
        self.orientation = orientation
        self.x = x
        self.y = y

C0 = np.array([[1,1,1],
               [1,0,0],
               [1,0,0],
               [1,0,0],
               [1,1,1]])

C1 = np.array([[1,0,0,0,1],
               [1,0,0,0,1],
               [1,1,1,1,1]])

C2 = np.array([[1,1,1],
               [0,0,1],
               [0,0,1],
               [0,0,1],
               [1,1,1]])

C3 = np.array([[1,1,1,1,1],
               [1,0,0,0,1],
               [1,0,0,0,1]])

E0 = np.array([[1,1,1],
               [1,0,0],
               [1,1,1],
               [1,0,0],
               [1,1,1]])

E1 = np.array([[1,0,1,0,1],
               [1,0,1,0,1],
               [1,1,1,1,1]])

E2 = np.array([[1,1,1],
               [0,0,1],
               [1,1,1],
               [0,0,1],
               [1,1,1]])

E3 = np.array([[1,1,1,1,1],
               [1,0,1,0,1],
               [1,0,1,0,1]])

O0 = np.array([[1,1,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [1,1,1]])

O1 = np.array([[1,1,1,1,1],
               [1,0,0,0,1],
               [1,1,1,1,1]])

V0 = np.array([[1,0,1],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [0,1,0]])

V1 = np.array([[1,1,1,1,0],
               [0,0,0,0,1],
               [1,1,1,1,0]])

V2 = np.array([[0,1,0],
               [1,0,1],
               [1,0,1],
               [1,0,1],
               [1,0,1]])

V3 = np.array([[0,1,1,1,1],
               [1,0,0,0,0],
               [0,1,1,1,1]])

letterdict = {"C": [np.transpose(np.nonzero(C0)),np.transpose(np.nonzero(C1)),np.transpose(np.nonzero(C2)),np.transpose(np.nonzero(C3))],
              "E": [np.transpose(np.nonzero(E0)),np.transpose(np.nonzero(E1)),np.transpose(np.nonzero(E2)),np.transpose(np.nonzero(E3))],
              "O": [np.transpose(np.nonzero(O0)),np.transpose(np.nonzero(O1))],
              "V": [np.transpose(np.nonzero(V0)),np.transpose(np.nonzero(V1)),np.transpose(np.nonzero(V2)),np.transpose(np.nonzero(V3))]}


def vletterdetect(m,x,y):
    if np.array_equal(m,C0):
        return letter("C",0,x,y)
    if np.array_equal(m,C2):
        return letter("C",2,x,y)
    if np.array_equal(m,E0):
        return letter("E",0,x,y)
    if np.array_equal(m,E2):
        return letter("E",2,x,y)
    if np.array_equal(m,O0):
        return letter("O",0,x,y)
    if np.array_equal(m,V0):
        return letter("V",0,x,y)
    if np.array_equal(m,V2):
        return letter("V",2,x,y)
    return False

def hletterdetect(m,x,y):
    if np.array_equal(m,C1):
        return letter("C",1,x,y)
    if np.array_equal(m,C3):
        return letter("C",3,x,y)
    if np.array_equal(m,E1):
        return letter("E",1,x,y)
    if np.array_equal(m,E3):
        return letter("E",3,x,y)
    if np.array_equal(m,O1):
        return letter("O",1,x,y)
    if np.array_equal(m,V1):
        return letter("V",1,x,y)
    if np.array_equal(m,V3):
        return letter("V",3,x,y)
    return False

def solvepuzzle(m):
    lettersarray, noise = identifyletters(m)
    lettersarray = validate(lettersarray, noise)
    return "".join([l.name for l in lettersarray])

def identifyletters(m):
    h = m.shape[0]
    w = m.shape[1]
    lettersarray = []
    
    for i in range(h-4):
        for j in range(w-4):
            l = hletterdetect(m[i:i+3,j:j+5],j,i)
            if l:
                lettersarray.append(l)
                m[i:i+3,j:j+5]=np.zeros((3,5))
                continue
                
            l = vletterdetect(m[i:i+5,j:j+3],j,i)
            if l:
                lettersarray.append(l)
                m[i:i+5,j:j+3]=np.zeros((5,3))
                continue
            
        for j in range(w-4, w-2):
            l = vletterdetect(m[i:i+5,j:j+3],j,i)
            if l:
                lettersarray.append(l)
                m[i:i+5,j:j+3]=np.zeros((5,3))
                continue

    for i in range(h-4, h-2):
        for j in range(w-4):
            l = hletterdetect(m[i:i+3,j:j+5],j,i)
            if l:
                lettersarray.append(l)
                m[i:i+3,j:j+5]=np.zeros((3,5))
                continue
    
    return [lettersarray,np.transpose(np.nonzero(m))]

def validate(lettersarray, noise):
    while True:
        invalid = []
        for i in range(len(lettersarray)):
            for n in noise:
                if isadjacent(lettersarray[i],n):
                    invalid.append(i)
                    noise = np.append(noise, [lettersarray[i].y,lettersarray[i].x]+letterdict[lettersarray[i].name][lettersarray[i].orientation], axis=0)
                    break

        if invalid:
            invalid.reverse()
            for i in invalid:
                del lettersarray[i]
        else:
            break

    return lettersarray

def isadjacent(l,n):
    if l.orientation%2 == 0:
        if l.x<=n[1] and n[1]<l.x+3 and (n[0]==l.y-1 or n[0]==l.y+5):
            return True
        if l.y<=n[0] and n[0]<l.y+5 and (n[1]==l.x-1 or n[1]==l.x+3):
            return True
    else:
        if l.x<=n[1] and n[1]<l.x+5 and (n[0]==l.y-1 or n[0]==l.y+3):
            return True
        if l.y<=n[0] and n[0]<l.y+3 and (n[1]==l.x-1 or n[1]==l.x+5):
            return True


if __name__ == '__main__' :

    puzzle = sys.argv[1]
    with open(puzzle, "r") as f:
        puzzle = json.load(f)
    teamName = "nom dequipe"
    teamStreetAdress = "817, 54e avenue, Lachine"

    solutions = [solvepuzzle(np.array([[x=="X" for x in l] for l in m], dtype='int')) for m in puzzle]

    #with open("team.json", "r") as f:
    #    team_data = json.load(f)

    output = {
        "teamName": teamName,
        "teamStreetAdress": teamStreetAdress,
        "solutions": solutions
    #    "participants": team_data["participants"]
    }

    print(json.dumps(output))
