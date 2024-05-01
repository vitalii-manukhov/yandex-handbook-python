import unittest

from fraction import Fraction

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.f_1 = Fraction("1/1")
        self.f_2 = Fraction("-1/1")
        self.f_3 = Fraction("1/-1")
        self.f_4 = Fraction("-1/-1")

        self.f_5 = Fraction(2, 3)
        self.f_6 = Fraction(-2, 3)
        self.f_7 = Fraction(2, -3)
        self.f_8 = Fraction(-2, -3)

        self.f_9 = Fraction("0/1")
        self.f_10 = Fraction(0, 2)

        self.f_11 = Fraction(-1)
        self.f_12 = Fraction(1)
        self.f_13 = Fraction(2)
        self.f_14 = Fraction(20)

        self.f_15 = Fraction('3')
        self.f_16 = Fraction("30")
        self.f_17 = Fraction("-100")

    def test_initialization(self):
        self.assertEqual(self.f_1.numerator(), 1)
        self.assertEqual(self.f_1.denominator(), 1)
        self.assertEqual(self.f_2.numerator(), 1)
        self.assertEqual(self.f_2.denominator(), 1)
        self.assertEqual(self.f_3.numerator(), 1)
        self.assertEqual(self.f_3.denominator(), 1)
        self.assertEqual(self.f_4.numerator(), 1)
        self.assertEqual(self.f_4.denominator(), 1)

        self.assertEqual(self.f_5.numerator(), 2)
        self.assertEqual(self.f_5.denominator(), 3)
        self.assertEqual(self.f_6.numerator(), 2)
        self.assertEqual(self.f_6.denominator(), 3)
        self.assertEqual(self.f_7.numerator(), 2)
        self.assertEqual(self.f_7.denominator(), 3)
        self.assertEqual(self.f_8.numerator(), 2)
        self.assertEqual(self.f_8.denominator(), 3)

        self.assertEqual(self.f_9.numerator(), 0)
        self.assertEqual(self.f_9.denominator(), 1)
        self.assertEqual(self.f_10.numerator(), 0)
        self.assertEqual(self.f_10.denominator(), 2)

        self.assertEqual(self.f_11.numerator(), 1)
        self.assertEqual(self.f_11.denominator(), 1)
        self.assertEqual(self.f_12.numerator(), 1)
        self.assertEqual(self.f_12.denominator(), 1)
        self.assertEqual(self.f_13.numerator(), 2)
        self.assertEqual(self.f_13.denominator(), 1)
        self.assertEqual(self.f_14.numerator(), 20)
        self.assertEqual(self.f_14.denominator(), 1)

        self.assertEqual(self.f_15.numerator(), 3)
        self.assertEqual(self.f_15.denominator(), 1)
        self.assertEqual(self.f_16.numerator(), 30)
        self.assertEqual(self.f_16.denominator(), 1)
        self.assertEqual(self.f_17.numerator(), 100)
        self.assertEqual(self.f_17.denominator(), 1)

    def test___str__(self):
        self.assertEqual(self.f_1.__str__(), "1/1")
        self.assertEqual(self.f_2.__str__(), "-1/1")
        self.assertEqual(self.f_3.__str__(), "-1/1")
        self.assertEqual(self.f_4.__str__(), "1/1")

        self.assertEqual(self.f_5.__str__(), "2/3")
        self.assertEqual(self.f_6.__str__(), "-2/3")
        self.assertEqual(self.f_7.__str__(), "-2/3")
        self.assertEqual(self.f_8.__str__(), "2/3")

        self.assertEqual(self.f_9.__str__(), "0/1")
        self.assertEqual(self.f_10.__str__(), "0/2")

        self.assertEqual(self.f_11.__str__(), "-1/1")
        self.assertEqual(self.f_12.__str__(), "1/1")
        self.assertEqual(self.f_13.__str__(), "2/1")
        self.assertEqual(self.f_14.__str__(), "20/1")

        self.assertEqual(self.f_15.__str__(), "3/1")
        self.assertEqual(self.f_16.__str__(), "30/1")
        self.assertEqual(self.f_17.__str__(), "-100/1")

    def test___repr__(self):
        self.assertEqual(self.f_1.__repr__(), "Fraction('1/1')")
        self.assertEqual(self.f_2.__repr__(), "Fraction('-1/1')")
        self.assertEqual(self.f_3.__repr__(), "Fraction('-1/1')")
        self.assertEqual(self.f_4.__repr__(), "Fraction('1/1')")

        self.assertEqual(self.f_5.__repr__(), "Fraction('2/3')")
        self.assertEqual(self.f_6.__repr__(), "Fraction('-2/3')")
        self.assertEqual(self.f_7.__repr__(), "Fraction('-2/3')")
        self.assertEqual(self.f_8.__repr__(), "Fraction('2/3')")

        self.assertEqual(self.f_9.__repr__(), "Fraction('0/1')")
        self.assertEqual(self.f_10.__repr__(), "Fraction('0/2')")

        self.assertEqual(self.f_11.__repr__(), "Fraction('-1/1')")
        self.assertEqual(self.f_12.__repr__(), "Fraction('1/1')")
        self.assertEqual(self.f_13.__repr__(), "Fraction('2/1')")
        self.assertEqual(self.f_14.__repr__(), "Fraction('20/1')")

        self.assertEqual(self.f_15.__repr__(), "Fraction('3/1')")
        self.assertEqual(self.f_16.__repr__(), "Fraction('30/1')")
        self.assertEqual(self.f_17.__repr__(), "Fraction('-100/1')")

    def test___neg__(self):
        # __init__
        self.assertEqual((-self.f_1).numerator(), 1)
        self.assertEqual((-self.f_1).denominator(), 1)
        self.assertEqual((-self.f_2).numerator(), 1)
        self.assertEqual((-self.f_2).denominator(), 1)
        self.assertEqual((-self.f_3).numerator(), 1)
        self.assertEqual((-self.f_3).denominator(), 1)
        self.assertEqual((-self.f_4).numerator(), 1)
        self.assertEqual((-self.f_4).denominator(), 1)

        self.assertEqual((-self.f_5).numerator(), 2)
        self.assertEqual((-self.f_5).denominator(), 3)
        self.assertEqual((-self.f_6).numerator(), 2)
        self.assertEqual((-self.f_6).denominator(), 3)
        self.assertEqual((-self.f_7).numerator(), 2)
        self.assertEqual((-self.f_7).denominator(), 3)
        self.assertEqual((-self.f_8).numerator(), 2)
        self.assertEqual((-self.f_8).denominator(), 3)

        self.assertEqual((-self.f_9).numerator(), 0)
        self.assertEqual((-self.f_9).denominator(), 1)
        self.assertEqual((-self.f_10).numerator(), 0)
        self.assertEqual((-self.f_10).denominator(), 2)

        self.assertEqual((-self.f_11).numerator(), 1)
        self.assertEqual((-self.f_11).denominator(), 1)
        self.assertEqual((-self.f_12).numerator(), 1)
        self.assertEqual((-self.f_12).denominator(), 1)
        self.assertEqual((-self.f_13).numerator(), 2)
        self.assertEqual((-self.f_13).denominator(), 1)
        self.assertEqual((-self.f_14).numerator(), 20)
        self.assertEqual((-self.f_14).denominator(), 1)

        self.assertEqual((-self.f_15).numerator(), 3)
        self.assertEqual((-self.f_15).denominator(), 1)
        self.assertEqual((-self.f_16).numerator(), 30)
        self.assertEqual((-self.f_16).denominator(), 1)
        self.assertEqual((-self.f_17).numerator(), 100)
        self.assertEqual((-self.f_17).denominator(), 1)

        #__str__
        self.assertEqual((-self.f_1).__str__(), "-1/1")
        self.assertEqual((-self.f_2).__str__(), "1/1")
        self.assertEqual((-self.f_3).__str__(), "1/1")
        self.assertEqual((-self.f_4).__str__(), "-1/1")

        self.assertEqual((-self.f_5).__str__(), "-2/3")
        self.assertEqual((-self.f_6).__str__(), "2/3")
        self.assertEqual((-self.f_7).__str__(), "2/3")
        self.assertEqual((-self.f_8).__str__(), "-2/3")

        self.assertEqual((-self.f_9).__str__(), "0/1")
        self.assertEqual((-self.f_10).__str__(), "0/2")

        self.assertEqual((-self.f_11).__str__(), "1/1")
        self.assertEqual((-self.f_12).__str__(), "-1/1")
        self.assertEqual((-self.f_13).__str__(), "-2/1")
        self.assertEqual((-self.f_14).__str__(), "-20/1")

        self.assertEqual((-self.f_15).__str__(), "-3/1")
        self.assertEqual((-self.f_16).__str__(), "-30/1")
        self.assertEqual((-self.f_17).__str__(), "100/1")
        
        # __repr__
        self.assertEqual((-self.f_1).__repr__(), "Fraction('-1/1')")
        self.assertEqual((-self.f_2).__repr__(), "Fraction('1/1')")
        self.assertEqual((-self.f_3).__repr__(), "Fraction('1/1')")
        self.assertEqual((-self.f_4).__repr__(), "Fraction('-1/1')")

        self.assertEqual((-self.f_5).__repr__(), "Fraction('-2/3')")
        self.assertEqual((-self.f_6).__repr__(), "Fraction('2/3')")
        self.assertEqual((-self.f_7).__repr__(), "Fraction('2/3')")
        self.assertEqual((-self.f_8).__repr__(), "Fraction('-2/3')")

        self.assertEqual((-self.f_9).__repr__(), "Fraction('0/1')")
        self.assertEqual((-self.f_10).__repr__(), "Fraction('0/2')")

        self.assertEqual((-self.f_11).__repr__(), "Fraction('1/1')")
        self.assertEqual((-self.f_12).__repr__(), "Fraction('-1/1')")
        self.assertEqual((-self.f_13).__repr__(), "Fraction('-2/1')")
        self.assertEqual((-self.f_14).__repr__(), "Fraction('-20/1')")

        self.assertEqual((-self.f_15).__repr__(), "Fraction('-3/1')")
        self.assertEqual((-self.f_16).__repr__(), "Fraction('-30/1')")
        self.assertEqual((-self.f_17).__repr__(), "Fraction('100/1')")

    def test_numerator(self):
        f = Fraction("1/5")
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "1/5")
        self.assertEqual(f.__repr__(), "Fraction('1/5')")

        f.numerator(2)
        self.assertEqual(f.numerator(), 2)
        self.assertEqual(f.__str__(), "2/5")
        self.assertEqual(f.__repr__(), "Fraction('2/5')")

        f.numerator(-3)
        self.assertEqual(f.numerator(), 3)
        self.assertEqual(f.__str__(), "-3/5")
        self.assertEqual(f.__repr__(), "Fraction('-3/5')")

        f.numerator(-2)
        self.assertEqual(f.numerator(), 2)
        self.assertEqual(f.__str__(), "2/5")
        self.assertEqual(f.__repr__(), "Fraction('2/5')")

        # Reduction
        f = Fraction(1, 10)
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "1/10")
        self.assertEqual(f.__repr__(), "Fraction('1/10')")

        f.numerator(2)
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "1/5")
        self.assertEqual(f.__repr__(), "Fraction('1/5')")

        f.denominator(10)
        f.numerator(5)
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "1/2")
        self.assertEqual(f.__repr__(), "Fraction('1/2')")

        f.denominator(10)
        f.numerator(-5)
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "-1/2")
        self.assertEqual(f.__repr__(), "Fraction('-1/2')")

        f.denominator(10)
        f.numerator(-5)
        self.assertEqual(f.numerator(), 1)
        self.assertEqual(f.__str__(), "1/2")
        self.assertEqual(f.__repr__(), "Fraction('1/2')")

    def test_denominator(self):
        f = Fraction("1/5")
        self.assertEqual(f.denominator(), 5)
        self.assertEqual(f.__str__(), "1/5")
        self.assertEqual(f.__repr__(), "Fraction('1/5')")

        f.denominator(4)
        self.assertEqual(f.denominator(), 4)
        self.assertEqual(f.__str__(), "1/4")
        self.assertEqual(f.__repr__(), "Fraction('1/4')")

        f.denominator(-3)
        self.assertEqual(f.denominator(), 3)
        self.assertEqual(f.__str__(), "-1/3")
        self.assertEqual(f.__repr__(), "Fraction('-1/3')")

        f.denominator(-4)
        self.assertEqual(f.denominator(), 4)
        self.assertEqual(f.__str__(), "1/4")
        self.assertEqual(f.__repr__(), "Fraction('1/4')")

        # Reduction
        f = Fraction(2, 5)
        self.assertEqual(f.denominator(), 5)
        self.assertEqual(f.__str__(), "2/5")
        self.assertEqual(f.__repr__(), "Fraction('2/5')")

        f.denominator(10)
        self.assertEqual(f.denominator(), 5)
        self.assertEqual(f.__str__(), "1/5")
        self.assertEqual(f.__repr__(), "Fraction('1/5')")

        f.numerator(2)
        f.denominator(-10)
        self.assertEqual(f.denominator(), 5)
        self.assertEqual(f.__str__(), "-1/5")
        self.assertEqual(f.__repr__(), "Fraction('-1/5')")

        f.numerator(2)
        f.denominator(-10)
        self.assertEqual(f.denominator(), 5)
        self.assertEqual(f.__str__(), "1/5")
        self.assertEqual(f.__repr__(), "Fraction('1/5')")

    def test___add__(self):
        f_1 = Fraction(1, 3)
        f_2 = Fraction(1, 3)
        
        f_3 = f_1 + f_2
        self.assertEqual(f_1.__str__(), "1/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "2/3")

        f_3.numerator(-2)
        f_2 = f_1 + f_3
        self.assertEqual(f_1.__str__(), "1/3")
        self.assertEqual(f_2.__str__(), "-1/3")
        self.assertEqual(f_3.__str__(), "-2/3")

        f_2.denominator(4)
        f_1 = f_2 + f_3
        self.assertEqual(f_1.__str__(), "-11/12")
        self.assertEqual(f_2.__str__(), "-1/4")
        self.assertEqual(f_3.__str__(), "-2/3")   

        f_2 = -f_3 + f_1
        self.assertEqual(f_1.__str__(), "-11/12")
        self.assertEqual(f_2.__str__(), "-1/4")
        self.assertEqual(f_3.__str__(), "-2/3")

        f_4 = -f_1 + f_2 + f_3
        self.assertEqual(f_1.__str__(), "-11/12")
        self.assertEqual(f_2.__str__(), "-1/4")
        self.assertEqual(f_3.__str__(), "-2/3")
        self.assertEqual(f_4.__str__(), "0/3")

        # Integer

        f_1 = Fraction(1)
        f_2 = Fraction(-2)
        f_3 = Fraction(-1)
        self.assertEqual(f_1.__str__(), "1/1")
        self.assertEqual(f_2.__str__(), "-2/1")
        self.assertEqual(f_3.__str__(), "-1/1")
        number = 3

        self.assertEqual(f_1 + f_2, Fraction(-1, 1))
        self.assertEqual(f_2.__str__(), "-2/1")
        self.assertEqual(f_3.__str__(), "-1/1")
        self.assertEqual(f_2 + f_3, Fraction("-3/1"))
        self.assertEqual((f_1 + 3).__str__(), "4/1")
        self.assertEqual((f_2 + number).__str__(), "1/1")
        self.assertEqual((f_3 + 3 + f_1).__str__(), "3/1")

        f_1.denominator(3)
        f_2.denominator(-8)
        self.assertEqual(f_1.__str__(), "1/3")
        self.assertEqual(f_2.__str__(), "1/4")
        self.assertEqual((f_1 + number).__str__(), "10/3")
        self.assertEqual((f_2 + 3).__str__(), "13/4")

        f_3.denominator(100)
        self.assertEqual(f_3.__str__(), "-1/100")
        self.assertEqual((f_3 + -number).__str__(), "-301/100")
        # self.assertEqual((number + f_3).__str__(), "")

    def test__sub__(self):
        f_1 = Fraction(2, 3)
        f_2 = Fraction(1, 3)

        f_3 = f_1 - f_2
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "1/3")

        f_3 = f_2 - f_1
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "-1/3")

        f_2.denominator(6)
        f_3 = f_1 - f_2
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/6")
        self.assertEqual(f_3.__str__(), "1/2")

        f_3 = f_2 - f_1
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/6")
        self.assertEqual(f_3.__str__(), "-1/2")

        f_2.denominator(3)
        f_3 = -f_1 - -f_2
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "-1/3")

        f_3 = -f_2 - -f_1
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "1/3")

        f_4 = f_1 - f_2 - f_3
        self.assertEqual(f_1.__str__(), "2/3")
        self.assertEqual(f_2.__str__(), "1/3")
        self.assertEqual(f_3.__str__(), "1/3")
        self.assertEqual(f_4.__str__(), "0/3")

        # Integer

        f_1 = Fraction(1, 3)
        f_2 = Fraction(2, 3)
        f_3 = Fraction("-3/5")
        f_4 = Fraction(3)
        number = 1

        self.assertEqual(f_1 - f_4, Fraction(-8, 3))
        self.assertEqual(f_2 - f_4, Fraction(-7, 3))
        self.assertEqual(f_3 - f_4, Fraction(-18, 5))
        self.assertEqual((-f_1 - 10).__str__(), "-31/3")
        self.assertEqual((f_2 - number).__str__(), "-1/3")
        self.assertEqual((f_3 - -number).__str__(), "2/5")

    def test___iadd__(self):
        f_1 = Fraction("1/10")
        f_2 = Fraction("3/10")
        self.assertEqual(f_1.__str__(), "1/10")
        self.assertEqual(f_2.__str__(), "3/10")
        
        expected_numerator = [2, 7, 1]
        expected_denominator = [5, 10, 1]

        for iteration in range(3):
            f_1 += f_2
            self.assertEqual(f_1.__str__(), f"{expected_numerator[iteration]}/{expected_denominator[iteration]}")
            self.assertEqual(f_2.__str__(), "3/10")

        expected_numerator = [7, 2, 1, -1]
        expected_denominator = [10, 5, 10, 5]

        for iteration in range(4):
            f_1 += -f_2
            self.assertEqual(f_1.__str__(), f"{expected_numerator[iteration]}/{expected_denominator[iteration]}")
            self.assertEqual(f_2.__str__(), "3/10")

        f_1 = Fraction(1)
        expected = [[2, 4, 7], [1, 1, 1]]

        # Integer
        for iteration in range(1, 4):
            f_1 += iteration
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration - 1]}/{expected[1][iteration - 1]}")

    def test___isub__(self):
        f_1 = Fraction("1/10")
        f_2 = Fraction("3/10")
        self.assertEqual(f_1.__str__(), "1/10")
        self.assertEqual(f_2.__str__(), "3/10")
        
        expected_numerator = [1, 1, 0]
        expected_denominator = [5, 10, 10]

        for iteration in range(3):
            f_2 -= f_1
            self.assertEqual(f_1.__str__(), "1/10")
            self.assertEqual(f_2.__str__(), f"{expected_numerator[iteration]}/{expected_denominator[iteration]}")

        expected_numerator = [1, 1, 3]
        expected_denominator = [10, 5, 10]

        for iteration in range(3):
            f_2 -= -f_1
            self.assertEqual(f_1.__str__(), "1/10")
            self.assertEqual(f_2.__str__(), f"{expected_numerator[iteration]}/{expected_denominator[iteration]}")
 
        # Integer
        f_1 = Fraction(3, 10)
        expected = [[-7, -27, -57], [10, 10, 10]]

        for iteration in range(1, 4):
            f_1 -= iteration
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration - 1]}/{expected[1][iteration - 1]}")

    def test___mul__(self):
        f_1 = Fraction(2, 5)
        f_2 = Fraction(3, 4)
        
        f_3 = f_1 * f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "3/10")

        f_3 = f_1 * -f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "-3/10")

        f_3 = -f_1 * -f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "3/10")

        f_4 = f_1 * f_2 * f_3
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "3/10")
        self.assertEqual(f_4.__str__(), "9/100")
 
        # Integer
        f_1 = Fraction(1, 3)
        f_2 = Fraction(2, -5)
        f_3 = Fraction(2)
        number = -2
        self.assertEqual(f_1.__str__(), "1/3")
        self.assertEqual(f_2.__str__(), "-2/5")
        self.assertEqual(f_1 * f_3, Fraction(2, 3))
        self.assertEqual(f_2 * f_3, Fraction(-4, 5))
        self.assertEqual(f_1 * number, Fraction(-2, 3))
        self.assertEqual(f_1 * -number, Fraction(2, 3))
        self.assertEqual(f_2 * -number, Fraction(-4, 5))

    def test__truediv__(self):
        f_1 = Fraction(2, 5)
        f_2 = Fraction(3, 4)
        
        f_3 = f_1 / f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "8/15")

        f_3 = f_1 / -f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "-8/15")

        f_3 = -f_1 / -f_2
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "8/15")

        f_4 = f_1 / f_2 / f_3
        self.assertEqual(f_1.__str__(), "2/5")
        self.assertEqual(f_2.__str__(), "3/4")
        self.assertEqual(f_3.__str__(), "8/15")
        self.assertEqual(f_4.__str__(), "1/1")

        # Integer
        f_1 = Fraction(1, 3)
        f_2 = Fraction(2, -5)
        f_3 = Fraction(2)
        number = -2
        self.assertEqual(f_1.__str__(), "1/3")
        self.assertEqual(f_2.__str__(), "-2/5")
        self.assertEqual(f_1 / f_3, Fraction(1, 6))
        self.assertEqual(f_2 / f_3, Fraction(-1, 5))
        self.assertEqual(f_1 / number, Fraction(-1, 6))
        self.assertEqual(f_1 / -number, Fraction(1, 6))
        self.assertEqual(f_2 / -number, Fraction(-1, 5))

    def test___imul__(self):
        f_1 = Fraction(2, 5)
        f_2 = Fraction(3, 4)
        expected = [[3, 9, 27], [10, 40, 160]]

        for iteration in range(3):
            f_1 *= f_2
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration]}/{expected[1][iteration]}")
            self.assertEqual(f_2.__str__(), "3/4")

        f_1 = Fraction(2, 5)
        expected = [[-3, 9, -27], [10, 40, 160]]

        for iteration in range(3):
            f_1 *= -f_2
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration]}/{expected[1][iteration]}")
            self.assertEqual(f_2.__str__(), "3/4")

        # Integer
        f_1 = Fraction(1, 3)
        expected = [[1, 2, 2], [3, 3, 1]]

        for iteration in range(1, 4):
            f_1 *= iteration
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration - 1]}/{expected[1][iteration - 1]}")

    def test___itruediv__(self):
        f_1 = Fraction(2, 5)
        f_2 = Fraction(3, 4)

        expected = [[8, 32, 128], [15, 45, 135]]

        for iteration in range(3):
            f_1 /= f_2
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration]}/{expected[1][iteration]}")
            self.assertEqual(f_2.__str__(), "3/4")

        f_1 = Fraction(2, 5)
        expected = [[-8, 32, -128], [15, 45, 135]]

        for iteration in range(3):
            f_1 /= -f_2
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration]}/{expected[1][iteration]}")
            self.assertEqual(f_2.__str__(), "3/4")

        # Integer
        f_1 = Fraction(1, 3)
        expected = [[1, 1, 1], [3, 6, 18]]

        for iteration in range(1, 4):
            f_1 /= iteration
            self.assertEqual(f_1.__str__(), f"{expected[0][iteration - 1]}/{expected[1][iteration - 1]}")

    def test_expressions(self):
        f_1 = Fraction(1, 1)
        f_2 = Fraction("1/2")
        f_3 = Fraction(2, 3)
        f_4 = Fraction("1/4")
        f_5 = Fraction(3, 4)

        self.assertEqual(((f_1 * f_2 - f_3) / f_4 + f_5).__str__(), "1/12")
        self.assertEqual((f_5 * 2).__str__(), "3/2")
        self.assertEqual((f_1 + 1 - 1 + 1 - (f_5 * 2 * 2 - 2)).__str__(), "1/1")

    def test_reverse(self):
        f_1 = Fraction(1, 1)
        f_2 = Fraction(2, 3)
        f_3 = Fraction(-4, 9)
        f_4 = Fraction(10, -7)
        f_5 = Fraction(5)

        self.assertEqual((f_1.reverse()).__str__(), "1/1")
        self.assertEqual((f_2.reverse()).__str__(), "3/2")
        self.assertEqual((f_3.reverse()).__str__(), "-9/4")
        self.assertEqual((f_4.reverse()).__str__(), "-7/10")
        self.assertEqual(f_5.reverse(), Fraction(1, 5))

    def test_comparison(self):
        f_1 = Fraction(1, 2)
        f_2 = Fraction(2, 3)
        f_3 = Fraction(-1, 2)
        f_4 = Fraction(-1 ,3)
        f_5 = Fraction(1)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_2.__str__(), "2/3")
        self.assertEqual(f_3.__str__(), "-1/2")
        self.assertEqual(f_4.__str__(), "-1/3")
        self.assertEqual(f_5.__str__(), "1/1")

        self.assertTrue(f_1 < f_2)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_2.__str__(), "2/3")

        self.assertTrue(f_1 < f_5 and -1 < f_5)
        self.assertTrue(f_4 < 0)

        self.assertTrue(f_1 <= f_1 and f_1 <= f_2)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_2.__str__(), "2/3")

        self.assertTrue(1 <= f_5)
        self.assertTrue(f_3 <= 0)

        self.assertTrue(f_1 == f_1)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_2.__str__(), "2/3")

        self.assertTrue(f_5 == 1)
        self.assertFalse(f_5 == 0)

        self.assertTrue(f_1 != f_3)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_3.__str__(), "-1/2")

        self.assertTrue(f_5 != -1)
        self.assertTrue(f_5 != 0)

        self.assertTrue(f_1 > f_3)
        self.assertEqual(f_1.__str__(), "1/2")
        self.assertEqual(f_3.__str__(), "-1/2")

        self.assertTrue(f_5 > -100)
        self.assertTrue(f_5 > 0)

        self.assertTrue(f_4 >= f_3 and f_2 >= f_4)
        self.assertEqual(f_2.__str__(), "2/3")
        self.assertEqual(f_3.__str__(), "-1/2")
        self.assertEqual(f_4.__str__(), "-1/3")

        self.assertTrue(f_5 >= f_3 and f_5 >= -100)
        self.assertTrue(f_5 >= 0)

    def test___radd__(self):
        f_1 = Fraction(1, 3)
        number = 3

        self.assertEqual(3 + f_1, Fraction(10, 3))
        self.assertEqual(number + -f_1, Fraction(8, 3))
        self.assertEqual(-number * 3 + -f_1, Fraction(-28, 3))

    def test___rsub__(self):
        f_1 = Fraction('9')
        number = -3

        self.assertEqual(-3 - -f_1, Fraction('6'))
        self.assertEqual(number - f_1, Fraction('-12'))
        self.assertEqual(number // number - f_1, Fraction('-8'))

    def test___rmul__(self):
        f_1 = Fraction("1/5")
        number = 5

        self.assertEqual(5 * f_1, Fraction(1))
        self.assertEqual(number * 5 * f_1, Fraction(5))
        self.assertEqual(-number * f_1, Fraction(-1))

    def test___rtruediv(self):
        f_1 = Fraction(5)
        number = 3

        self.assertEqual(5 / f_1, Fraction(1))
        self.assertEqual(-number / -f_1, Fraction(3, 5))
        self.assertEqual(-number * -number / -f_1, Fraction(-9, 5) )

if __name__ == "__main__":
    unittest.main()