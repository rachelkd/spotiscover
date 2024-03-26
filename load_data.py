"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module loads the data and creates the graph needed for our project.

Copyright and Usage Information
===============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from __future__ import annotations
import json
from typing import Optional, TextIO, Union
from classes import _Vertex, Graph, WeightedGraph, _WeightedVertex  # See if we need unweighted graph classes upon submission

TRACKS_TO_OBJECTS = {}  # Maps tuple ({artist_name}, {track_name}) to corresponding Track object


def _add_tracks_to_graph(g: Graph, file: TextIO) -> None:
    """Read playlist data (JSON file) in file and *mutates* given graph to add vertices and edges
    according to data.

    - Each track in a playlist in our data is a Track object.
    - Each edge indicates that two Tracks appear in the same playlist
    - The edge weight indicates the number of playlists that contain both Tracks
    """

    # Read line by line
    # while ...
    #   Get playlist id
    #   Get track info
    #   Create new track object if not in TRACKS_TO_OBJECTS
    #   Map track to Track object
    #   Add to graph g
    pass


def load_graph(file_names: list[str]) -> WeightedGraph:
    """Returns a WeightedGraph that contains all tracks in the file_names' data.

    - Each vertex represents a track in our playlist data.
    - A weighted edge between two tracks represents the number of playlists that contain both tracks.
    """
    g = WeightedGraph()

    for file_dir in file_names:
        with open(file_dir) as file:
            _add_tracks_to_graph(g, file)

    return g


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['json', 'classes'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
