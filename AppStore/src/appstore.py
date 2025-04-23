from Juego import Juego, Categoria


class AppStore:
    
    CANT_MIN_ROMPECABEZAS = 25
    CANT_MIN_DEPORTE = 20
    CANT_MIN_ACCION = 12
    DESCUENTO_1 = 0.20
    DESCUENTO_2 = 0.15

    def __init__(self):
        self.juego1 = Juego("Candy Crush", Categoria.ROMPECABEZAS, 3000, 300, 50, "CandyCrush.jpg")
        self.juego2 = Juego("Flow", Categoria.ROMPECABEZAS, 5500, 250, 15, "Flow.jpg")
        self.juego3 = Juego("FIFA", Categoria.DEPORTE, 7500, 850, 80, "FIFA.jpg")
        self.juego4 = Juego("Clash of Clans", Categoria.ACCION, 2000, 1000, 36, "ClashOfClans.jpg")

    def darJuego1(self):
        return self.juego1

    def darJuego2(self):
        return self.juego2

    def darJuego3(self):
        return self.juego3

    def darJuego4(self):
        return self.juego4

    def buscarJuego(self, nombre):
        if nombre == self.juego1.dar_nombre():
            return self.juego1
        elif nombre == self.juego2.dar_nombre():
            return self.juego2
        elif nombre == self.juego3.dar_nombre():
            return self.juego3
        elif nombre == self.juego4.dar_nombre():
            return self.juego4
        return None

    def venderLicenciasJuego(self, nombre, cantidad):
        juego = self.buscarJuego(nombre)
        if juego:
            return juego.vender_licencias(cantidad)
        return False

    def comprarLicenciasJuego(self, nombre, cantidad):
        juego = self.buscarJuego(nombre)
        if juego:
            juego.comprar_licencias(cantidad)

    def darJuegoMasVendido(self):
        mas_vendido = "Ninguno"
        cantidad_mas_vendida = 0

        if self.juego1.dar_cantidad_vendidas() > cantidad_mas_vendida:
            mas_vendido = self.juego1.dar_nombre()
            cantidad_mas_vendida = self.juego1.dar_cantidad_vendidas()

        if self.juego2.dar_cantidad_vendidas() > cantidad_mas_vendida:
            mas_vendido = self.juego2.darNombre()
            cantidad_mas_vendida = self.juego2.dar_cantidad_vendidas()

        if self.juego3.dar_cantidad_vendidas() > cantidad_mas_vendida:
            mas_vendido = self.juego3.darNombre()
            cantidad_mas_vendida = self.juego3.dar_cantidad_vendidas()

        if self.juego4.dar_cantidad_vendidas() > cantidad_mas_vendida:
            mas_vendido = self.juego4.darNombre()
            cantidad_mas_vendida = self.juego4.dar_cantidad_vendidas()

        return mas_vendido

    def calcularVentaPorVolumen(self, c1, c2, c3, c4):
        cant_rompecab = 0
        cant_deporte = 0
        cant_accion = 0

        if self.juego1.dar_categoria() == Categoria.ROMPECABEZAS:
            cant_rompecab += c1
        elif self.juego1.dar_categoria() == Categoria.DEPORTE:
            cant_deporte += c1
        elif self.juego1.dar_categoria() == Categoria.ACCION:
            cant_accion += c1

        if self.juego2.dar_categoria() == Categoria.ROMPECABEZAS:
            cant_rompecab += c2
        elif self.juego2.dar_categoria() == Categoria.DEPORTE:
            cant_deporte += c2
        elif self.juego2.dar_categoria() == Categoria.ACCION:
            cant_accion += c2

        if self.juego3.dar_categoria() == Categoria.ROMPECABEZAS:
            cant_rompecab += c3
        elif self.juego3.dar_categoria() == Categoria.DEPORTE:
            cant_deporte += c3
        elif self.juego3.dar_categoria() == Categoria.ACCION:
            cant_accion += c3

        if self.juego4.dar_categoria() == Categoria.ROMPECABEZAS:
            cant_rompecab += c4
        elif self.juego4.dar_categoria() == Categoria.DEPORTE:
            cant_deporte += c4
        elif self.juego4.dar_categoria() == Categoria.ACCION:
            cant_accion += c4

        total_venta = (
            self.juego1.dar_precio() * c1 +
            self.juego2.dar_precio() * c2 +
            self.juego3.dar_precio() * c3 +
            self.juego4.dar_precio() * c4
        )

        descuento = 0

        if cant_rompecab >= AppStore.CANT_MIN_ROMPECABEZAS:
            descuento = total_venta * AppStore.DESCUENTO_1
        elif cant_deporte >= AppStore.CANT_MIN_DEPORTE and cant_accion >= AppStore.CANT_MIN_ACCION:
            descuento = total_venta * AppStore.DESCUENTO_2

        total_con_descuento = total_venta - descuento

        mensaje = (
            f"El precio total de la venta sería: ${total_venta}.\n"
            f"El descuento sería de: ${descuento}\n"
            f"El precio con descuento sería: ${total_con_descuento}."
        )
        return mensaje

    def metodo1(self):
        return "Respuesta 1"

    def metodo2(self):
        return "Respuesta 2"