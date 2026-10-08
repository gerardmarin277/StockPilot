from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class PurchasesView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        label = QLabel("🚚 Órdenes de Compra y Proveedores")
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e293b;")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)