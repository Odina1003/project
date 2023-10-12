class Credit:
    def __init__(self, id, price):
        self._id = id
        self._price = price
    
    def __str__(self):
        return f'{self._id} | {self._price}'
    
    def id(self):
        d = []
        d.append(self._id)