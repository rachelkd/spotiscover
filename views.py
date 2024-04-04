"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module manages the routing of the web application.

Copyright and Usage Information
===============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""

from flask import Blueprint, render_template, request, session
from input import return_random_track
from load_data import load_graph

PLAYLIST_GRAPH, TRACKS_TO_OBJECTS, URIS_TO_OBJECTS = load_graph(['data/mpd.slice.0-999.json',
                                                                 'data/mpd.slice.1000-1999.json',
                                                                 'data/mpd.slice.2000-2999.json'])

VIEWS = Blueprint('views', __name__)
LIKED_SONGS_SO_FAR = set()


@VIEWS.route('/', methods=['GET', 'POST'])
@VIEWS.route('/')
def home() -> str:
    """Renders the home page of the application.
    If a POST request is received, it processes the user's response to the displayed track.
    If enough songs have been liked, it generates recommendations and renders the recommendation page.
    If not enough songs have been liked, it renders the base template with a random track.

    Returns the rendered HTML content in str.
    """
    global LIKED_SONGS_SO_FAR

    if request.method == 'POST':
        response = request.form.get('rdo')  # Get the value of the radio button

        if response == 'yes':
            t = URIS_TO_OBJECTS[session['uri']]
            LIKED_SONGS_SO_FAR.add(t)

    if len(LIKED_SONGS_SO_FAR) >= 3:
        recs = PLAYLIST_GRAPH.get_recommendations(tracks_liked=LIKED_SONGS_SO_FAR)
        LIKED_SONGS_SO_FAR.clear()  # Clear liked_songs_so_far after generating recommendations

        uris = [r[0].track_uri[14:] for r in recs]
        return render_template('rec.html', uris=uris)
    else:
        track = return_random_track(PLAYLIST_GRAPH, [])
        full_track_uri = track.track_uri
        uri = full_track_uri[14:]
        session['uri'] = full_track_uri
        return render_template("base.html", uri=uri)


@VIEWS.route('/recomendation')
def rec() -> str:
    """Renders the recommendation page.
    Returns the str rendered HTML content for the recommendation page.
    """
    return render_template('rec.html')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['flask', 'input', 'load_data'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
