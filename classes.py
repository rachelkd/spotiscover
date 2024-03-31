"""CSC111 Winter 2024 Project 2:
How Do We Create Playlists? An Investigation into Song Recommendations Based on Similarity and Occurrence in Playlists

Module Description
==================
This module contains the classes required for our project.
Classes include:
    - Track, _Vertex, _Graph, _WeightedVertex, WeightedGraph

Copyright and Usage Information
==============================
This file is Copyright (c) 2024 Rachel Deng, Ben Henderson, Jeha Park
"""
from __future__ import annotations
from typing import Any, Union

import networkx as nx


class Track:
    """A track in a playlist.

    Instance Attributes:
        - track_name: The name of this track
        - artist_name: The name of the artist who performed this track.
        - album_name: The name of the album that this track is a part of.
        - playlists: A set of playlists that this track appears in.
                     Playlists will be represented with their unique IDs (integers).
        - track_uri: The Spotify Uniform Resource Indicator of this track.
        - artist_uri: The Spotify Uniform Resource Indicator of this track's artist.
        - album_uri: The Spotify Uniform Resource Indicator of this track's album.

    Representation Invariants:
        - self.track_name != ''
        - self.artist_name != ''
        - self.album_name != ''
        - self.track_uri != ''
        - self.artist_uri != ''
        - self.album_uri != ''
    """
    track_name: str
    artist_name: str
    album_name: str
    playlists: set[int]
    track_uri: str
    artist_uri: str
    album_uri: str

    def __init__(self, track_name: str, artist_name: str, album_name: str, uris: list[str]) -> None:
        """Initialize a new Track with the given track name, artist name, album name,
        and respective Spotify Uniform Resource Indicators (URIs) in the same order.
        """
        self.track_name = track_name
        self.artist_name = artist_name
        self.album_name = album_name
        self.track_uri = uris[0]
        self.artist_uri = uris[1]
        self.album_uri = uris[2]
        self.playlists = set()

    def __str__(self) -> str:
        """Return a string representation of this Track."""
        # return (f'Track(track_name={self.track_name}, '
        #         f'artist_name={self.artist_name}, '
        #         f'album_name={self.album_name}, '
        #         f'track_uri={self.track_uri}, '
        #         f'artist_uri={self.artist_uri}, '
        #         f'album_uri={self.album_uri})')
        return (f'Track(track_name={self.track_name}, '
                f'artist_name={self.artist_name}, '
                f'album_name={self.album_name})')

    def add_to_playlist(self, pid: int) -> None:
        """Adds the given playlist id to this Track's playlists."""
        self.playlists.add(pid)


