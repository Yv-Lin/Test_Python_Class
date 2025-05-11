#  1oz = 29.573ml
#
# x = input('請輸入轉換的數字')
# s = input('單位是oz還是ml?(o/m)')
#
# if s=='o':
#     result = float(x) * 29.573
#     result = round(result,2)
#     print(f'您的換算結果為{x}oz約{result}ml')
# else:
#     result = float(x) / 29.573
#     result = round(result,2)
#     print(f'您的換算結果為{x}ml約{result}oz')

class Oz:
    def __init__(self,x,s):
        self.x = float(x)
        self.s = s

    def oz_to_ml(self):
        result = self.x * 29.573
        result = round(result,2)
        print(f'您的換算結果為{self.x}oz約{result}ml')

    def ml_to_oz(self):
        result = self.x / 29.573
        result = round(result,2)
        print(f'您的換算結果為{self.x}ml約{result}oz')

    def result(self):
        if self.s == 'o':
            self.oz_to_ml()
        else:
            self.ml_to_oz()


x = input('請輸入轉換的數字:')
s = input('單位是oz還是ml?(o/m):')

r = Oz(x,s)
# r.result()

if s == 'o':
    r.oz_to_ml()
else:
    r.ml_to_oz()
