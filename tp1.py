"""
TP 1 - Algoritmos de Colocacion

Integrantes:
    Emanuel Stradella <e.stradella94@outlook.com>
    Juilo Aguilar <julioaguilar-ap@outlook.com>
    Antonela Orellano <anto_orellano09@hotmail.com>
"""

import doctest


def primer_ajuste(memoria, procesos):
    """Primer Ajuste

    >>> primer_ajuste([], [])
    ([], [])

    >>> primer_ajuste([], [[1, 5]])
    ([], [1])

    >>> primer_ajuste([[10, None]], [[1, 5]])
    ([[10, 1]], [])

    >>> primer_ajuste([[15, None], [5, None], [30, None]], \
                      [[1, 10], [2, 3], [3, 45]])
    ([[15, 1], [5, 2], [30, None]], [3])

    >>> primer_ajuste([], [[1, 5], [2, 3]])
    ([], [1, 2])
    """

    no_colocados = []   # Procesos que no se pudieron colocar en la memoria

    for proc in procesos:
        exito = False
        
        for part in memoria:
            if part[1] == None and part[0] >= proc[1]:
                part[1] = proc[0]
                exito = True
                break

        if not exito:
            no_colocados.append(proc[0])

    return memoria, no_colocados


def peor_ajuste(memoria, procesos):
    """Peor Ajuste

    >>> peor_ajuste([], [])
    ([], [])

    >>> peor_ajuste([], [[1, 5]])
    ([], [1])

    >>> peor_ajuste([[15, None], [10, None], [20, None]], \
                    [[1, 10], [2, 10], [3, 3]])
    ([[15, 2], [10, 3], [20, 1]], [])

    >>> peor_ajuste([[15, None], [10, None], [20, None]], \
                    [[1, 15], [2, 23], [3, 1]])
    ([[15, 3], [10, None], [20, 1]], [2])

    >>> peor_ajuste([[10, None], [11, None], [5, None]], \
                    [[1, 15], [2, 1], [3, 2]])
    ([[10, 3], [11, 2], [5, None]], [1])
    """

    no_colocados = []   # Procesos que no se pudieron colocar en la memoria

    for proc in procesos:
        exito = False
        mayor_desperdicio = None # Posición de la partición que produce mayor
                                 # desperdicio.
        
        for part in memoria:
            if part[1] == None and part[0] >= proc[1]:
                if mayor_desperdicio == None:
                    mayor_desperdicio = memoria.index(part)
                elif part[0] - proc[1] > memoria[mayor_desperdicio][0] - proc[1]:
                    mayor_desperdicio = memoria.index(part)

                exito = True

        if exito:
            memoria[mayor_desperdicio][1] = proc[0]
        else:
            no_colocados.append(proc[0])

    return memoria, no_colocados


def mejor_ajuste(memoria, procesos):
    """Mejor Ajuste

    >>> mejor_ajuste([], [])
    ([], [])

    >>> mejor_ajuste([], [[1, 5]])
    ([], [1])

    >>> mejor_ajuste([[15, None], [10, None], [20, None]], \
                     [[1, 10], [2, 10], [3, 3]])
    ([[15, 2], [10, 1], [20, 3]], [])

    >>> mejor_ajuste([[15, None], [10, None], [20, None]], \
                     [[1, 15], [2, 23], [3, 1]])
    ([[15, 1], [10, 3], [20, None]], [2])

    >>> mejor_ajuste([[10, None], [11, None], [5, None]], \
                     [[1, 15], [2, 1], [3, 2]])
    ([[10, 3], [11, None], [5, 2]], [1])
    """

    no_colocados = []   # Procesos que no se pudieron colocar en la memoria

    for proc in procesos:
        exito = False
        menor_desperdicio = None # Posición de la partición que produce menor
                                 # desperdicio.
        
        for part in memoria:
            if part[1] == None and part[0] >= proc[1]:
                if menor_desperdicio == None:
                    menor_desperdicio = memoria.index(part)
                elif part[0] - proc[1] < memoria[menor_desperdicio][0] - proc[1]:
                    menor_desperdicio = memoria.index(part)

                exito = True

        if exito:
            memoria[menor_desperdicio][1] = proc[0]
        else:
            no_colocados.append(proc[0])

    return memoria, no_colocados


def combinar(memoria):
    """Combinar los bloques libres adyacentes en la memoria

    >>> combinar([])
    []

    >>> combinar([[10, 1], [5, None], [3, None], [10, 2]])
    [[10, 1], [8, None], [10, 2]]

    >>> combinar([[10, 1], [5, None], [3, None], [10, 2], [10, None]])
    [[10, 1], [8, None], [10, 2], [10, None]]

    >>> combinar([[7, None], [10, 1], [5, None], [3, None], [10, 2], [10, None]])
    [[7, None], [10, 1], [8, None], [10, 2], [10, None]]
    """

    antLibre = False
    antEspacio = 0

    for part in memoria[:]:
        if antLibre and part[1] == None:
            part[0] += antEspacio
            del memoria[memoria.index(part) - 1]

        if part[1] == None:
            antLibre = True
        else:
            antLibre = False

        antEspacio = part[0]

    return memoria


def compactar(memoria):
    """Compactar los bloques libres al final de la memoria

    >>> compactar([])
    []

    >>> compactar([[10, 1], [5, None], [3, None], [10, 2]])
    [[10, 1], [10, 2], [8, None]]

    >>> compactar([[10, 1], [5, None], [3, None], [10, 2], [10, None]])
    [[10, 1], [10, 2], [18, None]]

    >>> compactar([[7, None], [10, 1], [5, None], [3, None], [10, 2], [10, None]])
    [[10, 1], [10, 2], [25, None]]
    """

    encontrado = False
    partAux = [0, None]
    nuevoEsp = 0

    for part in memoria[:]:
        if part[1] == None:
            encontrado = True
            nuevoEsp += part[0]
            del memoria[memoria.index(part)]

    if encontrado:
        partAux[0] = nuevoEsp
        memoria.append(partAux)

    return memoria


if __name__ == "__main__":
    doctest.testmod(verbose=True)
