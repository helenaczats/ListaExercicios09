import pytest
from area.area import area_quadrado, area_retangulo, area_triangulo
from utils.utils import ler_csv

def test_area_quadrado():
    
    lado = 3
    resultado_esperado = 9
    resultado_obtido = area_quadrado(lado)
    assert resultado_esperado == resultado_obtido

def test_area_retangulo():
    
    base = 5
    altura = 10
    resultado_esperado = 50
    
    resultado_obtido = area_retangulo(base, altura)
    
    assert resultado_esperado == resultado_obtido
    
def test_area_triangulo():
    
    base = 10
    altura = 6
    resultado_esperado = 30
    
    resultado_obtido = area_triangulo(base, altura)
    
    assert resultado_esperado == resultado_obtido
    


@pytest.mark.parametrize("base, altura, resultado_esperado",
                         [ 
                            (3,6,18), 
                            (2,5,10),
                            (10,20,200),
                            (8,16,128),
                            (58,76,4408),
                         ]
                        )    

def test_area_retangulo_param(base,altura, resultado_esperado):
    resultado_obtido = area_retangulo(base,altura)
    assert resultado_esperado == resultado_obtido
    



@pytest.mark.parametrize("base, altura, resultado_esperado",
                         ler_csv("./fixtures/massa_triangulo.csv")
                         )
    
def test_area_triangulo_csv(base, altura, resultado_esperado):
    resultado_obtido = area_triangulo(int(base), int(altura))
    assert int(resultado_esperado) == int(resultado_obtido)
    