import threading
import random
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QComboBox, QPushButton, QLabel,
                             QGridLayout, QScrollArea)
from PyQt6.QtCore import pyqtSignal, QObject


class CinemaSignals(QObject):
    update_seats = pyqtSignal()
    log_message = pyqtSignal(str)


class BookingThread(threading.Thread):
    def __init__(self, cinema, title, session_id, seat_index, signals):
        super().__init__()
        self.cinema = cinema
        self.title = title
        self.session_id = session_id
        self.seat_index = seat_index
        self.signals = signals

    def run(self):
        success = self.cinema.book_ticket(self.title, self.session_id, self.seat_index)
        status = "Успешно" if success else "Занято/Ошибка"
        msg = f"Поток {threading.get_ident()}: Место {self.seat_index + 1} -> {status}"
        self.signals.log_message.emit(msg)
        self.signals.update_seats.emit()


class BotSimulationThread(threading.Thread):
    def __init__(self, cinema, title, session_id, count, signals):
        super().__init__()
        self.cinema = cinema
        self.title = title
        self.session_id = session_id
        self.count = count
        self.signals = signals

    def run(self):
        threads = []
        seats_count = len(self.cinema.get_session_data(self.title, self.session_id))

        for _ in range(self.count):
            seat_idx = random.randint(0, seats_count - 1)
            t = BookingThread(self.cinema, self.title, self.session_id, seat_idx, self.signals)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()


class CinemaWindow(QMainWindow):
    def __init__(self, cinema):
        super().__init__()
        self.cinema = cinema
        self.signals = CinemaSignals()
        self.signals.update_seats.connect(self.refresh_grid)
        self.signals.log_message.connect(self.add_log)

        self.setWindowTitle("Система бронирования Кинотеатра")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        controls_layout = QHBoxLayout()
        self.movie_combo = QComboBox()
        self.movie_combo.addItems(list(self.cinema.movies.keys()))
        self.movie_combo.currentTextChanged.connect(self.update_sessions)

        self.session_combo = QComboBox()
        self.session_combo.currentTextChanged.connect(self.refresh_grid)

        self.bot_btn = QPushButton("Запустить 10 ботов (Тест гонки)")
        self.bot_btn.clicked.connect(self.run_bots)

        controls_layout.addWidget(QLabel("Фильм:"))
        controls_layout.addWidget(self.movie_combo)
        controls_layout.addWidget(QLabel("Сеанс:"))
        controls_layout.addWidget(self.session_combo)
        controls_layout.addWidget(self.bot_btn)

        layout.addLayout(controls_layout)

        self.seats_area = QWidget()
        self.seats_grid = QGridLayout()
        self.seats_area.setLayout(self.seats_grid)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.seats_area)
        layout.addWidget(scroll)

        self.log_label = QLabel("Лог операций:")
        layout.addWidget(self.log_label)

        self.update_sessions()

    def update_sessions(self):
        title = self.movie_combo.currentText()
        self.session_combo.clear()
        if title in self.cinema.movies:
            sessions = list(self.cinema.movies[title].sessions.keys())
            self.session_combo.addItems(sessions)
        self.refresh_grid()

    def refresh_grid(self):
        title = self.movie_combo.currentText()
        session_id = self.session_combo.currentText()

        while self.seats_grid.count():
            child = self.seats_grid.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not title or not session_id:
            return

        seats = self.cinema.get_session_data(title, session_id)

        row_len = 10
        for i, is_taken in enumerate(seats):
            btn = QPushButton(str(i + 1))
            if is_taken:
                btn.setStyleSheet("background-color: #ff4d4d; color: white;")
                btn.setEnabled(False)
            else:
                btn.setStyleSheet("background-color: #4dff4d;")
                btn.clicked.connect(lambda checked, idx=i: self.book_seat(idx))

            self.seats_grid.addWidget(btn, i // row_len, i % row_len)

    def book_seat(self, seat_index):
        title = self.movie_combo.currentText()
        session_id = self.session_combo.currentText()
        thread = BookingThread(self.cinema, title, session_id, seat_index, self.signals)
        thread.start()

    def run_bots(self):
        title = self.movie_combo.currentText()
        session_id = self.session_combo.currentText()
        bot_thread = BotSimulationThread(self.cinema, title, session_id, 10, self.signals)
        bot_thread.start()

    def add_log(self, message):
        current_text = self.log_label.text()
        lines = current_text.split('\n')
        if len(lines) > 5:
            lines = lines[-5:]
        self.log_label.setText('\n'.join(lines) + '\n' + message)
