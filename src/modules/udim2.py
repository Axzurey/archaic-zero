from pygame import Vector2


class udim2:
    xScale: float = 0
    yScale: float = 0
    xOffset: float = 0
    yOffset: float = 0
    def __init__(self, xOffset: float = 0, xScale: float = 0, yOffset: float = 0, yScale: float = 0):
        self.xOffset = xOffset
        self.xScale = xScale
        self.yOffset = yOffset
        self.yScale = yScale

    @staticmethod
    def fromScale(xScale: float = 0, yScale: float = 0):
        return udim2(0, xScale, 0, yScale)

    @staticmethod
    def fromOffset(xOffset: float = 0, yOffset: float = 0):
        return udim2(xOffset, 0, yOffset, 0)

    def toScale(self):
        return Vector2(self.xScale, self.yScale)

    def toOffset(self):
        return Vector2(self.xOffset, self.yOffset)