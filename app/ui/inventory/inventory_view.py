from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class InventoryView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        label = QLabel("📦 Gestión de Inventario y Productos")
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e293b;")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)