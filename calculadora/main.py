import sys

from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    # Info
    info = Info("2.0 ^ 10.0 = 1024")
    window.addToVlayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText("Digite algo:") # Se quiser colocar um placeholder
    window.addToVlayout(display)

    # Executa tudo
    window.show()
    window.adjustFixedSize()
    app.exec()
