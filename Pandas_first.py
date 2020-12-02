import pandas
data = pandas.read_csv('titanic.csv', index_col = 'PassengerId')
print(data['Sex'].value_counts()['male'], end=' ')
print(data['Sex'].value_counts()['female'])
print(round(data['Survived'].value_counts()[1] / data['Survived'].count() * 100, 2))