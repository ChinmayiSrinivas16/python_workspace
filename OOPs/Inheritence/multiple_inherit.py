class Calling:
    def feature1(self):
        print("Calling feature")


# Parent class 2
class Camera:
    def feature2(self):
        print("Camera feature")


# Child class (Multiple Inheritance)
class SmartPhone(Calling, Camera):
    def explore(self):
        print("Exploring features of SmartPhone")