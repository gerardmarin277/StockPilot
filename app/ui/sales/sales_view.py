from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class SalesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        label = QLabel("🛒 Punto de Ventas (Sales)")
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e293b;")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)