class Ichimliklar:

    def __init__(self, nomi, narxi):
        self._nomi = nomi
        self._narxi =  narxi

    @property
    def nomi(self):
        return self._nomi

    @property
    def narxi(self):
        return self._narxi

    def __str__(self):
        return f'{self.nomi} | {self.narxi}'