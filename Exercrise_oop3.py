class Car():
    def __init__(self,color,door):
        self.color = color
        self.door = door

    def run(self):
        print(f'您的車子顏色為{self.color}')

class Toyota(Car):
    # pass
    def __init__(self,color,door):
        super().__init__(color,door)
        self.brand = 'Toyota'
        # super().run()

class Tesla(Car):
    # pass
    def __init__(self,color,door):
        super().__init__(color,door)
        self.brand = 'Tesla'
        # super().run()

c1 = Toyota('White',4)
print(c1.__dict__)

c2 = Tesla('Black',5)
print(c2.__dict__)

