class Cell:
    def __init__(self, x, y, value=0):
        self.value = value
        self.x = x
        self.y = y
        self.quad = self.pick_quad()
        self.availability = set(range(1,10,1)) if value == 0 else set()


    def pick_quad(self):
        return int(self.x / 3) + int(self.y / 3) * 3


    def update_available(self, values=set()):
        self.availability -= values


    def __str__(self):
        val = "" if self.value == 0 else str(self.value)
        return "(" + ','.join([str(self.x), str(self.y), str(self.quad)]) + "):" + val



s = Cell(0, 0)
print(s)