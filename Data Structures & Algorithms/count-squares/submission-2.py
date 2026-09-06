class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.points:
            prev = self.points[point]
            self.points[point] = prev + 1
        else:
            self.points[point] = 1

    def count(self, point: List[int]) -> int:
        cnt = 0
        qx, qy = point
        for point, freq in self.points.items():
            x, y = point
            if (qx-x) != 0 and (((qy-y) / (qx-x)) == 1 or ((qy-y) / (qx-x)) == -1):
                # check for other 2 points
                first = (x, qy)
                second = (qx, y)
                if first in self.points and second in self.points:
                    f1 = self.points[first]
                    f2 = self.points[second]

                    cnt += (freq * f1 * f2)

        return cnt