from Juego import Juego, Categoria


class AppStore:
    
    CANT_MIN_ROMPECABEZAS = 25
    CANT_MIN_DEPORTE = 20
    CANT_MIN_ACCION = 12
    DESCUENTO_1 = 0.20
    DESCUENTO_2 = 0.15

    def __init__(self):
        self.juego1 = Juego("Candy Crush", Categoria.ROMPECABEZAS, 3000, 300, 50, "img.png")
        self.juego2 = Juego("Flow", Categoria.ROMPECABEZAS, 5500, 250, 15, "Flow.png")
        self.juego3 = Juego("FIFA", Categoria.DEPORTE, 7500, 850, 36, "fifa.png")
        self.juego4 = Juego("Clash of clans", Categoria.ACCION, 2000, 1000, 36, "class.png")
        
    def darJuego1(self):
        return self.juego1

    def darJuego2(self):
        return self.juego2

    def darJuego3(self):
        return self.juego3

    def darJuego4(self):
        return self.juego4

    def buscarJuego(self, nombre):
        assert nombre, "El nombre no puede ser vacio"
        
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
        assert nombre, "El nombre no puede ser vacio"
        assert cantidad > 0, "La cantidad debe ser mayor que cero"
        
        juego = self.buscarJuego(nombre)
        if juego:
            return juego.vender_licencias(cantidad)
        return False
        

    def comprarLicenciasJuego(self, nombre, cantidad):
        assert nombre, "El nombre no puede ser vacio"
        assert cantidad > 0, "La cantidad debe ser mayor que cero"
        juego = self.buscarJuego(nombre)
        if juego:
            juego.comprar_licencias(cantidad)
        
        

    def darJuegoMasVendido(self):
        mas_vendido = "Ninguno"
        cantidad_mas_vendido=0
        
        if self.juego1.dar_cantidad_vendidas() > cantidad_mas_vendido:
            mas_vendido = self.juego1.dar_nombre()
            cantidad_mas_vendido = self.juego1.dar_cantidad_vendidas()
        
        if self.juego2.dar_cantidad_vendidas() > cantidad_mas_vendido:
            mas_vendido = self.juego2.dar_nombre()
            cantidad_mas_vendido = self.juego2.dar_cantidad_vendidas()
        
        if self.juego3.dar_cantidad_vendidas() > cantidad_mas_vendido:
            mas_vendido = self.juego3.dar_nombre()
            cantidad_mas_vendido = self.juego3.dar_cantidad_vendidas()
        
        if self.juego4.dar_cantidad_vendidas() > cantidad_mas_vendido:
            mas_vendido = self.juego4.dar_nombre()
            cantidad_mas_vendido = self.juego4.dar_cantidad_vendidas()
        
        return mas_vendido
        

    def calcularVentaPorVolumen(self, c1, c2, c3, c4):
        

    def metodo1(self):
        

    def metodo2(self):
        