class Multiple():
    def __init__(self):
        print("initize instance variables")

    def is_mul_three(self, num):
        if num % 3 == 0:
            return True
        else:
            return False

    def is_mul_five(self, num):
        if num % 5 == 0:
            return True
        else:
            return False
        
    def is_mul_three_five(self, num):
        return("Function to test multiple of 3 and 5")

        
cal= Multiple()
print(cal.is_mul_three(9))
print(cal.is_mul_five(17))
#print(cal.is_mul_five(5))

#print(cal.is_mul_three_five(4))
