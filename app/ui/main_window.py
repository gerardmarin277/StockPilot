from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel, QStackedWidget, QButtonGroup
)
from PySide6.QtCore import Qt

from app.ui.dashboard.dashboard_view import DashboardView
from app.ui.inventory.inventory_view import InventoryView
from app.ui.sales.sales_view import SalesView
from app.ui.purchases.purchases_view import PurchasesView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StockPilot - Business & Inventory Management")
        self.resize(1280, 720)

        # Layout Principal (Horizontal: Sidebar + Contenido)
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 1. Sidebar Lateral
        sidebar = QWidget()
        sidebar.setObjectName("Sidebar")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        sidebar_layout.setSpacing(5)

        # Título / Logo
        app_title = QLabel("📦 StockPilot")
        app_title.setObjectName("SidebarTitle")
        sidebar_layout.addWidget(app_title)

        # Grupo de botones de navegación
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self.btn_dashboard = self._create_nav_button("📊  Dashboard", 0)
        self.btn_inventory = self._create_nav_button("📦  Inventario", 1)
        self.btn_sales = self._create_nav_button("🛒  Ventas", 2)
        self.btn_purchases = self._create_nav_button("🚚  Compras", 3)

        sidebar_layout.addWidget(self.btn_dashboard)
        sidebar_layout.addWidget(self.btn_inventory)
        sidebar_layout.addWidget(self.btn_sales)
        sidebar_layout.addWidget(self.btn_purchases)
        sidebar_layout.addStretch()

        # 2. Área Contenedora Derecha (Header + Vistas)
        right_container = QWidget()
        right_layout = QVBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)

        # Header Superior
        header = QWidget()
        header.setObjectName("Header")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)

        self.header_title = QLabel("Dashboard")
        self.header_title.setObjectName("HeaderTitle")
        user_info = QLabel("👤 Gerard (Admin)")

        header_layout.addWidget(self.header_title)
        header_layout.addStretch()
        header_layout.addWidget(user_info)

        # Vistas Apiladas (QStackedWidget)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setObjectName("ContentArea")

        self.dashboard_view = DashboardView()
        self.inventory_view = InventoryView()
        self.sales_view = SalesView()
        self.purchases_view = PurchasesView()

        self.stacked_widget.addWidget(self.dashboard_view)
        self.stacked_widget.addWidget(self.inventory_view)
        self.stacked_widget.addWidget(self.sales_view)
        self.stacked_widget.addWidget(self.purchases_view)

        right_layout.addWidget(header)
        right_layout.addWidget(self.stacked_widget)

        # Agregar al Layout Principal
        main_layout.addWidget(sidebar)
        main_layout.addWidget(right_container)

        # Seleccionar la vista inicial
        self.btn_dashboard.setChecked(True)

    def _create_nav_button(self, text: str, index: int) -> QPushButton:
        btn = QPushButton(text)
        btn.setCheckable(True)
        self.button_group.addButton(btn, index)
        btn.clicked.connect(lambda: self._switch_view(index, text))
        return btn

    def _switch_view(self, index: int, title: str):
        self.stacked_widget.setCurrentIndex(index)
        clean_title = title.split("  ")[-1]
        self.header_title.setText(clean_title)