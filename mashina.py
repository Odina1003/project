class Ustunlar:
    def __init__(self, qator, name, soni):
        self._ustun = list[Ustunlar] = [i for i in range(1, 5)]
        self._qator = qator
        self._name = name
        self._soni = soni

    def rellifColumn(self):
        for i in self._ustun:
            ls = list[self._qator, self._name, self._soni]
        if self._name in ls:
            return f'{self._qator}, {self._name}, {self._soni}'
        
    def availableCans(self, ichilik_nomi):
        if ichilik_nomi in self._name:
            return self._soni

