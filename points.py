class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#     def add(self):
#         return self.x + self.y
# obj1 = points(2, 3)
# print(obj1.add())

    def show(self):
        print("Vector:", self.x, self.y)


v1 = vector(3, 4)
v1.show()