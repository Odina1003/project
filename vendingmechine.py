from credit import Credit

class VendingMachine:
    def __init__(self):
        self.a : list[Credit] = []

    def rechargeCard(self, dic):
        if dic in self.a:
            return 'good'
        else:
            return 'no card'
