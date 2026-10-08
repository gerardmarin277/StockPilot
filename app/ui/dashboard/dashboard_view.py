from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt


class DashboardView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel("📊 Panel de Control (Dashboard)")
        label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1e293b;")
        label.setAlignment(Qt.AlignCenter)

        layout.addWidget(label)