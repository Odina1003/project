from ichimlik import Ichimliklar

class VendingMachine:
    def __init__(self):
        self.drinks : list[Ichimliklar] = []

    def addBeverange(self, drink, price):
        self.drinks.append(drink, price)
        return "Ichimlik qo'shildi"
    
    def getPrice(self, drink_name: Ichimliklar):
        for ichimlik in self.drinks:
            if ichimlik._nomi == drink_name._nomi:
                return drink_name._narxi
            return '-1.0'