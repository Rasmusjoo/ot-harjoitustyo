import os
import pygame
dirname = os.path.dirname(__file__)


def load_assets(folder, filename):
    image = pygame.image.load(
        os.path.join(dirname, "assets", folder, filename)
    )
    return image


def load_level(levelmap):
    level_data = []
    file = os.path.join(dirname, "data", "level maps", levelmap)
    with open(file, "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
        for line in lines:
            level_data.append(line)

    return level_data

def save_score(points):
    file = os.path.join(dirname, "data", "scores", "scores.txt")
    with open(file, "a", encoding="utf-8") as file_open:
        file_open.write("%s\n" % points)

def fetch_scores():
    scores = []
    file = os.path.join(dirname, "data", "scores", "scores.txt")
    with open(file, "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
        for line in lines:
            scores.append(int(line[:-1]))
    return scores
