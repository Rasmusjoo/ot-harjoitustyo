import os
import pygame
dirname = os.path.dirname(__file__)


def load_assets(folder, filename):
    '''Returns wanted image

    Args:
        folder: The folder in which the image is located
        filename: Name of the imagefile

    Returns:
        imagefile
    '''
    image = pygame.image.load(
        os.path.join(dirname, "assets", folder, filename)
    ).convert_alpha()
    return image


def load_level(levelmap):
    '''Loads level data from file

    Args:
        levelmap: Filename of the wanted level

    Returns:
        level_data: List of strings needed for level creation.

    '''
    level_data = []
    file = os.path.join(dirname, "data", "level maps", f"level_{levelmap}")
    with open(file, "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
        for line in lines:
            level_data.append(line)

    return level_data


def save_score(points):
    '''Saves the games score to a file

    Args:
        points: Amount of points gained in the game.

    '''
    file = os.path.join(dirname, "data", "scores", "scores.txt")
    with open(file, "a", encoding="utf-8") as file_open:
        file_open.write(f"{points}\n")


def fetch_scores():
    '''Reads sccores from a file and places them in a list

    Returns:
        scores: A list of scores from previous games

    '''
    scores = []
    file = os.path.join(dirname, "data", "scores", "scores.txt")
    with open(file, "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
        for line in lines:
            scores.append(int(line[:-1]))
    return scores
