import math 
def promedio(x):
    '''Funcion que retorna el promedio de cierta cantidad de datos
    Entrada
    -------
    x : lista de datos

    Salida
    ------
    prom : suma de todos los numeros dividida en su cantidad
    '''
    x_nan = [valor for valor in x if not math.isnan(valor)]
    if len(x_nan) == 0:
        return 0
    suma = sum(x_nan)
    prom = suma / len(x_nan)
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

def mediana(x):
    '''Funcion que retorna la mediana de una lista de numeros
    Entrada
    -------
    n : ordena la lista

    Salida
    ------
    mediana : identifica si la cantidad de numeros es par o impar y retorna su mediana
    '''
    x.sort()
    n = len(x)
    
    if n % 2 != 0:
        median = x[(n + 1) // 2]
    else:
        median = (x[(n // 2) - 1] + x[n // 2]) / 2
    return median
def rango(x):
    ''' Función que retorna el rango de una serie de datos

    Entrada
    -------
    lista de datos

    Salida
    -------
    rango
    '''
    rango = max(x)- min(x)

    return rango

def varianza(x):
    '''
    Función que calcula la varianza de una serie de datos

    Entrada
    -------
    lista de datos

    Salida
    ------
    var: calcula la varianza dividiendo la suma de los cuadrados de las diferencias por el numero de datos
    '''
    x_nan = [valor for valor in x if not math.isnan(valor)]
    m = promedio(x_nan)
    n = len(x_nan)
    var = 0
    for k in range(n):
        var += ((x_nan[k] - m) **2) / n
    return var
def cuartiles(x):
    '''Funcion que calcula los cuartiles de una serie de datos

    Entrada
    -------
    lista de datos
    
    Salida
    ------
    Q1, Q2, Q3 : retorna los cuartiles
    '''
    datos2 = sorted(x)
    b = len(datos2)
    if b % 4== 0:
        medio = b // 2
        Q1 = (datos2[:medio])[len(datos2[:medio]) // 2]
        Q3 = (datos2[medio:])[len(datos2[medio:]) // 2]
    else:
        medio = b // 2
        Q1 = datos2[:medio][len(datos2[:medio]) // 2]
        Q3 = datos2[medio+1:][len(datos2[medio+1:]) // 2]

    Q2 = mediana(datos2)
    return Q1, Q2, Q3
def rango_intercuartil(x):
    '''Funcion que calcula el rango intercuartil de ciera cantidad de datos
    Entrada
    -------
    x : datos

    Salida
    ------
    rangint : resta de Q1 - Q3
    '''
    Q1, Q2, Q3 = cuartiles(x)
    rangint = Q3 - Q1

    return rangint

def mad(x):
    '''Funcion que calcula la desviación mediana absoluta
    Entrada
    -------
    x : lista de datos

    Salida
    ------
    dma : calcula la mediana, su desviación absoluta y luego la mediana de su desviacion absoluta
    '''
    x_nan = [valor for valor in x if not math.isnan(valor)]
    median = mediana(x)
    desviaciones_absolutas = [abs(n - median) for n in x]
    dma = mediana(desviaciones_absolutas)                           
                                
    return dma
def desviacion_estandar(x):
    '''Funcion que calcula la desviacion estandar de cierta cantidad de datos
    Entrada
    -------
    x : lista de datos

    Salida:
    -------
    desv : retorna la desviación estándar
    '''
    x_nan = [valor for valor in x if not math.isnan(valor)]
    vari = varianza(x_nan)
    desv = math.sqrt(vari)

    return desv
def percentil(x, per):
    '''Funcion que calcula el percentil de una lista de datos
    Entrada
    -------
    x : lista de datos
    per : percentil que se desa calcular (1-100)

    Salida
    ------
    EL percentil calculado
    '''
    datos = sorted(x)
    n = len(datos)

    if n == 0:
        return None

    k = (per / 100) * (n - 1)
    f = math.floor(k)
    c = math.ceil(k)

    if f == c:
        return datos[int(k)]
    d = datos[f] * (c - k)
    d1 = datos[c] * (k - f)
    return d + d1




