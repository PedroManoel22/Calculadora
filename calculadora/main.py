from PySide6.QtWidgets import QApplication
import sys
from main_window import MainWindow
from display import Display
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

    # Display
    display = Display()
    # display.setPlaceholderText("Digite algo:") # Se quiser colocar um placeholder
    window.addWidgetToVLayout(display)
   
    
    
    # Executa tudo
    window.show()
    window.adjustFixedSize()
    app.exec()