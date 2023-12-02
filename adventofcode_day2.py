from pathlib import Path

input_file = Path("input_day2.txt")

class CubeSet(dict):
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.update({"red":red, "green":green, "blue":blue})
    
    def is_possible(self, r, g, b):
        return (self.get("red") <= r and self.get("green") <= g and self.get("blue") <= b)
    
class Game():
    def __init__(self, uuid) -> None:
        self.uuid = uuid
        self.cube_sets : list[CubeSet] = []
    
    def add_cube_set(self, cube_set):
        self.cube_sets.append(CubeSet(**cube_set))

    def is_possible(self, r, g, b):
        return all([cube_set.is_possible(r, g, b) for cube_set in self.cube_sets])
    
    def max_per_color(self):
        red = max([cube_set.get("red") for cube_set in self.cube_sets])
        green = max([cube_set.get("green") for cube_set in self.cube_sets])
        blue = max([cube_set.get("blue") for cube_set in self.cube_sets])

        return red, green, blue
    
    def __repr__(self) -> str:
        return f"{self.uuid} : Cube Sets = {len(self.cube_sets)}"
    
Games = []
with open(input_file, "r") as open_file:
    for game in open_file:
        game_id, raw_cube_set_data = game.strip().split(":")
        uuid = int(game_id.split(" ")[1])

        G = Game(uuid)

        cube_set_data = raw_cube_set_data.split(";")
        cube_sets = [cube_set.split(",") for cube_set in cube_set_data]
        
        for cube_set in cube_sets:
            cubes = [cube.strip().split(" ") for cube in cube_set]
            
            G.add_cube_set({cube[1]:int(cube[0]) for cube in cubes})
            
        Games.append(G)

# part 1
uuid_sum = 0
for G in Games:
    if G.is_possible(12, 13, 14):
        uuid_sum += G.uuid

print(uuid_sum)

# part 2
power_sum = 0
for G in Games:
    r, g, b = G.max_per_color()
    power_sum += r*g*b

print(power_sum)