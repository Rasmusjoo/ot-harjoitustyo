level_map = [
    "                                          ",
    "        P       C                         ",
    "XX     XXX    XXXX               C        ",
    "XXX                 Z      X   XXXX    X  ",
    "XXXX        Z      XXX    XXX         XX  ",
    "XXXXX  R   XXX  RCXXXXXXXXXXXX       XXX  ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  R   XXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


TILE_SIZE = 128
SCREEN_WIDTH = 1280
SCREEN_HIGHT = len(level_map) * TILE_SIZE

# camera
camera_borders = {
    "left": 100,
    "right": 200,
    "top": 100,
    "bottom": 150
}
