class Car:
    def __init__(self,color,brand,door):
        # self.color = 'red'
        # self.brand = 'Tesla'
        # self.door=5
        self.color = color
        self.brand = brand
        self.door=door
        self.type = type

    def run(self):
        tmpType = ''
        if self.type == 'HRV':
            tmpType = '跨界轎旅車'
        else:
            tmpType = '一般車'
        print(f'您的車品牌為{self.brand}，顏色為 {self.color}，型號是 {self.type} 的 {self.door}門車')

c1 = Car('red','Tesla',5,'ModelS')
# print(c1)
# print (c1.color)
# print(c1.brand)
# print(c1.door)
# print(c1.__dict__)
c1.run()

c2 = Car('black','Toyota',5,'HRV')
# print(c2.__dict__)
c2.run()
