import os
import json
import pygame
dirname = os.path.dirname(__file__)


def load_assets(folder, *filenames):
    '''Loads one or more image files from the specified folder.

    Args:
        folder: The name of the folder containing the image files.
        *filenames: One or more image file names to load.

    Returns:
        A list of image objects.
    '''
    images = []
    for filename in filenames:
        try:
            image = pygame.image.load(
                os.path.join(dirname, "assets", folder, filename)
            ).convert_alpha()
            images.append(image)
        except pygame.error as error:
            print(f"Error loading image {filename}: {error}")
    return images


def load_level(levelmap):
    '''Loads level data from file

    Args:
        levelmap: Filename of the wanted level

    Returns:
        level_data: List of strings needed for level creation.

    '''
    level_data = []
    file = os.path.join(dirname, "data", "levels", f"level_{levelmap}")
    with open(file, "r", encoding="utf-8") as file_open:
        lines = file_open.readlines()
        for line in lines:
            level_data.append(line)

    return level_data


def save_score(points, player_name=None, level=None, file=None):
    '''Saves the game's score to a file

    Args:
        points: Amount of points gained in the game.
        player_name (optional): The nametag of the player
        level (optional): The level the player was playing when they achieved the score.
        file (optional): The name of the file to save the score to.

    '''
    if not player_name:
        player_name = "player_1"
    if not file:
        file = "scores.json"
    if not level:
        level = "1"
    file_path = os.path.join(dirname, "data", "scores", f"level_{level}", file)

    # Load the existing scores from the file
    try:
        with open(file_path, "r", encoding="utf-8") as score_file:
            scores = json.load(score_file)
    except IOError:
        scores = []

    # Add the new score to the list
    scores.append({"points": points, "player_name": player_name})

    # Save the updated list of scores to the file
    try:
        with open(file_path, "w", encoding="utf-8") as score_file:
            json.dump(scores, score_file)
    except IOError as error:
        print(f"Error saving score: {error}")


def fetch_scores(level=None, file=None):
    '''Fetches the scores from the file

    Args:
        level (optional): The level to fetch the scores for.
        file (optional): The name of the file to fetch the scores from.

    Returns:
        scores : A list of scores. Each score is a dictionary
        containing "points" and "player_name" keys.
    '''
    if not file:
        file = "scores.json"
    if not level:
        level = "1"
    file_path = os.path.join(dirname, "data", "scores", f"level_{level}", file)

    # Load the scores from the file
    try:
        with open(file_path, "r", encoding="utf-8") as score_file:
            scores = json.load(score_file)
    except IOError:
        scores = []

    return scores


def kill_all_sprites(groups):
    """Removes all sprites from the specified groups.

    Args:
        groups: A sprite group or a list of sprite groups from which to remove sprites.

    Returns:
        None
    """
    # If groups is a single group, wrap it in a list
    if isinstance(groups, pygame.sprite.Group):
        groups = [groups]

    for group in groups:
        group.empty()
