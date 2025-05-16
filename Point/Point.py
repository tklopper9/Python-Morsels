class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def coords(self):
        return (self.x, self.y, self.z)
        
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"
        
    def __eq__(self, other):
        if self.coords == other.coords:
            return True
        else:
            return False
    def __add__(self, other):
        x, y, z = tuple(map(sum, zip(self.coords, other.coords)))
        return Point(x, y, z)
        
    def __sub__(self, other):
        point = self + other*(-1)
        return point
        
    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Point(self.x * other, self.y * other, self.z * other)
        
    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Point(self.x * other, self.y * other, self.z * other)
    
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z