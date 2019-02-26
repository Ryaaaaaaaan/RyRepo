class ComboOrder:
    def __init__(self,burger="cheese",drink="cola",chips="medium"):
        self.burger= burger
        self.drink = drink
        self.chips = chips
    def order(self):
        print("Drink: {}".format(self.drink))
        print("Chips: {}".format(self.chips))    
        print("Burger: {}".format(self.burger))
        
        
order1 = ComboOrder("cheese", "cola")
order2 = ComboOrder("lamb", "lemonade", "large")
order1.order()
order2.order()