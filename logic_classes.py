class Cuboid:
    def __init__(self, x, y, z, size_x, size_y, size_z):
        self.apex_list = []
        self.apex_list.append(Apex(x, y, z)) 
        self.apex_list.append(Apex(x+size_x, y, z)) 
        self.apex_list.append(Apex(x+size_x, y+size_y, z)) 
        self.apex_list.append(Apex(x+size_x, y+size_y, z+size_z)) 
        self.apex_list.append(Apex(x+size_x, y, z+size_z)) 
        self.apex_list.append(Apex(x, y+size_y, z))
        self.apex_list.append(Apex(x, y, z+size_z))
        self.apex_list.append(Apex(x, y+size_y, z+size_z))
        for apex in self.apex_list:
            for apex2 in self.apex_list:
                p = 0
                if apex is not apex2:
                    if apex.x == apex2.x:
                        p = p+1
                    if apex.y == apex2.y:
                        p = p+1
                    if apex.z == apex2.z:
                        p = p+1
                    if p==2:
                        apex.add_neighbour(apex2)
    def move(self, x, y, z):
        for apex in self.apex_list:
            apex.x += x
            apex.y += y
            apex.z += z


    # def rotate(self, pitch, roll, yaw):
        # return 0
        

    def get_projection(self, d):
        projection_dict = dict()
        for apex in self.apex_list:
            new_x = ((apex.x * d)/apex.z)+500
            new_y = ((apex.y * d)/apex.z)+500
            new_proj_apex = Projected_Apex(new_x, new_y)
            projection_dict[apex] = new_proj_apex
            new_proj_apex.print_all()
        used_apex = []
        for key_apex, proj_apex in projection_dict.items():
            for neighbour in key_apex.neighbours:
                if neighbour not in used_apex:
                    proj_apex.add_neighbour(projection_dict[neighbour])
            used_apex.append(key_apex)
        return projection_dict

class Apex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.neighbours = []

    def add_neighbour(self, new_neighbour):
        self.neighbours.append(new_neighbour)
        if self not in new_neighbour.neighbours:
            new_neighbour.add_neighbour(self)

class Projected_Apex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.mother_apex = mother_apex
        self.neighbours = []

    def add_neighbour(self, new_neighbour):
        if new_neighbour not in self.neighbours:
            self.neighbours.append(new_neighbour)
            new_neighbour.add_neighbour(self)
    def print_all(self):
        print("x: ", self.x, "y:", self.y)