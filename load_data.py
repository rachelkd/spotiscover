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
from graph import _Vertex, Graph, WeightedGraph, _WeightedVertex  # See if we need unweighted graph classes upon submission


def _add_tracks_to_graph(graph: Graph, file: TextIO) -> None:
    """Read playlist data (JSON file) in file.

    - Each track in a playlist in our data is a Track object.
    - Each Track gets added to the given graph.
    """


def load_graph(file_names: list[str]) -> WeightedGraph:
    """Returns a WeightedGraph that contains all tracks in the file_names' data.

    - Each vertex represents a track in our playlist data.
    - A weighted edge between two tracks represents the number of playlists that contain both tracks.
    """
    with



if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
