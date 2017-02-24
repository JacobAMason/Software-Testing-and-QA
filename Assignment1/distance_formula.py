from math import sqrt


class DistanceFormulaCalculator:
    @staticmethod
    def compute_distance(x1, y1, x2, y2):
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return distance


if __name__ == '__main__':
    DF = DistanceFormulaCalculator()
