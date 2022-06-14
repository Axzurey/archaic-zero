import math
from pygame import Vector2


def lerp(a: float, b: float, t: float) -> float:
    return (1 - t) * a + t * b

def pointsOnCircle(radius: float, points: int):
    angle = 2 * math.pi / points
    return [Vector2(math.cos(i * angle), math.sin(i * angle)) * radius for i in range(points)]

def normalize(min, max, value):
    return (value - min) / (max - min)