class Restaurant:
    def __init__(self,menu,food_preparation):
        self.menu=menu
        self.food_preparation=food_preparation
    def display_food(self):
        print(self.menu)
        print(self.food_preparation)
        
class Delivery:
    def __init__(self,Name,delivery_add,phone_num,rider_phone):
        self.Name=Name
        self.delivery_add=delivery_add
        self.phone_num=phone_num
        self.rider_phone=rider_phone
    def display_delivery_rider(self):
        print(self.Name)
        print(self.delivery_add)
        print(self.phone_num)
        print(self.rider_phone)

class order(Restaurant,Delivery):
    def __init__(self,menu,food_preparation,Name,delivery_add,phone_num,rider_phone):
        super().__init__(menu,food_preparation)
        Delivery.__init__(self,Name,delivery_add,phone_num,rider_phone)
    def display_food_order(self):
        self.display_food()
        self.display_delivery_rider()
t=order('Indian','spicy','Tharini','ambattur',00000000,123456789)
t.display_food_order()