import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QMenu
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt
from functools import partial


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 200)

        # Создание виджетов для логина
        self.label_username = QLabel("Username:")
        self.label_username.setStyleSheet("color: white; font-size: 16px;")  # Стиль текста
        self.input_username = QLineEdit()
        self.input_username.setStyleSheet("background-color: white; color: black; padding: 5px; font-size: 14px;")

        self.label_password = QLabel("Password:")
        self.label_password.setStyleSheet("color: white; font-size: 16px;")
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_password.setStyleSheet("background-color: white; color: black; padding: 5px; font-size: 14px;")

        self.button_login = QPushButton("Login")
        self.button_login.setStyleSheet(
            "background-color: #4CAF50; color: white; font-size: 14px; padding: 8px; border-radius: 5px;"
        )
        self.button_login.clicked.connect(self.check_credentials)

        # Настройка компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)

        # Установка стиля фона окна авторизации
        self.setStyleSheet("background-color: #2C3E50;")  # Темный фон
        self.setLayout(layout)

    def check_credentials(self):
        # Проверка учетных данных
        username = self.input_username.text()
        password = self.input_password.text()

        if username == "user" and password == "password":  # Замените на реальную проверку
            self.open_profile()
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def open_profile(self):
        # Переход к профилю пользователя
        self.hide()
        self.profile_window = ProfileWindow()
        self.profile_window.show()


class ProfileWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Profile")
        self.setGeometry(300, 300, 400, 400)

        # Создание виджета приветствия
        self.label_welcome = QLabel("Welcome to your profile!")
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_welcome.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")

        # Добавление изображения как отдельного виджета
        self.image_label = QLabel()
        pixmap = QPixmap("photo.jpg")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Создание и настройка компоновки
        layout = QVBoxLayout()
        layout.addWidget(self.label_welcome)
        layout.addWidget(self.image_label)  # Добавляем изображение как виджет

        self.button_menu = QPushButton("Menu")
        self.button_menu.setStyleSheet(
            "background-color: green; color: white; font-size: 14px; padding: 8px; border-radius: 5px;"
        )
        self.button_menu.clicked.connect(self.open_menu)
        layout.addWidget(self.button_menu)

        self.setLayout(layout)

    def open_menu(self):
        # Переход к меню
        self.hide()
        self.menu_window = MenuWindow()
        self.menu_window.show()




class MenuWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu")
        self.setGeometry(300, 300, 400, 400)

        # Приветственное сообщение в верхней части экрана
        self.label_welcome = QLabel("Welcome to menu!")
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.label_welcome.setStyleSheet("color: white; font-size: 18px; font-weight: bold; margin-top: 10px;")
        self.setStyleSheet(
            f"background-image: url({'menu_photo.jpg'}); background-repeat: no-repeat; background-position: center; background-size: cover;"
        )
        # Создание кнопок для позиций меню
        self.menu_items = ["Пицца", "Суши", "Паста", "Салат"]
        self.buttons = []

        # Основной вертикальный компоновщик
        layout = QVBoxLayout()
        layout.addWidget(self.label_welcome)

        # Добавление кнопок меню
        for item in self.menu_items:
            button = QPushButton(item)
            button.setStyleSheet(
                "background-color: black; color: white; font-size: 14px; padding: 8px; margin-top: 5px;"
            )
            button.clicked.connect(partial(self.show_selection, item))  # Передаём параметр item через partial
            self.buttons.append(button)
            layout.addWidget(button)

        self.setLayout(layout)

    def show_selection(self, item):
        # Отображение окна с сообщением при выборе блюда
        QMessageBox.information(self, "Выбор блюда", f"Вы выбрали: {item}")



def main():
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
