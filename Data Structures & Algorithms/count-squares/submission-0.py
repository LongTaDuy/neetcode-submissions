class CountSquares:

    def __init__(self):
        self.pointcount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointcount[tuple(point)] += 1
        self.points.append(point)
        

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0
        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or px == x or py == y:
                continue
            res += self.pointcount[(px, y)] * self.pointcount[(x, py)]
        return res
        
