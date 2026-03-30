from PySide6.QtWidgets import QApplication, QLabel
import sys
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label_1 = QLabel("O meu texto")
    window.v_layout.addWidget(label_1)

    window.show()
    app.exec()