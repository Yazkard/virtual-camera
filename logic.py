from logic_classes import *


class Engine:
    def __init__(self, file):
        self.d = 15
        self.cuboid_list = []
        self.read_file(file)
    
    def read_file(self, file):
        new = Cuboid(100, 100, 100, 1000, 1000, 100)
        self.cuboid_list.append(new)
        new = Cuboid(-1100, 100, 100, 1000, 1000, 100)
        self.cuboid_list.append(new)
        print(self.cuboid_list)

    def move(self, x, y, z):
        for cub in self.cuboid_list:
            cub.move(x,y,z)

    def get_projection(self):
        proj_dict = dict()
        for cub in self.cuboid_list:
            d = cub.get_projection(self.d)
            proj_dict.update(d)
        return proj_dict