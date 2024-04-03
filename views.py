"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module manages the directories of the web application.

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

views = Blueprint('views', __name__)
liked_songs_so_far = set()

@views.route('/', methods=['GET', 'POST'])
@views.route('/')
def home():
    global liked_songs_so_far
    
    if request.method == 'POST':
        response = request.form.get('rdo')  # Get the value of the radio button
        
        if response == 'yes':
            liked_songs_so_far.add(session['track'])
    
    if len(liked_songs_so_far) >= 3:
        recs = PLAYLIST_GRAPH.get_recommendations(tracks_liked=liked_songs_so_far)
        liked_songs_so_far.clear()  # Clear liked_songs_so_far after generating recommendations
        
        uris = [rec[0].track_uri[14:] for rec in recs]
        return render_template('rec.html', uris=uris)
    else:
        track = return_random_track(PLAYLIST_GRAPH, [])
        session['track'] = track
        uri = track.track_uri[14:]
        return render_template("base.html", uri=uri)
@views.route('/recomendation')
def rec():
    return render_template('rec.html')
