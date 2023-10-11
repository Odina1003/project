from ichimlik import Ichimliklar
from yangi_ichimlik import VendingMachine

ichimlik1 = Ichimliklar('Coca cola', 3200)
ichimlik2 = Ichimliklar('Suv', 1000)
ichimlik3 = Ichimliklar('Pepsi', 2500)

print(ichimlik1._nomi, ichimlik1._narxi)
a = VendingMachine()
print(a.addBeverange('Fanta', 2000))
print(a.getPrice('Fanta'))
