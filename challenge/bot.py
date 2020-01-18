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
        me: Player = players_by_id[game.player_id]

        try:
            if not plannedPath:
                self.planets = creerListePlanetes(game)
                self.blitz = creerListeBlitz(game)
                target: Point = self.getDestination(game, me)
                path: List(Point) = self.findPath(me.position)
                self.plannedPath = self.convert(path)


            return pop(self.plannedPath)


            #players_by_id: Dict[int, Player] = game_message.generate_players_by_id_dict()

			#legal_moves = self.get_legal_moves_for_current_tick(game=game_message.game, players_by_id=players_by_id)


			# You can print out a pretty version of the map but be aware that
			# printing out long strings can impact your bot performance (30 ms in average).
			# print(game_message.game.pretty_map)

			#return random.choice(legal_moves)
		except:
            print("something went wrong")

    def get_legal_moves_for_current_tick(self, game: Game, players_by_id: Dict[int, Player]) -> List[Move]:
        '''
		You should define here what moves are legal for your current position and direction
		so that your bot does not send a lethal move.

		Your bot moves are relative to its direction, if you are in the DOWN direction.
		A TURN_RIGHT move will make your bot move left in the map visualization (replay or logs)
		'''



        me: Player = players_by_id[game.player_id]

        position: Point = me.position
        direction: Direction = me.direction

        up: Point = copy.copy(position)
        up.y = up.y-1
        down: Point = copy.copy(position)
        down.y = down.y+1
        left: Point = copy.copy(position)
        left.x = left.x-1
        right: Point = copy.copy(position)
        right.x = right.x+1

        if direction==Direction.UP:
            forward: Point = up
            leftTurn: Point = left
            rightTurn: Point = right
        elif direction==Direction.DOWN:
            forward: Point = down
            leftTurn: Point = right
            rightTurn: Point = left
        elif direction==Direction.LEFT:
            forward: Point = left
            leftTurn: Point = down
            rightTurn: Point = up
        elif direction==Direction.RIGHT:
            forward: Point = right
            leftTurn: Point = up
            rightTurn: Point = down

        move: List[Move] = []

        #if game.get_tile_type_at(forward)!= TileType.ASTEROIDS and not self.inList(forward,me.tail): move.append(Move.FORWARD)
        #if game.get_tile_type_at(left) != TileType.ASTEROIDS and not self.inList(left,me.tail): move.append(Move.TURN_LEFT)
        #if game.get_tile_type_at(right) != TileType.ASTEROIDS and not self.inList(right,me.tail): move.append(Move.TURN_RIGHT)

        if game.get_tile_type_at(forward)!= TileType.ASTEROIDS: move.append(Move.FORWARD)
        if game.get_tile_type_at(left) != TileType.ASTEROIDS: move.append(Move.TURN_LEFT)
        if game.get_tile_type_at(right) != TileType.ASTEROIDS: move.append(Move.TURN_RIGHT)


        return move


    def inList(self, point: Point, pointList: List[Point]):
        for pointInList in pointList:
            if point==pointInList:
                return False
        return True


    def norm(self, u, v):
        return abs(u.x - v.x) + abs(u.y - v.y)


    def creerListePlanetes(self, game: Game) -> List[Point]:
          listePlanetes: List[Point] = []
          for row in game.map:
            for i in row:
              if game.get_tile_type_at(i) == "%"
                listePlanetes.append(i)
          return listePlanetes

        def creerListeBlitz(self, game: Game) -> List[Point]:
          listeBlitz = []
          for row in game.map:
            for i in row:
              if game.get_tile_type_at(i) == "$"
                listePlanetes.append(i)
          return listePlanetes

    def getDestination(self, me: Player, game: Game) -> Point:
        m: int = 1000
        pos: Point = me.position
        for p in self.blitz:
            if game._validate_tile_exists(p) != me.id
                if abs(self.norm(me.position.x-p.x, me.position.y - p.y)) < m
                    m = abs(self.norm(me.position.x-p.x, me.position.y - p.y))
                    pos = p
        for p in self.planets:
            if game._validate_tile_exists(p) != me.id
                if abs(self.norm(me.position.x-p.x, me.position.y - p.y)) < m
                    m = abs(self.norm(me.position.x-p.x, me.position.y - p.y))
                    pos = p
        return pos


