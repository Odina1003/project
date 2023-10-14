class Credit:
    def __init__(self, id, price):
        self._id = id
        self._price = price
    
    @property
    def id(self):
        return self._id

    @property 
    def price(self):
        return self._price
    
    def __str__(self):
        return f'{self._id} | {self._price}'