class _Vertex:
    """A vertex in a book review graph, used to represent a Track.

    Instance Attributes:
        - item: The data stored in this vertex, representing a user or book.
        - neighbours: The vertices that are adjacent to this vertex.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Any
    neighbours: set[_Vertex]

    def __init__(self, item: Any) -> None:
        """Initialize a new vertex with the given item.

        This vertex is initialized with no neighbours.
        """
        self.item = item
        self.neighbours = set()

    def degree(self) -> int:
        """Return the degree of this vertex."""
        return len(self.neighbours)


class Graph:
    """A graph used to represent a playlist network.
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _Vertex object.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item and kind to this graph.

        The new vertex is not adjacent to any other vertices.
        Do nothing if the given item is already in this graph.
        """
        if item not in self._vertices:
            self._vertices[item] = _Vertex(item)

    def add_edge(self, item1: Any, item2: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            v1.neighbours.add(v2)
            v2.neighbours.add(v1)
        else:
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Note that the *items* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return {neighbour.item for neighbour in v.neighbours}
        else:
            raise ValueError

    def get_all_vertices(self) -> set:
        """Return a set of all vertex items in this graph.
        """
        return set(self._vertices.keys())

    def to_networkx(self, max_vertices: int = 5000) -> nx.Graph:
        """Convert this graph into a networkx Graph.

        max_vertices specifies the maximum number of vertices that can appear in the graph.
        (This is necessary to limit the visualization output for large graphs.)
        """
        graph_nx = nx.Graph()
        for v in self._vertices.values():
            graph_nx.add_node(v.item)

            for u in v.neighbours:
                if graph_nx.number_of_nodes() < max_vertices:
                    graph_nx.add_node(u.item)

                if u.item in graph_nx.nodes:
                    graph_nx.add_edge(v.item, u.item)

            if graph_nx.number_of_nodes() >= max_vertices:
                break

        return graph_nx


class _WeightedVertex(_Vertex):
    """A vertex in a weighted playlist graph, used to a represent Track.

    Instance Attributes:
        - item: The data stored in this vertex, representing a user or book.
        - neighbours: The vertices that are adjacent to this vertex, and their corresponding
            edge weights.
        - occurrences: The number of times this Track appears in our playlist graph/network.

    Representation Invariants:
        - self not in self.neighbours
        - all(self in u.neighbours for u in self.neighbours)
    """
    item: Track
    neighbours: dict[_WeightedVertex, int]
    occurrences: int

    def __init__(self, item: Any) -> None:
        """Initialize a new vertex with the given item.

        This vertex is initialized with no neighbours.
        """
        super().__init__(item)
        self.neighbours = {}
        self.occurrences = 1  # By default, a Track appears at least once in our network.

    def __str__(self) -> str:
        """Return a string representation of this vertex."""
        return f'_WeightedVertex(item={self.item}, occurrences={self.occurrences})'

    def sim_score(self, other: _WeightedVertex) -> float:
        """Return the similarity score between this item and the given item.

        The similarity score is calculated by taking the sum of the weights of all neighbours (for BOTH self and other)
        adjacent to BOTH self and other DIVIDED BY the sum of occurences for item1 and item2.
        """
        total_occurrences = self.occurrences + other.occurrences
        neighbours = set(self.neighbours.keys())
        other_neighbours = set(other.neighbours.keys())
        adj_to_both = neighbours.intersection(other_neighbours)

        sum_weights = sum(self.neighbours[v] + other.neighbours[v] for v in adj_to_both)

        return sum_weights / total_occurrences


class WeightedGraph(Graph):
    """A weighted graph used to represent a playlist network that keeps track of Tracks in playlists.

    Instance Attributes:
         - tracks_to_objects:
              A mapping of Tracks in the tuple (<artist_name>, <track_name>) to their
              corresponding Track object
    """
    # Private Instance Attributes:
    #     - _vertices:
    #         A collection of the vertices contained in this graph.
    #         Maps item to _WeightedVertex object.

    _vertices: dict[Any, _WeightedVertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges),
        and an empty mapping from track details to Track objects."""
        self._vertices = {}

        Graph.__init__(self)

    def add_vertex(self, item: Track) -> None:
        """Add a vertex with the given item.

        The new vertex is not adjacent to any other vertices.
        If given item is already in the graph, then increase its occurrences by 1.
        """
        if item not in self._vertices:
            self._vertices[item] = _WeightedVertex(item)
        else:
            track = self._vertices[item]
            track.occurrences += 1

    def add_edge(self, item1: Any, item2: Any, weight: Union[int, float] = 1) -> None:
        """Add an edge between the two vertices with the given items in this graph,
        with the given weight.

        The weight is the number of playlists that item1 and item2 both appear in.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Check if an edge already exists for this graph's edge
            if v2 in v1.neighbours and v1 in v2.neighbours:
                # Add one to the existing weight
                v1.neighbours[v2] += 1
                v2.neighbours[v1] += 1
            else:
                # Add the new edge
                v1.neighbours[v2] = weight
                v2.neighbours[v1] = weight
        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    # def get_track_object(self, track_tup: tuple[str, str]) -> Track:
    #     """Return the Track corresponding to the given track tuple.
    #
    #     Raise ValueError if given track tuple is not a key in self.tracks_to_objects.
    #
    #     Track tuple is formatted as such:
    #         - (<artist_name>, <track_name>)
    #     """
    #     if track_tup not in self.tracks_to_objects:
    #         raise ValueError(f'{track_tup} does not appear in this graph.')
    #
    #     return self.tracks_to_objects[track_tup]

    def get_occurrences(self, item: Any) -> int:
        """Return the number of times the given item appears in the playlists in this graph.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item not in self._vertices:
            raise ValueError(f'{item} does not appear in this graph.')

        vertex = self._vertices[item]
        return vertex.occurrences

    def get_weight(self, item1: Any, item2: Any) -> int:
        """Return the weight of the edge between the given items.

        Return 0 if item1 and item2 are not adjacent.

        Raise ValueError if item1 and item2 are not in this graph.
        """
        if item1 not in self._vertices:
            raise ValueError(f'{item1} is not an item in this graph.')
        if item2 not in self._vertices:
            raise ValueError(f'{item2} is not an item in this graph.')

        v1 = self._vertices[item1]
        v2 = self._vertices[item2]
        return v1.neighbours.get(v2, 0)

    # TODO: Delete below if not needed
    # def average_weight(self, item: Any) -> float:
    #     """Return the average weight of the edges adjacent to the vertex corresponding to item.
    #
    #     Raise ValueError if item does not corresponding to a vertex in the graph.
    #     """
    #     if item in self._vertices:
    #         v = self._vertices[item]
    #         return sum(v.neighbours.values()) / len(v.neighbours)
    #     else:
    #         raise ValueError

    def sim_score(self, item1: Any, item2: Any) -> float:
        """Return the similarity score between two items in this graph.

        The similarity score is calculated by taking the sum of the weights of all neighbours adjacent to BOTH item1
        and item2 DIVIDED BY the sum of occurences for item1 and item2.

        If item1 or item2 is not in this graph, then raise a ValueError.
        """
        if item1 not in self._vertices:
            raise ValueError(f'{item1} is not in this graph.')
        if item2 not in self._vertices:
            raise ValueError(f'{item2} is not in this graph.')

        v1 = self._vertices[item1]
        v2 = self._vertices[item2]

        assert v1.sim_score(v2) == v2.sim_score(v1)

        return v1.sim_score(v2)

    def get_recommendations(self, tracks_liked: set[Track], recc_limit: int = 10, occur_limit: int = 30) \
            -> list[tuple[Track, float]]:
        """Return a list of <recc_limit> Tracks recommended based off of given track_liked.
        For each track liked, similarity scores are calculated. The tracks recommended are the tracks with
        the highest SUM of similarity across the rated tracks. Recommended tracks DO NOT include tracks liked.
        Ties are broken by descending alphabetical order.

        To make "independent" and/or less popular artists become discovered, recommendations DO NOT include
        Tracks with more than <occur_limit> occurrences in this graph.

        Preconditions:
            - track_ratings != {}
            - all(track in self._vertices for track in track_ratings)
        """
        similarity = {}  # Maps Tracks to similarity score

        for track in tracks_liked:
            for neighbour in self._vertices[track].neighbours:
                # Check if neighbour is a valid song to recommend
                if neighbour not in tracks_liked and neighbour.occurrences <= occur_limit:
                    sim_score = self.sim_score(track, neighbour.item)
                    similarity[neighbour.item] = similarity.get(track, 0) + sim_score

        assert similarity != {}

        top_similarity_scores = [(t, similarity[t]) for t in similarity]
        top_similarity_scores.sort(key=lambda x: (x[1], x[0].track_name), reverse=True)

        return top_similarity_scores[:recc_limit]

    def to_networkx(self, max_vertices: int = 5000) -> nx.Graph:
        """Convert this graph into a networkx Graph.

        max_vertices specifies the maximum number of vertices that can appear in the graph.
        (This is necessary to limit the visualization output for large graphs.)

        Note that this method is provided for you, and you shouldn't change it.
        """
        graph_nx = nx.Graph()
        for v in self._vertices.values():
            graph_nx.add_node(v.item)

            for u in v.neighbours.keys():
                if graph_nx.number_of_nodes() < max_vertices:
                    graph_nx.add_node(u.item)

                if u.item in graph_nx.nodes:
                    graph_nx.add_edge(v.item, u.item, weight=v.neighbours[u])

            if graph_nx.number_of_nodes() >= max_vertices:
                break

        return graph_nx


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['networkx'],  # the names (strs) of imported modules
        'allowed-io': ['print', 'open', 'input'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
