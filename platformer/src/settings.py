level_map = [
    "                       WWW       WWW   C       ",
    "                            WWW       WW     WW",
    "        P       C                        W     ",
    "XX     XXX    XXXX               C          W  ",
    "XXX                 Z      X   XXXX    X  W    ",
    "XXXX        Z      XXX    XXX         XX       ",
    "XXXXX  R   XXX CR XXXXXXXXXXXX       XXXX   R C",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  R C XXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]

test_level_map = [
    "       ",
    "   P   ",
    "XXXXXXX"]

test_level_map_2 = [
    "       ",
    "   P  Z",
    "XXXXXXX"]

TILE_SIZE = 128
WINDOW_WIDTH = 1480
WINDOW_HIGHT = 1000  # len(level_map) * TILE_SIZE

# camera
camera_borders = {
    "left": 100,
    "right": 200,
    "top": 100,
    "bottom": 150
}
