import random


def flip():
    """Randomly return either 'H' or 'T'."""
    return random.choice(['H', 'T'])


def flip_loaded():
    """Flip a loaded coin."""
    return 'H'
