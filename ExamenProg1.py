from Biblioteca import * 

# Datos iniciales
productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70],  # A
    [80, 55, 45],  # B
    [40, 65, 75]   # C
]
continuar="s"
while continuar=="s":
    pedir_opcion()
    continuar=input("Desea seguir ingresando opciones del menu? s-n: ") 

