
from .location import Location


class Rectangle(object):
    def __init__(self, x=0, y=0, w=0, h=0):
        """
        :param int x:
        :param int y:
        :param int w:
        :param int h:
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __repr__(self):
        """
        :rtype: str
        """
        return "%s(%d, %d, %d, %d)" % (
            self.__class__.__name__,
            self.x, self.y, self.w, self.h
        )

    # set

    def setX(self, x: int): self.x = x
    def setY(self, y: int): self.y = y
    def setW(self, w: int): self.w = w
    def setH(self, h: int): self.h = h

    def moveTo(self, location):
        """
        :param Location location:
        :rtype: Rectangle
        """
        self.x, self.y = location.x, location.y
        return self

    def setRect(self, rect):
        """
        :param Rectangle rect:
        """
        self.x = rect.x
        self.y = rect.y
        self.w = rect.w
        self.h = rect.h

    setROI = setRect

    def morphTo(self, reg):
        """
        :param Region reg:
        :rtype: Rectangle
        """
        self.setRect(reg)
        return self

    # get

    def getX(self): return self.x
    def getY(self): return self.y
    def getW(self): return self.w
    def getH(self): return self.h

    def getRect(self):
        """
        :rtype: Rectangle
        """
        return Rectangle(self.x, self.y, self.w, self.h)

    def getCenter(self):
        """
        :rtype: Location
        """
        return Location(self.x + self.w // 2, self.y + self.h // 2)

    def getBounds(self):
        """
        :rtype: (int, int, int, int)
        """
        return self.x, self.y, self.w, self.h

    getTarget = getCenter

    def getTopLeft(self): return Location(self.x, self.y)
    def getTopRight(self): return Location(self.x + self.w, self.y)
    def getBottomLeft(self): return Location(self.x, self.y + self.h)
    def getBottomRight(self): return Location(self.x + self.w, self.y + self.h)

