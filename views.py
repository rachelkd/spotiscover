from flask import Blueprint, render_template, request
from input import return_random_track
from load_data import load_graph
from track_to_spotify_track import create_track_from_api_response, api_response, get_track_embed_html

PLAYLIST_GRAPH, TRACKS_TO_OBJECTS = load_graph(['data/mpd.slice.0-999.json',
                                                'data/mpd.slice.1000-1999.json',
                                                'data/mpd.slice.2000-2999.json'])

views = Blueprint('views', __name__)
liked_songs_so_far = set() 

@views.route('/', methods=['GET', 'POST'])
def home():
    global liked_songs_so_far  # Declare liked_songs_so_far as global
    global liked_songs_so_far_set
    track = return_random_track(PLAYLIST_GRAPH, [])
    uri = track.track_uri[14:]
    uris = set()
    if request.method == 'POST':
        response = request.form['rdo']
        if response == 'yes':
            liked_songs_so_far.add(track)  
    if len(liked_songs_so_far) >= 3:
        recs = PLAYLIST_GRAPH.get_recommendations(tracks_liked=liked_songs_so_far)
        liked_songs_so_far = set()
        
        for rec in recs:
            u = rec[0].track_uri[14:]
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
        



    

@views.route('/recomendation')
def rec():
    return render_template('rec.html')