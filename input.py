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


def manage_io(g: WeightedGraph, num_reccomend: int = 10) -> None:
    """Asks user to like ten randomly-chosen tracks (vertices) in the given graph.
    Returns <num_recommend> recommended Tracks to user.
    """
    tracks_to_like = return_10_random_tracks(g, occur_min=30)
    print('Please like exactly THREE songs in this list.')
    print('===================================================')
    for i in range(len(tracks_to_like)):
        print(f'{i + 1}. {tracks_to_like[i].artist_name} - {tracks_to_like[i].track_name}')
    print('===================================================')
    index_liked_tracks = input('Type the number of the songs that you like (e.g., \"1 3 4\"), '
                               'separated by spaces: \n')

    # Check that three songs are liked
    while len(index_liked_tracks.split()) != 3 or any(not (num.isdigit() and 0 < int(num) <= 10)
                                                      for num in index_liked_tracks.split()):
        print('Invalid number or not enough songs liked.')
        print(f'Please like THREE songs. You have liked {len(index_liked_tracks.split())} songs.')
        index_liked_tracks = input('Type the number of songs that you enjoy, separated by commas: \n')

    liked_tracks = {tracks_to_like[int(num) - 1] for num in index_liked_tracks.split()}

    recommended_tracks = g.get_recommendations(liked_tracks, num_reccomend, occur_limit=30)

    for track in recommended_tracks:
        print(f'{track[0].artist_name} - {track[0].track_name} : {track[1]}')


def return_10_random_tracks(g: WeightedGraph, occur_min: int = 30) -> list[Track]:
    """Return a list of 10 random Tracks in the given WeightedGraph.
    The random Tracks selected have at least <occur_min> occurrences in the WeightedGraph.
    This is to ensure that some of the somes are somewhat relevant to the user.

    Preconditions:
        - all(isinstance(v, Track) for v in g.get_all_vertices())
    """
    more_than_10_occ = [track for track in g.get_all_vertices() if g.get_occurrences(track) >= occur_min]
    list_so_far = []

    for _ in range(10):
        random_int = random.randint(0, len(more_than_10_occ) - 1)
        list_so_far.append(more_than_10_occ.pop(random_int))

    return list_so_far


def return_random_track(g: WeightedGraph, cannot_contain: list[Track], occur_min: int = 30) -> Track:
    """Return a random Track in the given WeightedGraph that is NOT a track in <cannot_contain>.
    The random Track selected has at least <occur_min> occurrences in the WeightedGraph.
    This is to ensure that some of the somes are somewhat relevant to the user.

    Preconditions:
        - all(isinstance(v, Track) for v in g.get_all_vertices())
    """
    more_than_occur_min = [track for track in g.get_all_vertices() if g.get_occurrences(track) >= occur_min]
    random_int = random.randint(0, len(more_than_occur_min) - 1)

    # If the random track is in cannot_contain, reselect random song
    while more_than_occur_min[random_int] in cannot_contain:
        random_int = random.randint(0, len(more_than_occur_min) - 1)

    return more_than_occur_min[random_int]


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
