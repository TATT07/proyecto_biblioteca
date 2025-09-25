class DatabaseStub:
    """Stub que simula base de datos"""

    def libro_disponible(self, libro_id):
        # STUB: Libros con ID par están disponibles
        return libro_id % 2 == 0

    def registrar_prestamo(self, usuario_id, libro_id):
        # STUB: Simula registro exitoso
        # Aquí devolvemos True para simular éxito; también imprimimos para evidencia.
        print(f"[STUB] registrar_prestamo -> User={usuario_id}, Book={libro_id}")
        return True
