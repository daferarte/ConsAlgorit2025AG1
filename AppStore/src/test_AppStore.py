import pytest
from appstore import AppStore
from Juego import Juego, Categoria


@pytest.fixture
def appstore():
    return AppStore()


def test_dar_juego(appstore):
    assert appstore.darJuego1().dar_nombre() == "Candy Crush"
    assert appstore.darJuego2().dar_nombre() == "Flow"
    assert appstore.darJuego3().dar_nombre() == "FIFA"
    assert appstore.darJuego4().dar_nombre() == "Clash of Clans"


def test_buscar_juego_existente(appstore):
    juego = appstore.buscarJuego("Flow")
    assert juego is not None
    assert juego.dar_nombre() == "Flow"


def test_buscar_juego_inexistente(appstore):
    juego = appstore.buscarJuego("Among Us")
    assert juego is None


def test_vender_licencias_insuficientes(appstore):
    resultado = appstore.venderLicenciasJuego("Flow", 1000)
    assert resultado is False


def test_calcular_venta_con_descuento_rompecabezas(appstore):
    mensaje = appstore.calcularVentaPorVolumen(20, 10, 0, 0)
    assert "descuento sería de" in mensaje
    assert "El precio con descuento" in mensaje


def test_calcular_venta_con_descuento_deporte_y_accion(appstore):
    mensaje = appstore.calcularVentaPorVolumen(0, 0, 20, 12)
    assert "descuento sería de" in mensaje
    assert "El precio con descuento" in mensaje


def test_calcular_venta_sin_descuento(appstore):
    mensaje = appstore.calcularVentaPorVolumen(1, 1, 1, 1)
    assert "descuento sería de: $0" in mensaje
