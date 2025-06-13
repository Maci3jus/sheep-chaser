import math


class Wolf:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def find_closest_sheep(self, sheep_list):
        alive_sheep = []
        for sheep in sheep_list:
            if sheep.is_alive:
                alive_sheep.append(sheep)

        min_distance = math.inf
        closest_sheep = None
        for sheep in alive_sheep:
            distance = math.sqrt((sheep.x - self.x) ** 2 + (sheep.y - self.y) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_sheep = sheep

        return closest_sheep

    def chase(self, sheep):
        distance = math.sqrt((sheep.x - self.x) ** 2 + (sheep.y - self.y) ** 2)
        if distance <= 1.0:
            sheep.is_alive = False
            self.x, self.y = sheep.x, sheep.y
            print(f'Wolf ate sheep number: {sheep.id}')

        else:
            direction_x = (sheep.x - self.x) / distance
            direction_y = (sheep.y - self.y) / distance
            self.x = self.x + direction_x
            self.y = self.y + direction_y
            print(f'Wolf is chasing sheep number: {sheep.id}')

    def __str__(self):
        return f'Wolf: {self.x:.3f} {self.y:.3f}'
