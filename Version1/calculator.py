from math import sqrt
def mean(numbers):
	"""
    Calculate the mean of a list of numbers
	:param numbers:
	:return:
	"""
	return sum(numbers)/float(len(numbers))

def standart_deviation(numbers):
	"""
	Calculate the standard deviation of a list of numbers
	:param numbers:
	:return:
	"""
	avg = mean(numbers)
	variance = sum([(x-avg)**2 for x in numbers]) / float(len(numbers)-1)
	return sqrt(variance)