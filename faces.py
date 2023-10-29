import math

class Face:

    def __init__(self, normal, color):
        self.nrml = (normal[0],normal[1],normal[2])
        self.col = color

    def turn_ud(self, angle):
        tx = self.nrml[0]
        y = self.nrml[1]
        z = self.nrml[2]

        x = round(tx * math.cos(angle) - z * math.sin(angle))
        z = round(tx * math.sin(angle) + z * math.cos(angle))

        self.nrml = (x, y, z)

    def turn_lr(self, angle):
        ty = self.nrml[1]
        x = self.nrml[0]
        z = self.nrml[2]

        y = round(ty * math.cos(angle) - z * math.sin(angle))
        z = round(ty * math.sin(angle) + z * math.cos(angle))

        self.nrml = (x, y, z)

    def turn_fb(self, angle):
        ty = self.nrml[1]
        x = self.nrml[0]
        z = self.nrml[2]

        y = round(ty * math.cos(angle) - x * math.sin(angle))
        x = round(ty * math.sin(angle) + x * math.cos(angle))

        self.nrml = (x, y, z)


