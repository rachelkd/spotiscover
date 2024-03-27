"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module runs the playlist recommendation algorithm and creates visualizations as such.

Copyright and Usage Information
===============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from load_data import load_graph
from graph_visualization import visualize_graph
# from classes import WeightedGraph

PLAYLIST_GRAPH = load_graph(['data/mpd.slice.0-999.json'])

visualize_graph(PLAYLIST_GRAPH)

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['json', 'classes'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
