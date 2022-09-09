from dataset_init import *
# Calculate the mean of a list of numbers
def mean(numbers):
	return sum(numbers)/float(len(numbers))

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
	separated_dict = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		class_value = vector[-1]
		if (class_value not in separated_dict):
			separated_dict[class_value] = list()
		separated_dict[class_value].append(vector)
	return separated_dict

print(separate_by_class(dataset))
#@print(separate_by_class(local_db))