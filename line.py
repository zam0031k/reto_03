import math
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        """Compute the distance between two points."""
        return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5

    def compute_slope(self) -> float:
        """Compute the slope of the line."""
        if self.end.x == self.start.x:
            raise ValueError("Slope is undefined for vertical lines.")
        return (self.end.y - self.start.y) / (self.end.x - self.start.x)

    def compute_horizontal_cross(self) -> float:
        """Compute the x-coordinate where the line crosses the horizontal axis (y=0)."""
        if self.start.y == self.end.y:
            raise ValueError("The line is horizontal and does not cross the horizontal axis.")
        slope = self.compute_slope()
        return self.start.x - self.start.y / slope

    def compute_vertical_cross(self) -> float:
        """Compute the y-coordinate where the line crosses the vertical axis (x=0)."""
        slope = self.compute_slope()
        return self.start.y - slope * self.start.x


class Rectangle:
    def __init__(self, meth, *args):
        if meth == 1 and len(args) == 3 and isinstance(args[0], Point) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            # Método 1: Esquina inferior izquierda + ancho y alto
            point_left, w, h = args
            self.width = w
            self.height = h
            self.point_left_corner = Point(point_left.x, point_left.y)
            self.point_top_right = Point(point_left.x + self.width, point_left.y + self.height)
        elif meth == 2 and len(args) == 3 and isinstance(args[0], Point) and isinstance(args[1], (int, float)) and isinstance(args[2], (int, float)):
            # Método 2: Centro + ancho y alto
            point_center, w, h = args
            self.center = Point(point_center.x, point_center.y)
            self.width = w
            self.height = h
            self.point_left_corner = Point(
                self.center.x - self.width / 2,
                self.center.y - self.height / 2,
            )
            self.point_top_right = Point(
                self.center.x + self.width / 2,
                self.center.y + self.height / 2,
            )
        elif meth == 3 and len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            # Método 3: Dos esquinas opuestas
            point_left, point_right = args
            self.width = point_right.x - point_left.x
            self.height = point_right.y - point_left.y
            self.point_left_corner = Point(point_left.x, point_left.y)
            self.point_top_right = Point(point_right.x, point_right.y)
        elif meth == 4 and len(args) == 4 and all(isinstance(arg, Line) for arg in args):
            # Método 4: Cuatro lados
            l_right, l_left, l_top, l_down = args
            self.line_right = l_right
            self.line_left = l_left
            self.line_top = l_top
            self.line_down = l_down

            self.width = self.line_down.compute_length()
            self.height = self.line_left.compute_length()
            self.center = Point(
                ((self.line_left.start.x + self.width) / 2),
                ((self.line_top.end.y - self.height) / 2),
            )
            self.point_left_corner = Point(self.line_left.start.x, self.line_left.start.y)
            self.point_top_right = Point(self.line_top.end.x, self.line_top.end.y)
        else:
           raise ValueError("Número de argumentos inválido para inicializar un rectángulo.")

    def compute_area(self) -> float:
        """Compute the area of the rectangle."""
        return self.width * self.height


# Ejemplos de uso:
# Método 1
rect1 = Rectangle(1, Point(0, 0), 10, 5)
print(f"Rect1: {rect1.point_left_corner.x}, {rect1.point_left_corner.y}, {rect1.width}, {rect1.height}")

# Método 2
rect2 = Rectangle(2, Point(5, 5), 10, 5)
print(f"Rect2: {rect2.point_left_corner.x}, {rect2.point_left_corner.y}, {rect2.width}, {rect2.height}")

# Método 3
rect3 = Rectangle(3, Point(0, 0), Point(10, 5))
print(f"Rect3: {rect3.point_left_corner.x}, {rect3.point_left_corner.y}, {rect3.width}, {rect3.height}")

# Método 4
line_right = Line(Point(10, 0), Point(10, 5))
line_left = Line(Point(0, 0), Point(0, 5))
line_top = Line(Point(0, 5), Point(10, 5))
line_down = Line(Point(0, 0), Point(10, 0))
rect4 = Rectangle(4, line_right, line_left, line_top, line_down)
print(f"Rect4: {rect4.point_left_corner.x}, {rect4.point_left_corner.y}, {rect4.width}, {rect4.height}")

# Crear puntos
point1 = Point(1, 2)
point2 = Point(4, -2)

# Crear una línea
line = Line(point1, point2)

# Imprimir la longitud de la línea
print(f'The line\'s length: {line.compute_length()}')

# Imprimir la pendiente de la línea en grados
slope_rad = math.atan(line.compute_slope())
slope_deg = math.degrees(slope_rad)
print(f'The slope of the line from the horizontal axis in degrees: {slope_deg}')

# Imprimir la coordenada x donde la línea cruza el eje horizontal
print(f'The line crosses the horizontal axis at x = {line.compute_horizontal_cross()}')

# Imprimir la coordenada y donde la línea cruza el eje vertical
print(f'The line crosses the vertical axis at y = {line.compute_vertical_cross()}')