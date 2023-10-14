from ichimlik import Ichimliklar
from credit import Credit

class VendingMachine:
    def __init__(self):
        self.drinks : list[Ichimliklar] = []
        self._id : list[Credit.id] = []

    def rechargeCard(self, dic):
        if dic in self._id:
            return 'good'
        else:
            return 'no card'
        
    def addBeverange(self, drink, price):
        self.drinks.append(drink, price)
        return "Ichimlik qo'shildi"
    
    def getPrice(self, drink_name: Ichimliklar):
        for ichimlik in self.drinks:
            if ichimlik._nomi == drink_name._nomi:
                return drink_name._narxi
            return '-1.0'

    def getCredit(self, card_id):
        if card_id in self._id:
            return self._id[card_id]
        else:
            return '-1.0'