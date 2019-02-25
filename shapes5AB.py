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

sPent = Polygon(Point(875, 950), Point(950, 875), Point(925, 800), Point(825, 800), Point(800, 875))
sPent.setFill(color_rgb(0, 225, 0))
sPent.draw(s5Win)

sHex = Polygon(Point(832, 200), Point(917, 200), Point(950, 125), Point(917, 50), Point(832, 50), Point(800, 125))
sHex.setFill(color_rgb(225, 67, 22))
sHex.draw(s5Win)
             
