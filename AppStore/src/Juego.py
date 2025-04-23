from enum import Enum

class Categoria(Enum):
    ROMPECABEZAS = "Rompecabezas"
    DEPORTE = "Deporte"
    ACCION = "Acción"

class Juego:
    def __init__(self, nombre: str, categoria: Categoria, precio: int, tamanio: int, cantidad_licencias: int, ruta_imagen: str):
        assert nombre, "El nombre no puede ser vacío"
        assert categoria in Categoria, "Categoría inválida"
        assert precio > 0, "El precio debe ser mayor a 0"
        assert tamanio > 0, "El tamaño debe ser mayor a 0"
        assert cantidad_licencias >= 0, "Las licencias no pueden ser negativas"
        assert ruta_imagen, "La ruta de la imagen no puede ser vacía"

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.tamanio = tamanio
        self.cantidad_licencias = cantidad_licencias
        self.cantidad_vendidas = 0
        self.ruta_imagen = ruta_imagen

    def dar_nombre(self) -> str:
        return self.nombre

    def dar_categoria(self) -> Categoria:
        return self.categoria

    def dar_precio(self) -> int:
        return self.precio

    def dar_tamanio(self) -> int:
        return self.tamanio

    def dar_cantidad_licencias(self) -> int:
        return self.cantidad_licencias

    def dar_cantidad_vendidas(self) -> int:
        return self.cantidad_vendidas

    def dar_ruta_imagen(self) -> str:
        return self.ruta_imagen

    def comprar_licencias(self, cantidad: int):
        assert cantidad > 0, "La cantidad debe ser mayor que 0"
        self.cantidad_licencias += cantidad

    def vender_licencias(self, cantidad: int) -> bool:
        assert cantidad > 0, "La cantidad debe ser mayor que 0"
        if self.cantidad_licencias >= cantidad:
            self.cantidad_licencias -= cantidad
            self.cantidad_vendidas += cantidad
            return True
        return False
