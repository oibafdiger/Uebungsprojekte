import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        x,y = self.position
        dx, dy = move
        # Update Position
        self.position = (x + dx, y + dy)

        # append to path
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self, moves):
        super().__init__()
        # Standardbewegungen: up, down, left, right
        self.moves = [
            (0, 1),  #up
            (0, -1), #down
            (-1, 0), #left
            (1, 0)   #right
        ]  
    
    def level_up(self):
        # Diagonale Bewegungen hinzufügen
        diagonal_moves = [
            (1, 1),  #up-right
            (1, -1), #down-right
            (-1, 1), #up-left
            (-1, -1) #down-left
        ]
        self.moves.extend(diagonal_moves)

# Beispiel: Erstellung eines Pawns und Test der Methoden
pawn = Pawn("P1")
print("Startposition:", pawn.position)
print("Pfad:", pawn.path)

# Bewegung ausführen
for _ in range(5):
    new_pos = pawn.make_move()
    print(f"Bewegt nach: {new_pos}")

# Level-Up: Diagonale Bewegungen hinzufügen
pawn.level_up()
print("Nach Level-Up:", len(pawn.moves), "Bewegungen")

# Prüfen, ob Diagonale hinzugefügt wurden
print("Neue Bewegungen:", pawn.moves[-4:])



