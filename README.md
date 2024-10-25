# Spotify Song Recommendation System

A Python-based song recommendation system that analyzes playlist data to suggest new tracks based on user preferences. The system uses a weighted graph algorithm to find relationships between songs that appear in the same playlists.

## Features

-   Interactive web interface built with Flask and Tailwind CSS
-   Song preview functionality using Spotify's embedded player
-   Recommendation algorithm based on playlist co-occurrence and similarity scoring
-   Focus on promoting less mainstream tracks to help surface emerging artists

## Prerequisites

-   Python 3.11 or higher
-   Flask
-   Required Python packages (see `requirements.txt`)

## Installation

1. Clone this repository

```bash
git clone <repository-url>
cd spotify-recommendation-system
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages

```bash
pip install -r requirements.txt
```

4. Download the dataset from the [Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)

5. Extract the downloaded data and place the following files in a `data` folder in the project root:
    - mpd.slice.0-999.json
    - mpd.slice.1000-1999.json
    - mpd.slice.2000-2999.json

## Running the Application

1. From the project root directory, run:

```bash
python main.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. If port 5000 is in use, modify the port in `main.py`:

```python
if __name__ == '__main__':
    APP.run(debug=True, port=8080)  # or any other available port
```

## Usage

1. The application will present you with songs one at a time
2. For each song:
    - Preview the track using the embedded Spotify player
    - Click "Yes" or "No" to indicate if you like the song
    - Click "Submit" to record your choice
    - Wait a few seconds between submissions to avoid timeout errors
3. After liking three songs, you'll be redirected to a page showing personalized recommendations

## Technical Details

The recommendation system uses a weighted graph structure where:

-   Vertices represent tracks
-   Edges represent co-occurrence in playlists
-   Edge weights indicate the number of shared playlists
-   Similarity scores are calculated based on shared neighbors and occurrence frequency

For implementation details, see:

```python
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
        adjacent to BOTH self and other DIVIDED BY the sum of occurrences for item1 and item2.
        """
        total_occurrences = self.occurrences + other.occurrences
        neighbours = set(self.neighbours.keys())
        other_neighbours = set(other.neighbours.keys())
        adj_to_both = neighbours.intersection(other_neighbours)

        sum_weights = sum(self.neighbours[v] + other.neighbours[v] for v in adj_to_both)

        return sum_weights / (total_occurrences ** 2)
```

## Project Structure

-   `main.py`: Application entry point
-   `init.py`: Flask app configuration
-   `views.py`: Route handlers and application logic
-   `classes.py`: Core data structures and algorithms
-   `load_data.py`: Dataset parsing and graph construction
-   `input.py`: User input handling
-   `templates/`: HTML templates
-   `static/`: CSS and other static assets

## Authors

-   Rachel Deng
-   Ben Henderson
-   Jeha Park

## Dataset Citation

[C.W. Chen, P. Lamere, M. Schedl, and H. Zamani. Recsys Challenge 2018: Automatic Music Playlist Continuation. In Proceedings of the 12th ACM Conference on Recommender Systems (RecSys ’18), 2018.](https://dl.acm.org/doi/abs/10.1145/3240323.3240342)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
