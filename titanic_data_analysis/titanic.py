import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('titanic_data/train.csv')
	print(data)
	print(data.count())

	plt.figure(figsize=(18, 9))
	plt.subplot2grid((3, 4), (0, 0))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (0, 1))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 2))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (0, 3))
	data.Age.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Age')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='blue')
	plt.title('Men survived')

	plt.subplot2grid((3, 4), (1, 1))
	data.Survived[data.Sex == 'female'].value_counts(normalize=True).sort_index().plot(kind='bar', color='red')
	plt.title('Women survived')

	plt.subplot2grid((3, 4), (1, 2))
	data.Survived[data.Pclass == 1].value_counts(normalize=True).sort_index().plot(kind='bar', color='gray')
	plt.title('Pclass1 survived')

	plt.subplot2grid((3, 4), (1, 3))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='gray')
	plt.title('Pclass3 survived')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Pclass == 1][data.Sex == 'male'].value_counts(normalize=True).\
		sort_index().plot(kind='bar', color='blue')
	plt.title('Rich men survived')

	plt.subplot2grid((3, 4), (2, 1))
	data.Survived[data.Pclass == 3][data.Sex == 'male'].value_counts(normalize=True).\
		sort_index().plot(kind='bar', color='blue')
	plt.title('Poor men survived')

	plt.subplot2grid((3, 4), (2, 2))
	data.Survived[data.Pclass == 1][data.Sex == 'female'].value_counts(normalize=True).\
		sort_index().plot(kind='bar', color='red')
	plt.title('Rich female survived')

	plt.subplot2grid((3, 4), (2, 3))
	data.Survived[data.Pclass == 1][data.Sex == 'female'].value_counts(normalize=True).\
		sort_index().plot(kind='bar', color='red')
	plt.title('Poor female survived')

	plt.show()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
