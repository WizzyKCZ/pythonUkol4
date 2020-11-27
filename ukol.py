import random

class ukol:
    hopsa = 'goblin'
    golo = 'molo'

    def __init__(self, k, z, o):
        self.k = k
        self.z = z
        self.o = o

    def __str__(self):
        return f'({self.k}, {self.z}, {self.o})'

    def __eq__(self, other):
        return self.k == other.k and self.z == other.z and self.o == other.o

    def __gt__(self, other):
        return self.k > other.k and self.z > other.z and self.o > other.o

    def __add__(self, other):
        return self.k + other.k, self.z + other.z, self.o + other.o

    def __sub__(self, other):
        return self.k - other.k, self.z - other.z, self.o - other.o

    @staticmethod
    def rng():
        return random.randint(0, 100)

    @classmethod
    def migrena(cls):
        return cls(0, 0)

    def golok(self):
        print(self.k)

    def goloz(self):
        print(self.z)



class ukolDedicnost(ukol):
    def __init__(self, k, z, o):
        # Metoda super() zpřístupňuje atributy a metody předka - v tomto případě konstruktor
        super().__init__(k, z, o)

    def __str__(self):
        return f'({self.k}, {self.z}, {self.o})'