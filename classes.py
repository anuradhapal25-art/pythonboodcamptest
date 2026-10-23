class Pen:
    def write(self):
        print("Pen is writing")

class Pencil:
    def write(self):
        print("Pencil is writing")

class Marker:
    def write(self):
        print("Marker is writing")

items = [Pen(), Pencil(), Marker()]

for item in items:
    item.write()