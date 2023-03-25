from models.celular import Celular
from models.computador import Computador
from models.classes import Abacate, Laranja
def celular():
    celular = Celular("Motorola", "g2" , "1200")
    celular2 = Celular("Sansung", "s10" , "1500")
    celular3 = Celular("apple", "x10" , "1500")

    print(celular.valor,celular.modelo,celular.marca)
    print(celular2.valor,celular2.modelo,celular2.marca)
    print(celular3.valor,celular3.modelo,celular3.marca)



def computador():
    computador = Computador("Nokia", "s20", "4000")
    computador2 = Computador("Samsung", "g10", "2000")
    computador3 = Computador("Apple", "macbook", "10000")
    computador4 = Computador("Lenovo", "m14221", "10")
    computador5 = Computador("acer","acer", "5000")
                             

    print(computador.valor,computador.modelo,computador.marca)
    print(computador2.valor,computador2.modelo,computador2.marca)
    print(computador3.valor,computador3.modelo,computador3.marca)
    print(computador4.valor,computador4.modelo,computador4.marca)
    print(computador5.valor,computador5.modelo,computador5.marca)

def abacate():
    abacate = Abacate("breda", "200gr", "4")
    abacate1 = Abacate("Fortuna ", "300gr", "10")
    abacate2 = Abacate("Geada", "400gr", "20")
    abacate3 = Abacate("Margarida", "500gr", "30")

    print(abacate.valor,abacate.peso,abacate.valor)
    print(abacate1.valor,abacate1.peso,abacate1.valor)
    print(abacate2.valor,abacate2.peso,abacate2.valor)
    print(abacate3.valor,abacate3.peso,abacate3.valor)

def laranja():
    laranja = Laranja("Pera", "10gr", "40")
    laranja1 = Laranja("Lima", "50gr", "20")
    laranja2 = Laranja("natal", "1kg", "254")
    laranja3 = Laranja("Baía", "2kg", "500")

    print(laranja.valor,laranja.peso,laranja.valor)
    print(laranja1.valor,laranja1.peso,laranja1.valor)
    print(laranja2.valor,laranja2.peso,laranja2.valor)
    print(laranja3.valor,laranja3.peso,laranja3.valor)


laranja()

abacate()