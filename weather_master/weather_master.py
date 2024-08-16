"""
File: weather_master.py
Name: Ray
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	This program finds the maximum, minimum, average, and numbers of inputs under 16 among user inputs, respectively.
	"""
	print("stanCode \"Weather Master 4.0!" + '"')
	data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
	count = 1
	# counts of inputs
	if data == EXIT:
		print('No temperatures were entered')
	else:
		maximum = data
		minimum = data
		add = data
		average = data
		# in case if there's only one input, the average won't be assigned
		if data < 16:
			cold_days = 1
		else:
			cold_days = 0
		while True:
			data = int(input('Next temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			if data > maximum:
				maximum = data
			if data < minimum:
				minimum = data
			add = add + data
			count += 1
			average = add / count
			if data < 16:
				cold_days += 1

		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(float(average)))
		print(str(cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
