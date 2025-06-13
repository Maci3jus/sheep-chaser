import csv
import json

from sheep import Sheep
from wolf import Wolf


class Simulator:

    def __init__(self):
        self.round_num = 0
        self.max_rounds = 50
        self.start_sheep = 15
        self.csv_filename = 'alive.csv'
        self.json_filename = 'pos.json'
        self.alive_sheep = 0
        self.csv_data = []
        self.json_data = []

    def simulate(self):
        sheep_list = [Sheep(i) for i in range(self.start_sheep)]
        wolf = Wolf(0.0, 0.0)

        for self.round_num in range(self.max_rounds):
            print(f'Round {self.round_num + 1}')
            self.alive_sheep = 0
            sheep_positions = []

            for sheep in sheep_list:
                if sheep.is_alive:
                    sheep.move()

            closest_sheep = wolf.find_closest_sheep(sheep_list)

            if closest_sheep:
                wolf.chase(closest_sheep)
                print(wolf)
            else:
                print(f'All sheep are gone')
                break

            for sheep in sheep_list:
                if sheep.is_alive:
                    self.alive_sheep += 1
                    sheep_positions.append((sheep.x, sheep.y))
                else:
                    sheep_positions.append(None)

            print(f'Sheep alive: {self.alive_sheep}')

            self.csv_data.append([self.round_num + 1, self.alive_sheep])
            self.json_data.append({
                "round_no": self.round_num + 1,
                "wolf_pos": (wolf.x, wolf.y),
                "sheep_pos": sheep_positions
            })
        with open(self.csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['round number', 'alive_sheep'])
            writer.writerows(self.csv_data)

        with open(self.json_filename, 'w') as json_file:
            json.dump(self.json_data, json_file, indent=4)
