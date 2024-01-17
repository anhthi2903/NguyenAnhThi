# class Dog:
#     DogCount=0
#     def _init_(self,name,size,age,color):
#         self.name = name
#         self.size = size
#         self.age = age
#         self.color = color
#     def Go(self):
#         print("I'm going...")
#     def Stay(self,place):
#         print("I'm staying at {}".format(place))
#     def Lie(self, place):
#         print("I'm lying at {}".format(place))
#     def Bark(self):
#         print("Whoop...")
#     def Eat(self,food):
#         print("I'm eating {}".format(food))
# bull = Dog("Bull","large",2,"Yellow")
# bull.Stay("garden")
# bull.Bark()


class Dog:
    # Thuộc tính của lớp
    DogCount = 0

    def __init__(self, name, size, age, color):
        # Hàm khởi tạo đối tượng
        self.name = name  # Thuộc tính của đối tượng
        self.size = size  # Thuộc tính của đối tượng
        self.age = age    # Thuộc tính của đối tượng
        self.color = color  # Thuộc tính của đối tượng

    def Go(self):
        print("I'm going...")

    def Stay(self, place):
        print("I'm staying at {}".format(place))

    def Lie(self, place):
        print("I'm lying at {}".format(place))

    def Bark(self):
        print("Whoop...")

    def Eat(self, food):
        print("I'm eating {}".format(food))

# Khởi tạo đối tượng
bull = Dog("Bull", "large", 2, "Yellow")
bull.Stay("garden")
bull.Bark()  # Removed the space between bull.Bark()
