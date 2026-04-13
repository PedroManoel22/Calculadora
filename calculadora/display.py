from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN


class Display(QLineEdit):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]

        self.setStyleSheet(f"font-size: {BIG_FONT_SIZE}px;")  # Tamanho da fonte
        self.setMinimumHeight(BIG_FONT_SIZE * 2)  # Altura mínima
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)  # Alinhado a direita
        self.setTextMargins(*margins)
