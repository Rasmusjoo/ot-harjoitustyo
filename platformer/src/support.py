import os
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


def save_score(points, level=None, file=None):
    '''Saves the game's score to a file

    Args:
        points: Amount of points gained in the game.
        level (optional): The level the player was playing when they achieved the score.
        file (optional): The name of the file to save the score to.

    '''
    if not file:
        file = "scores.txt"
    if not level:
        level = "1"
    file_path = os.path.join(dirname, "data", "scores", f"level_{level}", file)

    # Handle errors when opening or writing to the file
    try:
        with open(file_path, "a", encoding="utf-8") as score_file:
            score_file.write(f"{points}\n")
    except IOError as error:
        print(f"Error saving score: {error}")


def fetch_scores(level=None, file=None):
    '''Reads scores from a file and returns them as a list

    Args:
        level (optional): The level to read the scores from.
        file (optional): The name of the file to read the scores from.

    Returns:
        scores: A list of scores from previous games.

    '''
    if not file:
        file = "scores.txt"
    if not level:
        level = "1"
    scores = []
    file_path = os.path.join(dirname, "data", "scores", f"level_{level}", file)

    # Handle errors when opening or reading from the file
    try:
        with open(file_path, "r", encoding="utf-8") as score_file:
            for line in score_file:
                try:
                    score = int(line[:-1])
                except ValueError:
                    print(f"Error: invalid score '{line[:-1]}'")
                    continue
                scores.append(score)
    except IOError as error:
        print(f"Error fetching scores: {error}")
        scores = []

    return scores


def kill_all_sprites(group):
    """Removes all sprites from the specified group.

    Args:
        group: The sprite group from which to remove sprites.

    Returns:
        None
    """
    group.empty()


if __name__ == "__main__":
    save_score(6)
    fetch_scores()
