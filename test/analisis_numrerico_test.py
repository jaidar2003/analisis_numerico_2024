from proyect.analisis_numerico import MinimosCuadrados

class TestMinimosCuadrados:
    def test_ingresar_datos(self):
        mc = MinimosCuadrados()
        mc.ingresar_datos()
        assert mc.x is not None
        assert mc.y is not None

    def test_ajuste_lineal(self):
        mc = MinimosCuadrados()
        mc.x = [1, 2, 3, 4, 5]
        mc.y = [2, 3, 4, 5, 6]
        mc.ajuste_lineal()
        assert mc.x is not None
        assert mc.y is not None
        assert mc.x == [1, 2, 3, 4, 5]
        assert mc.y == [2, 3, 4, 5, 6]
