def calcular_promedio(lista,valor)->bool: #parametros formales
    '''calcula si el promedio es mayor o menor que el valor'''
    promedio=0
    mayor=False
    for i in range (len(lista)):
        promedio+= lista[i] 
    if promedio>valor:
        mayor=True
    else:
        mayor=False
    return mayor 
        


entrada=[10,20,30,40]
valor=24    
print(calcular_promedio(entrada,valor)) #invocacion a la funcion | parametros actuales
