from app.database.connection import engine, Base, SessionLocal
from app.database.models import Role, User, Category, Product, Supplier
from app.domain.enums import RoleName
import bcrypt


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def init_database():
    print("🔨 Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # 1. Crear Roles si no existen
        roles_data = [
            (RoleName.ADMIN, "Administrador con acceso total"),
            (RoleName.MANAGER, "Gestor de inventario y ventas"),
            (RoleName.EMPLOYEE, "Empleado para registro de ventas")
        ]

        for role_name, desc in roles_data:
            existing_role = db.query(Role).filter_by(name=role_name).first()
            if not existing_role:
                db.add(Role(name=role_name, description=desc))

        db.commit()

        # 2. Crear Usuario Admin por defecto
        admin_role = db.query(Role).filter_by(name=RoleName.ADMIN).first()
        admin_user = db.query(User).filter_by(username="admin").first()

        if not admin_user and admin_role:
            db.add(User(
                username="admin",
                email="admin@stockpilot.com",
                password_hash=hash_password("admin123"),
                is_active=True,
                role_id=admin_role.id
            ))
            db.commit()
            print("👤 Usuario 'admin' creado (Contraseña: admin123).")

        # 3. Categorías iniciales de prueba
        if db.query(Category).count() == 0:
            categories = [
                Category(name="Ropa & Calzado", description="Textil y calzado deportivo/casual"),
                Category(name="Electrónica", description="Gadgets, cables y componentes"),
                Category(name="Oficina", description="Material de escritorio y papelería")
            ]
            db.add_all(categories)
            db.commit()
            print("🏷️ Categorías iniciales añadidas.")

        # 4. Proveedor inicial de prueba
        if db.query(Supplier).count() == 0:
            supplier = Supplier(
                name="Textil SL",
                contact_name="Carlos Gómez",
                email="contacto@textilsl.com",
                phone="+34 600 112 233",
                address="Polígono Industrial Norte, Calle A #12"
            )
            db.add(supplier)
            db.commit()
            print("🏭 Proveedor de prueba añadido.")

        # 5. Productos iniciales de prueba
        if db.query(Product).count() == 0:
            ropa_cat = db.query(Category).filter_by(name="Ropa & Calzado").first()
            elec_cat = db.query(Category).filter_by(name="Electrónica").first()

            products = [
                Product(
                    sku="CAM-001",
                    name="Camiseta Algodón Negra",
                    description="Camiseta básica 100% algodón",
                    price=24.99,
                    cost_price=12.50,
                    stock=45,
                    min_stock=15,
                    category_id=ropa_cat.id if ropa_cat else None
                ),
                Product(
                    sku="ZAP-002",
                    name="Zapatillas Deportivas",
                    description="Calzado deportivo transpirable",
                    price=59.99,
                    cost_price=30.00,
                    stock=8,
                    min_stock=10,  # En stock crítico para probar alertas
                    category_id=ropa_cat.id if ropa_cat else None
                ),
                Product(
                    sku="AUR-003",
                    name="Auriculares Inalámbricos",
                    description="Auriculares Bluetooth con cancelación de ruido",
                    price=79.99,
                    cost_price=45.00,
                    stock=20,
                    min_stock=5,
                    category_id=elec_cat.id if elec_cat else None
                )
            ]
            db.add_all(products)
            db.commit()
            print("📦 Productos iniciales añadidos.")

        print("✅ Base de datos inicializada correctamente.")

    except Exception as e:
        db.rollback()
        print(f"❌ Error al inicializar la base de datos: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    init_database()