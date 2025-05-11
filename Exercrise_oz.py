class Oz:
    def __init__(self, x, s,u):
        self.x = float(x)
        self.s = s
        self.u = 29.573


    def oz_to_ml(self):
        # result = float(x)*29.573
        result = float(x)* u
        result = round(result,2)
        print(f'您輸入的{self.x} oz，換算結果為{result} ml')

    def ml_to_oz(self):
        # result = float(x)/29.573
        result = float(x) / u
        result = round(result,2)
        print(f'您輸入的{self.x} ml，換算結果為{result} oz')

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
if s == 'm':
    r.ml_to_oz()
if s!= 'o' or s!= 'm':
    print('請確認輸入的轉換單位是否正確')


