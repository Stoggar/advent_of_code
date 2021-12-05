
with open('./day5.txt', 'r') as f:
    lines = f.readlines()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def from_str(point: str):
        listform = point.split(',')
        x = int(listform[0])
        y = int(listform[1])
        return Point(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'


class Vector:
    def __init__(self, line: str):
        parts = line.strip('\n').split('->')
        parts = [part.strip() for part in parts]
        self.start = Point.from_str(parts[0])
        self.end = Point.from_str(parts[1])

    def hor_or_ver(self):
        return self.start.x == self.end.x or self.start.y == self.end.y

    def points_covered(self):
        if self.start.x == self.end.x or self.start.y == self.end.y:
            return self.points_covered_hor_ver()
        current = self.start
        points = [current]
        while current != self.end:
            print(current, self.start, self.end)
            x = current.x + 1 if self.end.x > current.x else current.x - 1
            y = current.y + 1 if self.end.y > current.y else current.y - 1
            current = Point(x, y)
            points.append(current)
        return points

    def points_covered_hor_ver(self):
        if not self.hor_or_ver():
            raise ValueError
        if self.start.x == self.end.x:
            if self.start.y < self.end.y:
                y_coords = range(self.start.y, self.end.y + 1)
            else:
                y_coords = range(self.start.y, self.end.y -1, -1)
            return [Point(self.start.x, i) for i in y_coords]
        if self.start.y == self.end.y:
            if self.start.x < self.end.x:
                x_coords = range(self.start.x, self.end.x + 1)
            else:
                x_coords = range(self.start.x, self.end.x -1, -1)
            return [Point(i, self.start.y) for i in x_coords]

    def __repr__(self):
        return f'Vector(start={self.start}, end={self.end}'


class Map:
    def __init__(self, vectors):
        size_x, size_y = self._size(vectors)
        self.map = [[0 for i in range(size_x)] for i in range(size_y)]

    def mark(self, point):
        self.map[point.y][point.x] += 1

    def count_overlap(self):
        s = 0
        for row in self.map:
            for x in row:
                if x > 1:
                    s += 1
        return s

    @staticmethod
    def _size(vectors):
        x = 0
        y = 0
        for v in vectors:
            for point in [v.start, v.end]:
                if point.x > x:
                    x = point.x
                if point.y > y:
                    y = point.y
        # we found largest indices, +1 for size
        return x+1, y+1
        

    def __repr__(self):
        s = ''
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                s += f'{self.map[i][j]} '
            s += '\n'
        return s


vectors = [Vector(line) for line in lines]
#vectors = [v for v in vectors if v.hor_or_ver()]
m = Map(vectors)
for v in vectors:
    [m.mark(p) for p in v.points_covered()]
print(m.count_overlap())










