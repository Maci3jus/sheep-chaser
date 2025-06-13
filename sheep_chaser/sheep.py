import random


class Sheep:

    def __init__(self, sheep_id):
        self.x = random.uniform(-10.0, 10.0)
        self.y = random.uniform(-10.0, 10.0)
        self.is_alive = True
        self.id = sheep_id

    def move(self):
        if not self.is_alive:
            return

        direction = random.choice(["north", "south", "east", "west"])

        if direction == "north":
            self.y += 0.5
        elif direction == "south":
            self.y -= 0.5
        elif direction == "east":
            self.x += 0.5
        elif direction == "west":
            self.x -= 0.5
