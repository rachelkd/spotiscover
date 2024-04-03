"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
TODO

Copyright and Usage Information
==============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    from views import VIEWS

    app.register_blueprint(VIEWS, url_prefix='/')

    return app


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['flask', 'views'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
