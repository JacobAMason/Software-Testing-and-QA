class DistanceFormula:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.distance = 0

    def hello_world(self):
        return "hello world"

    def compute_distance(self):
        self.distance = self.x1 - self.x2
        return self.distance


if __name__ == '__main__':
    DF = DistanceFormula()
