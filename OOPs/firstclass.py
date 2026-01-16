class phone:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def show_details(self):
        return f"details of phone"
    
class touchscreen(phone):
    def __init__(self, storage,ram,touch_type):
        super().__init__( storage,ram)
        self.touch_type=touch_type
    def call(self):
        print("making a call using touchscreen phone")
    

p1=phone("Iphone 13",50000)
t1=touchscreen()
print(t1.call())
print(p1.show_details())
print(p1.brand)
print(p1.price)

   