from typing import Any

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(
        self, /, parent: QWidget | None = None, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando o layout básico
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Título da janela
        self.setWindowTitle("Calculadora mil grau")

    def adjustFixedSize(self):
        # Última coisa a ser feita
        self.adjustSize()  # Ajusta o tamanho da tabela caso o conteúdo seja maior
        self.setFixedSize(
            self.width(), self.height()
        )  # Colocando um tamanho fixo para a janela

    def addToVlayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
        # self.adjustFixedSize()
