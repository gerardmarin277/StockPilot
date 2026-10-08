class DomainException(Exception):
    pass


class InsufficientStockException(DomainException):
    def __init__(self, product_name: str, available: int, requested: int):
        super().__init__(
            f"Stock insuficiente para '{product_name}'. Disponible: {available}, Solicitado: {requested}"
        )


class EntityNotFoundException(DomainException):
    def __init__(self, entity_name: str, identifier: str | int):
        super().__init__(f"{entity_name} con identificador '{identifier}' no fue encontrado.")


class InvalidOperationException(DomainException):
    pass