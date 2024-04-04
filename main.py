"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module runs the playlist recommendation algorithm and creates visualizations as such.

Copyright and Usage Information
===============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from init import create_app


APP = create_app()


if __name__ == '__main__':
    APP.run(debug=True)
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['init'],  # the names (strs) of imported modules
    #     'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })
