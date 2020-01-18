from typing import Dict, List
from game_message import *
from bot_message import *
import random
import copy

class Bot:

    def __init__(self):
        self.plannedPath: List(Move) = []
        self.planets: List(Point) = []
        self.blitz: List(Point) = []

        '''
		This method should be use to initialize some variables you will need throughout the game.
		'''

    def get_next_move(self, game_message: GameMessage) -> Move:
        '''
		Here is where the magic happens, for now the moves are random. I bet you can do better ;)
		'''

        game = game_message.game
        me: Player = game_message.players[game.player_id]

        #try:
        if not self.plannedPath:
            self.planets = self.creerListePlanetes(game)
            self.blitz = self.creerListeBlitz(game)
            target: Point = self.getDestination(me, game)
            path: List(Point) = self.findPath(me.position, target)
            print(path)
            self.plannedPath = self.convert(path, me.direction)
            print(self.plannedPath)
        return self.plannedPath.pop()
        #except:
        #    print("something went wrong")



    def inList(self, point: Point, pointList: List[Point]):
        for pointInList in pointList:
            if point==pointInList:
                return False
        return True


    def norm(self, u, v):
        return abs(u.x - v.x) + abs(u.y - v.y)


    def creerListePlanetes(self, game: Game) -> List[Point]:
        listePlanetes: List[Point] = []
        for j in range(len(game.map)):
            for i in range(len(game.map[j])):
                if game.map[j][i] == "%":
                    p = Point(x=i, y=j)
                    listePlanetes.append(p)
        return listePlanetes

    def creerListeBlitz(self, game: Game) -> List[Point]:
        listeBlitz = []
        for j in range(len(game.map)):
            for i in range(len(game.map[j])):
                if game.map[j][i] == "$":
                    p = Point(x=i, j=y)
                    listeBlitz.append(p)
        return listeBlitz

    def getDestination(self, me: Player, game: Game) -> Point:
        m: int = 1000
        pos: Point = me.position
        for p in self.blitz:
            if game._validate_tile_exists(p) != me.id:
                if abs(self.norm(me.position.x-p.x, me.position.y - p.y)) < m:
                    m = abs(self.norm(me.position.x-p.x, me.position.y - p.y))
                    pos = p
        for p in self.planets:
            if game._validate_tile_exists(p) != me.id:
                if abs(self.norm(me.position.x-p.x, me.position.y - p.y)) < m:
                    m = abs(self.norm(me.position.x-p.x, me.position.y - p.y))
                    pos = p
        return pos

    def convert(self, liste, dirInit):
        mvt=[]
        n = len(liste)-1
        dir = dirInit
        for i in range(n):
            u=liste[i]
            v=liste[i+1]
            vect=[v.x-u.x,v.y-u.y]
            if vect==[1,0]:
                if dir==Direction.RIGHT:
                    mvt.append(Move.FORWARD)
                elif dir==Direction.UP:
                    mvt.append(Move.TURN_RIGHT)
                elif dir==Direction.DOWN:
                    mvt.append(Move.TURN_LEFT)
                dir=Direction.RIGHT
            if vect==[0,-1]:
                if dir==Direction.UP:
                    mvt.append(MoveFORWARD)
                elif dir==Direction.LEFT:
                    mvt.append(Move.TURN_RIGHT)
                elif dir==Direction.RIGHT:
                    mvt.append(Move.TURN_LEFT)
                dir=Direction.UP
            if vect==[-1,0]:
                if dir==Direction.LEFT:
                    mvt.append(Move.FORWARD)
                elif dir==Direction.DOWN:
                    mvt.append(Move.TURN_RIGHT)
                elif dir==Direction.UP:
                    mvt.append(Move.TURN_LEFT)
                dir=Direction.LEFT
            if vect==[0,1]:
                if dir==Direction.DOWN:
                    mvt.append(Move.FORWARD)
                elif dir==Direction.RIGHT:
                    mvt.append(Move.TURN_RIGHT)
                elif dir==Direction.LEFT:
                    mvt.append(Move.TURN_LEFT)
                dir=Direction.DOWN
        return mvt

    def findPath(self, position, target):
        right = copy.copy(position)
        right.x = right.x+1
        return [position,right]
