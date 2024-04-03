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
from typing import TextIO
from classes import Track, WeightedGraph


def _add_tracks_to_graph(g: WeightedGraph, file: TextIO, tracks_to_objects: dict, uris_to_objects: dict) -> None:
    """Read playlist data (JSON file) in file and *mutates* given graph to add vertices and edges
    according to data.

    - Each track in a playlist in our data is a Track object.
    - Each edge indicates that two Tracks appear in the same playlist
    - The edge weight indicates the number of playlists that contain both Tracks
    """

    data = json.load(file)

    # Get playlists in the file
    playlists_data = data['playlists']

    # For each playlist, get the playlist id (pid) and tracks
    for playlist in playlists_data:
        pid = playlist['pid']
        tracks = playlist['tracks']
        tracks_in_playlist_so_far = set()

        # Create Track object for every track in playlist
        for track in tracks:
            # Check if track is already in graph
            if (track['artist_name'], track['track_name']) not in tracks_to_objects:
                uris = [track['track_uri'], track['artist_uri'], track['album_uri']]
                track_obj = Track(track['track_name'], track['artist_name'], track['album_name'], uris)
                tracks_to_objects[(track['artist_name'], track['track_name'])] = track_obj
                uris_to_objects[uris[0]] = track_obj
            else:
                # Track already exists in graph
                track_obj = tracks_to_objects[(track['artist_name'], track['track_name'])]
            # Add current playlist id to track_obj
            track_obj.add_to_playlist(pid)
            # Add Track to graph. NOTE: WeightedGraph.add_vertex handles if a vertex is already in this WeightedGraph.
            g.add_vertex(track_obj)
            # Add edge between track_obj and all tracks in tracks_in_playlists_so_far
            for t in tracks_in_playlist_so_far:
                g.add_edge(track_obj, t)
            # Add Track to tracks_in_playlist_so_far
            tracks_in_playlist_so_far.add(track_obj)


def load_graph(file_names: list[str]) -> tuple[WeightedGraph, dict, dict]:
    """Returns a WeightedGraph that contains all tracks in the file_names' data AND
    a mapping of each track in the data (formatted as (artist_name, track_name) to its respective
    Track object.

    - Each vertex represents a track in our playlist data.
    - A weighted edge between two tracks represents the number of playlists that contain both tracks.
    """
    g = WeightedGraph()

    tracks_to_objects = {}  # Maps tuple ({artist_name}, {track_name}) to corresponding Track object
    uris_to_objects = {}  # Maps track URIs to Track objects

    for file_dir in file_names:
        with open(file_dir) as file:
            _add_tracks_to_graph(g, file, tracks_to_objects, uris_to_objects)

    return g, tracks_to_objects, uris_to_objects


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['json', 'classes'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
