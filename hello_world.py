import math, decimal
#print ("Hi")

#age = input ("your age is ?")

'''
if( age == 43):
    print("your age is: " + str(age))
else:
    print ("your age is not: " + str(age))
'''

#print( type(age))

def Ex():
    #print(not a)
    x=5
    y=1.0/3
    z=1.23
    print("{} + {} = ".format(x, y), x+y)
    print("{} - {} = ".format(x, y), x-y)
    print("{} * {} = ".format(x, y), x*y)
    print("{} / {} = ".format(x, y), x/y)
    print("{} % {} = ".format(x, y), x%y)
    print("{} ** {} = ".format(x, y), x**y)

    print(" {} is binary =".format(x), bin(x))
    print(" {} is type =".format(x), type(x))
    print(" {} is float =".format(x), float(x))
    print(" {} is rounded with 3 decimal place".format(y), round(y, 3))
    print(" {} is ceil =".format(z), math.ceil(z))
    print(" {} is floor =".format(z), math.floor(z))
   
Ex()


#Data type are: Integer, binary, octal, hexadecimal

#decimal.Decimal("1.233245435465")  for maintain the output
