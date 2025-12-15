import threading
import time
import random

class Session:
    def __init__(self, session_id, total_seats):
        self.session_id = session_id
        self.total_seats = total_seats
        self.seats = [False] * total_seats
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def book_seat(self, seat_index):
        with self.condition:
            if 0 <= seat_index < self.total_seats:
                if not self.seats[seat_index]:
                    time.sleep(random.uniform(0.1, 0.3))
                    self.seats[seat_index] = True
                    self.condition.notify_all()
                    return True
            return False

    def get_seats_status(self):
        with self.lock:
            return list(self.seats)

class Movie:
    def __init__(self, title):
        self.title = title
        self.sessions = {}

    def add_session(self, session_id, total_seats):
        self.sessions[session_id] = Session(session_id, total_seats)

class Cinema:
    def __init__(self):
        self.movies = {}
        self.global_semaphore = threading.Semaphore(5)

    def add_movie(self, title):
        if title not in self.movies:
            self.movies[title] = Movie(title)

    def add_session_to_movie(self, title, session_id, total_seats):
        if title in self.movies:
            self.movies[title].add_session(session_id, total_seats)

    def book_ticket(self, title, session_id, seat_index):
        with self.global_semaphore:
            if title in self.movies:
                movie = self.movies[title]
                if session_id in movie.sessions:
                    session = movie.sessions[session_id]
                    return session.book_seat(seat_index)
        return False

    def get_session_data(self, title, session_id):
        if title in self.movies:
            movie = self.movies[title]
            if session_id in movie.sessions:
                return movie.sessions[session_id].get_seats_status()
        return []
