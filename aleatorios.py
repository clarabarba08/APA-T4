''''
    T4 - Generació de números aleatoris fetn servir l'algoritme LGC
    Clara Barba Armengol
'''
import doctest
class Aleat:
    """
    Classe iterable Aleat : implementa un generador de números aleatoros en el rang 0 <= xn < m fent servir el mètode LGC
    Arguments de la funció: mòdul (m), multiplicador (a), increment (c) i valor inicial (x0)
    Proves unitàrias classe Aleat: 

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15


    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, m=2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.xn = x0
    
    def __iter__(self) :
        """
        Per tal que els objectes de la classe siguin iterables.
        """
        self.xn = self.x0
        return self
    
    def __next__(self):
        """
        Efectua la generació en sí mateixa y retrona el número aleatori següent
        """
        self.xn = ((self.a * self.xn) + self.c) % self.m
        return self.xn
    
    def __call__(self,x0):
        """
        Per reiniciar la secuencia amb el valor inicial indicat en el seu únic argument 
        """
        self.xn = x0


def aleat (m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Funció aleat implementa el mateix generador de números aleatoris que en l'exercici anterior en el rang 0 <= xn < m
    Pel reinici de send() --> Interrupción yeld --> per enviar valors externs a la funció durant l'execució

    Arguments de la funció: mòdul (m), multiplicador (a), increment (c) i valor inicial (x0)

    Proves unitàries de aleat: 
    - Comprovació del funcionament:

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    - Comprovació del reinici:

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    xn = x0
    while True:
        xn = ((a * xn) + c) % m
        send = (yield xn)
        if send: xn = send

doctest.testmod()


    




