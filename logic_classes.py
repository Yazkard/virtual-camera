class Cuboid:
    def __init__(self, apex_list):
        self.apex_list = apex_list

class Apex:
    def __init__(self, x,y,z neighbours):
        self.x = x
        self.y = y
        self.z = z
        self.neighbours = []

    def add_neighbour(new_neighbour):
        self.neighbours.append(new_neighbour)
        if self not in new_neighbour.neighbours:
            new_neighbour.add_neighbour(self)
