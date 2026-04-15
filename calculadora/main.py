import sys

from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # Cria a aplicação

    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Info
    info = Info("Sua Conta")
    window.addToVlayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText("Digite algo:") # Se quiser colocar um placeholder
    window.addToVlayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.addToVlayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
