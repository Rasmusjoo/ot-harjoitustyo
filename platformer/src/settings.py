level_map = [
    "                       WWW       WWW   C       ",
    "                            WWW       WW     WW",
    "        P       C                        W     ",
    "XX     XXX    XXXX               C          W  ",
    "XXX                 Z      X   XXXX    X  W    ",
    "XXXX        Z      XXX    XXX         XX       ",
    "XXXXX  R   XXX CR XXXXXXXXXXXX       XXXX   R C",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  R C XXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


TILE_SIZE = 128
SCREEN_WIDTH = 1480
SCREEN_HIGHT = 1000  # len(level_map) * TILE_SIZE

# camera
camera_borders = {
    "left": 100,
    "right": 200,
    "top": 100,
    "bottom": 150
}
