"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module creates the views of our web application.

Copyright and Usage Information
==============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from flask import Flask
from views import VIEWS


def create_app() -> Flask:
    """Creates and configures the Flask application. Returns the configured Flask application.
    """
    app = Flask(__name__)
    # from views import VIEWS
    app.secret_key = '1893tbdiub3u3'
    app.register_blueprint(VIEWS, url_prefix='/')

    return app


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['flask', 'views'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
