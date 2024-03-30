"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module manages input and output between the user and program.

Copyright and Usage Information
==============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from classes import WeightedGraph, Track
import random


def manage_io(g: WeightedGraph, num_suggestions: int = 10) -> None:
    """Asks user to rate three randomly-chosen tracks (vertices) in the given graph.
    Suggests {num_suggestions} number of Tracks to user.
    """
    raise NotImplemented


def return_10_random_song(g: WeightedGraph, occur_min: int=10) -> list[Track]:
    """Return a list of 10 random Tracks in the given WeightedGraph.
    The random Tracks selected have at least {occur_min} occurrences in the WeightedGraph.

    Preconditions:
        - all(isinstance(v, Track) for v in g.get_all_vertices())
    """
    more_than_10_occ = [track for track in g.get_all_vertices() if g.get_occurrences(track) >= occur_min]
    list_so_far = []
    for i in range(10):
        list_so_far.append(random.choice(more_than_10_occ))
    return list_so_far


# def get_user_ratings(g: WeightedGraph):
#     """Return a mapping of three randomly-picked rated tracks to user rating.
#     If the user does not know a song, then another track is randomly picked.
#
#     Preconditions:
#         - all(isinstance(v, Track) for v in g.get_all_vertices())
#     """
#     rated_so_far = 0
#     while rated_so_far < 3:
#         random_track = random.choice(list(g.get_all_vertices()))
#
#     # TODO: Figure out how to pass variables down in Flask



if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['networkx'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
