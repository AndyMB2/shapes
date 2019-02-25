#Graphics program by Andy B

from graphics import *

s5Win = GraphWin("Shapes5", 900, 900)
s5Win.setCoords(0, 0, 1000, 1000)

sTri = Polygon(Point(50, 50), Point(120, 200), Point(200, 50))
sTri.setFill(color_rgb(30, 30, 225))
sTri.draw(s5Win)

sSqr = Polygon(Point(50, 950), Point(200, 950), Point(200, 800), Point(50, 800))
sSqr.setFill(color_rgb(100, 25, 21))
sSqr.draw(s5Win)

