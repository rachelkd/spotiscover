"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module manages the directories of the web application.

Copyright and Usage Information
===============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from flask import Blueprint, render_template, request
from input import return_random_track
from load_data import load_graph
# from track_to_spotify_track import create_track_from_api_response, api_response, get_track_embed_html

PLAYLIST_GRAPH, TRACKS_TO_OBJECTS, URIS_TO_OBJECTS = load_graph(['data/mpd.slice.0-999.json',
                                                                 'data/mpd.slice.1000-1999.json',
                                                                 'data/mpd.slice.2000-2999.json'])

VIEWS = Blueprint('views', __name__)
LIKED_SONGS_SO_FAR = set()


@VIEWS.route('/', methods=['GET', 'POST'])
def home() -> str:
    global LIKED_SONGS_SO_FAR  # Declare liked_songs_so_far as global
    # global liked_songs_so_far_set
    track = return_random_track(PLAYLIST_GRAPH, [])
    uri = track.track_uri[14:]
    uris = set()
    if request.method == 'POST':
        response = request.form['rdo']
        if response == 'yes':
            LIKED_SONGS_SO_FAR.add(track)
    if len(LIKED_SONGS_SO_FAR) >= 3:
        recs = PLAYLIST_GRAPH.get_recommendations(tracks_liked=LIKED_SONGS_SO_FAR)
        LIKED_SONGS_SO_FAR = set()

        for r in recs:
            u = r[0].track_uri[14:]
            uris.add(u)
        return render_template('rec.html', uris=uris)

    else:
        # track = return_random_track(PLAYLIST_GRAPH, [])
        # uri = track.track_uri[14:]
        # track_html = get_track_embed_html(uri)
        return render_template("base.html", uri=uri)

    # else: # GET METHOD
    #     track = return_random_track(PLAYLIST_GRAPH, [])
    #     uri = track.track_uri[14:]
    #     track_html = get_track_embed_html(uri)

    #     return render_template("base.html", uri=uri)


@VIEWS.route('/recomendation')
def rec() -> str:
    return render_template('rec.html')


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['flask', 'input', 'load_data'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
