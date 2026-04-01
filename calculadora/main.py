from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)
    
    # Executa tudo
    window.show()
    window.adjustFixedSize()
    app.exec()