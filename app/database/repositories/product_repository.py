from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.database.models import Product, Category


class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, product_id: int) -> Optional[Product]:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def get_by_sku(self, sku: str) -> Optional[Product]:
        return self.db.query(Product).filter(Product.sku == sku).first()

    def get_all(self) -> List[Product]:
        return self.db.query(Product).all()

    def get_low_stock_products(self) -> List[Product]:
        return(
            self.db.query(Product)
            .filter(Product.stock <= Product.min_stock)
            .all()
        )

    def create(self, product: Product) -> Product:
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def update(self, product: Product) -> Product:
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product_id: int) -> bool:
        product = self.get_by_id(product_id)
        if product:
            self.db.delete(product)
            self.db.commit()
            return True
        return False

    def get_inventory_summary_sql(self) -> dict:
        """Ejemplo de consulta SQL pura para obtener agregados de negocio."""
        sql = text("""
            SELECT 
                COUNT(id) AS total_products,
                SUM(stock) AS total_stock_units,
                SUM(stock * cost_price) AS total_inventory_value
            FROM products
        """)
        result = self.db.execute(sql).fetchone()
        return {
            "total_products": result.total_products or 0,
            "total_stock_units": result.total_stock_units or 0,
            "total_inventory_value": round(result.total_inventory_value or 0.0, 2)
        }