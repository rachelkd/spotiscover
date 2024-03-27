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
from typing import Optional, TextIO, Union
from classes import Track, WeightedGraph

TRACKS_TO_OBJECTS = {}  # Maps tuple ({artist_name}, {track_name}) to corresponding Track object


def _add_tracks_to_graph(g: WeightedGraph, file: TextIO) -> None:
    """Read playlist data (JSON file) in file and *mutates* given graph to add vertices and edges
    according to data.

    - Each track in a playlist in our data is a Track object.
    - Each edge indicates that two Tracks appear in the same playlist
    - The edge weight indicates the number of playlists that contain both Tracks
    """

    # Read line by line
    # while ...
    #   Get playlist id
    #   Get track info
    #   Create new track object if not in TRACKS_TO_OBJECTS
    #   Map track to Track object
    #   Add to graph g
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
            track_name = track['track_name']
            artist_name = track['artist_name']

            # Check if track is already in graph
            track_tup = (artist_name, track_name)
            if track_tup not in TRACKS_TO_OBJECTS:
                album_name = track['album_name']
                track_uri, artist_uri, album_uri = track['track_uri'], track['artist_uri'], track['album_uri']
                track_obj = Track(track_name, artist_name, album_name,
                                  track_uri, artist_uri, album_uri)
                TRACKS_TO_OBJECTS[(artist_name, track_name)] = track_obj
            else:
                # Track already exists in graph
                track_obj = TRACKS_TO_OBJECTS[(artist_name, track_name)]
            # Add current playlist id to track_obj
            track_obj.add_to_playlist(pid)
            # Add Track to graph. NOTE: WeightedGraph.add_vertex handles if a vertex is already in this WeightedGraph.
            g.add_vertex(track_obj)
            # Add edge between track_obj and all tracks in tracks_in_playlists_so_far
            for t in tracks_in_playlist_so_far:
                g.add_edge(track_obj, t)
            # Add Track to tracks_in_playlist_so_far
            tracks_in_playlist_so_far.add(track_obj)


def load_graph(file_names: list[str]) -> WeightedGraph:
    """Returns a WeightedGraph that contains all tracks in the file_names' data.

    - Each vertex represents a track in our playlist data.
    - A weighted edge between two tracks represents the number of playlists that contain both tracks.
    """
    g = WeightedGraph()

    for file_dir in file_names:
        with open(file_dir) as file:
            _add_tracks_to_graph(g, file)

    return g


if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['json', 'classes'],  # the names (strs) of imported modules
    #     'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })
    pass
