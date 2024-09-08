from models.menu.menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, description,size):
        super().__init__(name, price)
        self.size = size

    def __str__(self) -> str:
        return self._name
    
    def discount(self):
        self._price -= self._price * 0.1