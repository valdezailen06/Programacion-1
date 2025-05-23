 #mostrar menu 
def validar_opcion(numero:int,desde:int,hasta:int)->int:
    '''Valida que el numero ingresado por el usuario pertenezca al rango dado'''
    while numero < desde or numero > hasta:
        print ("ERROR. Esta fuera de rango.") 
        numero=int(input(f"Seleccione una opcion ({desde}-{hasta}): "))    
    return numero 

def pedir_opcion ():
    ''' Pide al usuario que ingrese una opcion del menu'''
    print ("--- MENU DE OPCIONES ---\n1. Mostrar productos y ventas.\n2. Ordenar productos por ventas anuales.\n3. Buscar producto por nombre.\n4. Buscar monto de venta en la matriz.\n5. Salir")
    opcion=int(input("Selecciona una opcionn(1-5): "))
    opcion= validar_opcion(opcion,1,5)
    match opcion:
        case 1:
            mostrar_productosventas (productos,ventas)
        case 2:
            ordenar_por_total(productos,ventas)
        case 3:
            buscar_producto (productos,ventas)
        case 4:
            buscar_valor_en_matriz (productos,ventas)
        case _:
            print("Salir")
    
    

#mostrar matriz
def mostrar_productosventas (produ:list,ventas:list)-> any:
    '''Muestra la lista de productos, las ventas trimestrales y el total anual'''
    print("Ventas trimestrales (en miles de $)\nProducto | T1 | T2 | T3 | Total\n----------------------------------")
    for i in range (len(ventas)):
        total= ventas[i][0] + ventas[i][1] + ventas[i][2]
        print(f"   {produ[i]}     | {ventas[i][0]} | {ventas[i][1]} | {ventas[i][2]} | {total}") 

#Ordenar por ventas totales anuales
def ordenar_por_total(productos:list, ventas:list):
    '''Ordena los productos de forma descendente segun la ventas totales anuales'''
    for i in range(len(productos)-1):
        for j in range((len(productos)) - 1 - i):
            total_actual = ventas[j][0] + ventas[j][1] + ventas[j][2] 
            total_siguiente = ventas[j+1][0] + ventas[j+1][1] + ventas[j+1][2]
            
            if (total_siguiente > total_actual) or (total_siguiente == total_actual and productos[j+1] > productos[j]):
                #intercambio ventas
                aux_ventas = ventas[j]
                ventas[j] = ventas[j+1]
                ventas[j+1] = aux_ventas
                #intercambiao productos
                aux_producto = productos[j]
                productos[j] = productos[j+1]
                productos[j+1] = aux_producto
    for i in range(len(productos)):
        total = ventas[i][0] + ventas[i][1] + ventas[i][2]
        print(f"   {productos[i]}     | {ventas[i][0]} | {ventas[i][1]} | {ventas[i][2]} | {total}")
        
#buscar producto por nombre y mostrar sus ventas 
def validar_producto (ingreso:str)->str:
     '''Valida que lo ingresado por el usuario coincida con las opciones dadas'''
     while ingreso!="A" and ingreso!="B" and ingreso!="C":
          print("ERROR. Fuera de las opciones.")
          ingreso=input("Ingrese nombre dentro de las opciones (A-B-C): ")
     return ingreso 

def buscar_producto(product:list,ventas:list):
    '''Busca el producto por nombre y mustra sus ventas'''
    nombre=input("Ingrese nombre del producto (A-B-C): ")
    nombre = validar_producto(nombre)
    for i in range (len(product)):
        if product[i]==nombre:
              for j in range (len(ventas[i])):
                   print(ventas[i][j], end=" ")
              print()

#Buscar valor en matriz 
def buscar_valor_en_matriz(productos:list, ventas:list):
    '''Busca un valor dentro de la matriz y mustra a que producto y trimestre pertenece'''
    trimestre=["T1", "T2", "T3"]
    valor=int(input("Ingrese un valor:"))
    pertenece = False
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == valor:
                print(f"{valor} pertenece al Producto {productos[i]} y Trimestre {trimestre[j]}  ")
                pertenece = True
    if pertenece == False:
        print("Ese valor no pertenece a ningun producto.") 

productos = ["A", "B", "C"]
ventas = [
    [50, 60, 70],  # A
    [80, 55, 45],  # B
    [40, 65, 75]   # C
]
