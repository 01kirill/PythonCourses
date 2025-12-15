import sys
from PyQt6.QtWidgets import QApplication
from model import Cinema
from gui import CinemaWindow


def init_data():
    cinema = Cinema()

    cinema.add_movie("Inception")
    cinema.add_session_to_movie("Inception", "10:00", 50)
    cinema.add_session_to_movie("Inception", "14:00", 50)

    cinema.add_movie("Interstellar")
    cinema.add_session_to_movie("Interstellar", "18:00", 60)

    return cinema


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cinema_data = init_data()
    window = CinemaWindow(cinema_data)
    window.show()
    sys.exit(app.exec())
