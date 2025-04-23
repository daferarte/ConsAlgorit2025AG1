import pytest
from Juego import Juego, Categoria

@pytest.fixture
def juego_rompecabezas():
    return Juego(
        nombre="Sudoku Pro",
        categoria=Categoria.ROMPECABEZAS,
        precio=5000,
        tamanio=2048,
        cantidad_licencias=10,
        ruta_imagen="imagenes/sudoku.png"
    )

@pytest.fixture
def juego_deporte():
    return Juego(
        nombre="Fútbol Extremo",
        categoria=Categoria.DEPORTE,
        precio=7000,
        tamanio=4096,
        cantidad_licencias=15,
        ruta_imagen="imagenes/futbol.png"
    )

@pytest.fixture
def juego_accion():
    return Juego(
        nombre="Galaxy Wars",
        categoria=Categoria.ACCION,
        precio=10000,
        tamanio=8192,
        cantidad_licencias=5,
        ruta_imagen="imagenes/accion.png"
    )

def test_creacion_valida(juego_rompecabezas):
    assert juego_rompecabezas.dar_nombre() == "Sudoku Pro"
    assert juego_rompecabezas.dar_categoria() == Categoria.ROMPECABEZAS
    assert juego_rompecabezas.dar_precio() == 5000
    assert juego_rompecabezas.dar_tamanio() == 2048
    assert juego_rompecabezas.dar_cantidad_licencias() == 10
    assert juego_rompecabezas.dar_cantidad_vendidas() == 0
    assert juego_rompecabezas.dar_ruta_imagen() == "imagenes/sudoku.png"

def test_comprar_licencias(juego_rompecabezas):
    juego_rompecabezas.comprar_licencias(5)
    assert juego_rompecabezas.dar_cantidad_licencias() == 15

def test_vender_licencias_exitoso(juego_rompecabezas):
    assert juego_rompecabezas.vender_licencias(5) is True
    assert juego_rompecabezas.dar_cantidad_licencias() == 5
    assert juego_rompecabezas.dar_cantidad_vendidas() == 5

def test_vender_licencias_fallido(juego_rompecabezas):
    assert juego_rompecabezas.vender_licencias(15) is False
    assert juego_rompecabezas.dar_cantidad_licencias() == 10
    assert juego_rompecabezas.dar_cantidad_vendidas() == 0

def test_creacion_invalida_nombre_vacio():
    with pytest.raises(AssertionError):
        Juego("", Categoria.ACCION, 1000, 500, 5, "img.png")

def test_creacion_invalida_precio_negativo():
    with pytest.raises(AssertionError):
        Juego("Juego X", Categoria.ACCION, -100, 500, 5, "img.png")

def test_creacion_invalida_tamanio_0():
    with pytest.raises(AssertionError):
        Juego("Juego X", Categoria.ACCION, 1000, 0, 5, "img.png")

def test_comprar_licencias_cantidad_negativa(juego_rompecabezas):
    with pytest.raises(AssertionError):
        juego_rompecabezas.comprar_licencias(-2)

def test_vender_licencias_cantidad_negativa(juego_rompecabezas):
    with pytest.raises(AssertionError):
        juego_rompecabezas.vender_licencias(-3)

def test_categoria_deporte(juego_deporte):
    assert juego_deporte.dar_nombre() == "Fútbol Extremo"
    assert juego_deporte.dar_categoria() == Categoria.DEPORTE
    assert juego_deporte.vender_licencias(10) is True
    assert juego_deporte.dar_cantidad_vendidas() == 10

def test_categoria_accion(juego_accion):
    assert juego_accion.dar_nombre() == "Galaxy Wars"
    assert juego_accion.dar_categoria() == Categoria.ACCION
    juego_accion.comprar_licencias(5)
    assert juego_accion.dar_cantidad_licencias() == 10

def test_vender_todas_licencias(juego_rompecabezas):
    cantidad_total = juego_rompecabezas.dar_cantidad_licencias()
    assert juego_rompecabezas.vender_licencias(cantidad_total)
    assert juego_rompecabezas.dar_cantidad_licencias() == 0
    assert juego_rompecabezas.dar_cantidad_vendidas() == cantidad_total

def test_vender_cero_licencias(juego_rompecabezas):
    with pytest.raises(AssertionError):
        juego_rompecabezas.vender_licencias(0)

def test_comprar_cero_licencias(juego_rompecabezas):
    with pytest.raises(AssertionError):
        juego_rompecabezas.comprar_licencias(0)

def test_multiples_operaciones(juego_deporte):
    juego_deporte.vender_licencias(5)
    juego_deporte.comprar_licencias(3)
    juego_deporte.vender_licencias(4)
    assert juego_deporte.dar_cantidad_licencias() == 9  # 15 - 5 + 3 - 4
    assert juego_deporte.dar_cantidad_vendidas() == 9

def test_nombre_y_ruta_largos():
    nombre = "Super Ultra Mega Hiper Juego de Aventura Legendaria 2025 Edición Épica" * 2
    ruta = "/imagenes/juegos/aventuras/ultra/mega/legendaria/epica/2025.png" * 2
    juego = Juego(nombre, Categoria.ACCION, 5000, 1000, 1, ruta)
    assert juego.dar_nombre() == nombre
    assert juego.dar_ruta_imagen() == ruta

def test_creacion_invalida_ruta_imagen_vacia():
    with pytest.raises(AssertionError):
        Juego("Nombre válido", Categoria.ROMPECABEZAS, 1000, 500, 5, "")

def test_todas_las_categorias_creables():
    for categoria in Categoria:
        juego = Juego(f"Juego {categoria.name}", categoria, 1000, 500, 5, "imagen.png")
        assert juego.dar_categoria() == categoria