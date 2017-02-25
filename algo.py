class Fraction(object):
	def __init__(self, num, den):
		self.num = num
		self.den = den

	def __str__(self):
		return '{}/{}'.format(self.num, self.den)

	def __add__(self, other_fraction):
		numerator  = self.num*other_fraction.den + self.den*other_fraction.num
		denominator = self.den * other_fraction.den
		common = gcd(numerator, denominator)
		return Fraction(numerator//common, denominator//common)	

	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den
		return firstnum == secondnum

	def multiply(self, other):
		numerator = self.num * other.num
		denominator = self.den * other.den
		common = gcd(numerator, denominator)
		return Fraction(numerator // common, denominator // common)

	def subtract(self, other):
		numerator = (self.num * other.den) - (self.den * other.num)
		denominator = self.den * other.den
		common = gcd(numerator, denominator)
		return Fraction(numerator//common, denominator//common)
	
	def divide(self, other):
		numerator = self.num * other.den
		denominator = self.den * other.num
		common = gcd(numerator, denominator)
		return Fraction(numerator // common, denominator // common)
	

	def lessthan(self, other):
		return (self.num/self.den) < (other.num/other.den)

	def greaterthan(self, other):
		return (self.num/self.den) > (self.num/self.den)

	def to_decimal(self):
		return self.num/self.den


def gcd(m, n):
	while m % n != 0:
		oldm = m
		oldn = n
		m = oldn
		n = oldm % oldn
	return n


