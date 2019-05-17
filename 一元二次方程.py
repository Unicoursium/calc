import math


a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
x1 = ((b * -1 + math.sqrt(b * b - (4 * a) * c)) / (2 * a))
x2 = ((b * -1 - math.sqrt(b * b - (4 * a) * c)) / (2 * a))
if ((b * b - (4 * a) * c)> 0) :
    print('(dif_x)x1 =',x1,'x2=',x2)
elif ((b * b - (4 * a) * c)== 0) :
    print('(sam_x)x1=x2=',x1)
else :
    print('error')
