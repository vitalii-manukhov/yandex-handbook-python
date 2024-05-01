class Fraction:

    def __init__(self, *args):
        if len(args) == 1:  # str or one number
            if isinstance(args[0], str):
                numerator_str, denominator_str = ' ', ' ' 

                if args[0].find('/') != -1:
                    numerator_str, denominator_str = \
                        args[0].split(sep='/')
                else:
                    numerator_str, denominator_str = args[0], '1'
                
                if (int(numerator_str) < 0 and 
                        int(denominator_str) < 0):
                    self.__numerator, self.__denominator = (
                        abs(int(numerator_str)), 
                        abs(int(denominator_str)))
                elif int(denominator_str) < 0:
                    self.__numerator, self.__denominator = (
                        (int(numerator_str)) * (-1), 
                        abs(int(denominator_str)))
                else:
                    self.__numerator, self.__denominator = (
                        int(numerator_str), 
                        int(denominator_str))
            else:
                if (args[0] < 0):
                    self.__numerator = args[0]
                    self.__denominator = 1
                else:
                    self.__numerator = args[0]
                    self.__denominator = 1
        elif len(args) == 2:  # two numbers
            if (args[0] < 0 and args[1] < 0):
                self.__numerator = abs(args[0])
                self.__denominator = abs(args[1])
            elif (args[1] < 0):
                self.__numerator = (-1) * args[0]
                self.__denominator = abs(args[1])               
            else:
                self.__numerator = args[0]
                self.__denominator = args[1]                

        self.__ReduceFraction()

    def __GSD(self, other=None):
        if other is None:
            if (self.__numerator == 0):
                return 1
            
            temporary_left = self.__numerator
            temporary_right = self.__denominator
        else:
            temporary_left = other.__denominator
            temporary_right = self.__denominator

        while temporary_left:
            temporary_right, \
                temporary_left = (
                    temporary_left, 
                    temporary_right %
                    temporary_left)

        return abs(temporary_right)

    def __ReduceFraction(self):
        gsd = self.__GSD()

        if (gsd != 1):
            self.__numerator //= gsd
            self.__denominator //= gsd

    def __LSM(self, other):
        gsd = self.__GSD(other)
        return abs(self.__denominator * other.__denominator) // gsd

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"Fraction('{self.__numerator}/{self.__denominator}')"

    def numerator(self, number=None):
        if number is None:
            if self.__numerator < 0:
                return self.__numerator * (-1)
            else:
                return self.__numerator
        else:
            if number < 0 and self.__numerator < 0:
                self.__numerator = number * (-1)
            else:
                if self.__numerator < 0:
                    self.__numerator = number * (-1)
                else:
                    self.__numerator = number

            self.__ReduceFraction()

    def denominator(self, number=None):
        if number is None:
            return self.__denominator
        else:
            if (number < 0):
                self.__numerator *= (-1)
                self.__denominator = number * (-1)
            else:
                self.__denominator = number
            
            self.__ReduceFraction()

    def __neg__(self):
        temporary = Fraction(self.__numerator * (-1),
                             self.__denominator)
        return temporary
    
    def __add__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return Fraction(self.__numerator,
                                self.__denominator)
            other = Fraction(other)

        if self.__denominator == other.__denominator:
            return Fraction(self.__numerator + other.__numerator,
                            self.__denominator)

        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        return Fraction(self.__numerator * self_multiplier + 
                        other.__numerator * other_multiplier, 
                        lsm)

    def __iadd__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return self
            other = Fraction(other)

        if self.__denominator == other.__denominator:
            self.__numerator = self.__numerator + other.__numerator

            self.__ReduceFraction()

            return self

        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        self.__numerator = (self.__numerator * self_multiplier +
                            other.__numerator * other_multiplier)
        self.__denominator = lsm

        self.__ReduceFraction()

        return self

    def __sub__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return Fraction(self.__numerator,
                                self.__denominator)
            other = Fraction(other)

        if self.__denominator == other.__denominator:
            return Fraction(self.__numerator - other.__numerator,
                            self.__denominator)

        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        return Fraction(self.__numerator * self_multiplier -
                        other.__numerator * other_multiplier, 
                        lsm)

    def __isub__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return self 
            other = Fraction(other)

        if self.__denominator == other.__denominator:
            self.__numerator = self.__numerator - other.__numerator

            self.__ReduceFraction()

            return self

        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        self.__numerator = (self.__numerator * self_multiplier -
                            other.__numerator * other_multiplier)
        self.__denominator = lsm

        self.__ReduceFraction()

        return self
    
    def __mul__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return Fraction(self.__numerator,
                                self.__denominator)
            other = Fraction(other)

        return Fraction(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return Fraction(self.__numerator,
                                self.__denominator)
            other = Fraction(other)

        return Fraction(self.__numerator * other.__denominator,
                        self.__denominator * other.__numerator)

    def __imul__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return self
            other = Fraction(other)

        self.__numerator *= other.__numerator
        self.__denominator *= other.__denominator

        self.__ReduceFraction()

        return self

    def __itruediv__(self, other):
        if isinstance(other, int):
            if (other == 0):
                return self
            other = Fraction(other)

        if (other.__numerator < 0):
            self.__numerator *= other.__denominator * (-1)
            self.__denominator *= other.__numerator * (-1)
        else:
            self.__numerator *= other.__denominator
            self.__denominator *= other.__numerator

        self.__ReduceFraction()

        return self
    
    def reverse(self):
        if (self.__numerator < 0):
            return Fraction(self.__denominator * (-1),
                            self.__numerator * (-1))
        
        return Fraction(self.__denominator,
                        self.__numerator)
    
    def __lt__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator < 0:
                return True
            elif other == 0 and self.__numerator >= 0:
                return False
            else:
                other = Fraction(other)
            
        if self.__numerator < 0 and other.__numerator > 0:
            return True
        elif other.__numerator < 0 and self.numerator > 0:
            return False

        if self.__denominator == other.__denominator:
            if self.__numerator < other.__numerator:
                return True
            
            return False
            
        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        if (self.__numerator * self_multiplier <
                other.__numerator * other_multiplier):
            return True
        
        return False

    def __le__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator <= 0:
                return True
            elif other == 0 and self.__numerator > 0:
                return False
            else:
                other = Fraction(other)

        if self.__numerator < 0 and other.__numerator > 0:
            return True
        elif other.__numerator < 0 and self.numerator > 0:
            return False

        if self.__denominator == other.__denominator:
            if self.__numerator <= other.__numerator:
                return True
            
            return False
            
        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        if (self.__numerator * self_multiplier <=
                other.__numerator * other_multiplier):
            return True
        
        return False

    def __eq__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator == 0:
                return True
            elif other == 0 and self.__numerator != 0:
                return False
            else:
                other = Fraction(other)

        if (self.__denominator == other.__denominator and
                self.__numerator == other.__numerator):

            return True
        
        return False

    def __ne__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator != 0:
                return True
            elif other == 0 and self.__numerator == 0:
                return False
            else:
                other = Fraction(other)

        if (self.__denominator == other.__denominator and
                self.__numerator == other.__numerator):

            return False
        
        return True

    def __gt__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator > 0:
                return True
            elif other == 0 and self.__numerator <= 0:
                return False
            else:
                other = Fraction(other)

        if self.__numerator < 0 and other.__numerator > 0:
            return False
        elif other.__numerator < 0 and self.__numerator > 0:
            return True

        if self.__denominator == other.__denominator:
            if self.__numerator > other.__numerator:
                return True
            
            return False
            
        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        if (self.__numerator * self_multiplier >
                other.__numerator * other_multiplier):
            return True
        
        return False

    def __ge__(self, other):
        if isinstance(other, int):
            if other == 0 and self.__numerator >= 0:
                return True
            elif other == 0 and self.__numerator < 0:
                return False
            else:
                other = Fraction(other)

        if self.__numerator < 0 and other.__numerator > 0:
            return False
        elif other.__numerator < 0 and self.__numerator > 0:
            return True

        if self.__denominator == other.__denominator:
            if self.__numerator >= other.__numerator:
                return True
            
            return False
            
        lsm = self.__LSM(other)

        self_multiplier = lsm // self.__denominator
        other_multiplier = lsm // other.__denominator

        if (self.__numerator * self_multiplier >=
                other.__numerator * other_multiplier):
            return True
        
        return False
    
    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -(self - other)

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return (self / other).reverse()
    
f_5 = Fraction(3, 4)
print(2 * f_5)

