import sys 
from pathlib import Path
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow

def load_stylesheet(app: QApplication):
    style_path = Path(__file__).parent / "ui" / "styles" / "main.qss"

    if style_path.exists():
        with open(style_path, "r", encoding="utf-8") as f:
            app.setStyleSheet(f.read())



def main():
    app = QApplication(sys.argv)

    # Cargar estilos QSS
    load_stylesheet(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()