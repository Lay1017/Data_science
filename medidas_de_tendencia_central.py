import math 
def promedio(n):
    '''Funcion que retorna el promedio de cierta cantidad de datos
    Entrada
    -------
    x : lista de datos

    Salida
    ------
    prom : suma de todos los numeros dividida en su cantidad
    '''
    if len(n) == 0:
        return 0
    suma = sum(n)
    prom = suma / len(n)
    return prom

def moda(x):
    '''FUncion que retorna la moda de cierta cantidad de datos
    Entrada
    -------
    x : lista de datos

    Salida
    ------
    moda : str
    '''
    categorias = []
    for i in x:
        if i not in categorias:
            categorias.append(i)
    cuentas = []
    for c in categorias:
        n = 0
        for val in x:
            if val == c:
                n = n+1
        cuentas.append(n)
    i_max = 0
    val_max = cuentas[0]
    for m in range(1, len(cuentas)):
        if cuentas[m] > val_max:
            i_max = m
            val_max = cuentas[m]
    moda = categorias[i_max]
    return moda

def mediana(numeros):
    '''Funcion que retorna la mediana de una lista de numeros
    Entrada
    -------
    n : ordena la lista

    Salida
    ------
    mediana : identifica si la cantidad de numeros es par o impar y retorna su mediana
    '''
    lista = sorted(numeros)
    n = len(lista)
    
    if n % 2 == 1:
        median = lista[n // 2]
    else:
        median = (lista[(n // 2) - 1] + lista[n // 2]) / 2
    return median
def rango(lista):
    ''' Función que retorna el rango de una serie de datos

    Entrada
    -------
    lista de datos

    Salida
    -------
    rango
    '''
    rango = max(lista)- min(lista)

    return rango

def varianza(lista):
    '''
    Función que calcula la varianza de una serie de datos

    Entrada
    -------
    lista de datos

    Salida
    ------
    var: calcula la varianza dividiendo la suma de los cuadrados de las diferencias por el numero de datos
    '''
    media = sum(lista) / len(lista)
    suma = sum((x - media) ** 2 for x in lista)
    var = suma / len(lista)
    return var
def cuartiles(datos):
    '''Funcion que calcula los cuartiles de una serie de datos

    Entrada
    -------
    lista de datos
    
    Salida
    ------
    Q1, Q2, Q3 : retorna los cuartiles
    '''
    datos2 = sorted(datos)
    b = len(datos2)
    if b % 4 == 0:
        medio = b // 2
        Q1 = (datos2[:medio])[len(datos2[:medio]) // 2]
        Q3 = (datos2[medio:])[len(datos2[medio:]) // 2]
    else:
        medio = b // 2
        Q1 = datos2[:medio][len(datos2[:medio]) // 2]
        Q3 = datos2[medio+1:][len(datos2[medio+1:]) // 2]

    Q2 = mediana(datos2)
    return Q1, Q2, Q3
def rango_intercuartil(r):
    '''Funcion que calcula el rango intercuartil de ciera cantidad de datos
    Entrada
    -------
    r : datos

    Salida
    ------
    rangint : resta de Q1 - Q3
    '''
    Q1, Q2, Q3 = cuartiles(datos)
    rangint = Q3 - Q1

    return rangint

def mad(datos):
    '''Funcion que calcula la desviación mediana absoluta
    Entrada
    -------
    datos: lista de datos

    Salida
    ------
    dma : calcula la mediana, su desviación absoluta y luego la mediana de su desviacion absoluta
    '''
    median = mediana(numeros)
    desviaciones_absolutas = [abs(x - median) for x in datos]
    dma = mediana(numeros)(desviaciones_absolutas)                           
                                
    return dma
def desviacion_estandar(datos):
    '''Funcion que calcula la desviacion estandar de cierta cantidad de datos
    Entrada
    -------
    datos : lista de datos

    Salida:
    -------
    desv : retorna la desviación estándar
    '''
    vari = varianza(lista)
    desv = math.sqrt(varianza)

    return desv


