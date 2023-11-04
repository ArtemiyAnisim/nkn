import random


class MusicAlbum:
    def __init__(self, title, artist, release_year, genre, tracklist):
        self.title = title
        self.artist = artist
        self.release_year = release_year
        self.genre = genre
        self.tracklist = tracklist

    def play_track(self, track_number):
        print(f"Воспроизводится трек  {track_number}: {self.tracklist[track_number - 1]}")