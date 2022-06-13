def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t

def normalize(min, max, value):
    return (value - min) / (max - min)