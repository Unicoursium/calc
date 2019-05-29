import math
while True:
    a = float(input('a='))
    b = float(input('b='))
    c = float(input('c='))
    delta = (b * b - (4 * a) * c)
    if (math.sqrt(delta) == int(math.sqrt(delta))) :
        if (delta > 0) :
            print('(dif_x)x1 =',x1,'x2=',x2)
            x1 = ((b * -1 + math.sqrt(delta)) / (2 * a))
            x2 = ((b * -1 - math.sqrt(delta)) / (2 * a))
        elif (delta == 0) :
            x1 = ((b * -1 + math.sqrt(delta)) / (2 * a))
            x2 = ((b * -1 - math.sqrt(delta)) / (2 * a))
            print('(sam_x)x1=x2=',x1)
        else :
            print('error')
    else :
        if (delta > 0) :
            print('(dif_x) x1=','(',(b * -1),'+ sqrt(',delta,')  /',(2 * a),'x2= (',(b * -1),'- sqrt(',delta,')  /',(2 * a),')')
        elif (delta == 0) :
            print('(dif_x) x1=x2=','(',(b * -1),'-   sqrt(',delta,')  /',(2 * a))
        else :
            print('error')
