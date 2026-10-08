from enum import Enum

class RoleName(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"


class MovementType(str, Enum):
    PURCHASE = "PURCHASE"      # Entrada por compra
    SALE = "SALE"              # Salida por venta
    ADJUSTMENT = "ADJUSTMENT"  # Ajuste manual de inventario
    RETURN = "RETURN"          # Devolución


class PurchaseStatus(str, Enum):
    PENDING = "PENDING"
    ORDERED = "ORDERED"
    PARTIALLY_RECEIVED = "PARTIALLY_RECEIVED"
    RECEIVED = "RECEIVED"
    CANCELLED = "CANCELLED"


class SaleStatus(str, Enum):
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"