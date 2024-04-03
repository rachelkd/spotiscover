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
from init import create_app

# PLAYLIST_GRAPH, TRACKS_TO_OBJECTS = load_graph(['data/mpd.slice.0-999.json',
#                                                 'data/mpd.slice.1000-1999.json',
#                                                 'data/mpd.slice.2000-2999.json'])

# manage_io(PLAYLIST_GRAPH)  TODO: DELETE UPON SUBMISSION
# visualize_graph(PLAYLIST_GRAPH, max_vertices=800)  TODO: DELETE UPON SUBMISSION

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['json', 'classes'],  # the names (strs) of imported modules
    #     'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })
