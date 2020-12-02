import pandas
data = pandas.read_csv('titanic.csv', index_col = 'PassengerId')
print(data['Sex'].value_counts()['male'], end=' ')
print(data['Sex'].value_counts()['female'])

print(round(data['Survived'].value_counts()[1] / data['Survived'].count() * 100, 2))

print(round(data['Pclass'].value_counts()[1] / data['Pclass'].count() * 100, 2))

print(round(data['Age'].mean(), 2), end=' ')
n = data['Age'].count()
d = data.sort_values('Age', ascending=False).reset_index()['Age']
print((d[n // 2 - 1] + d[n // 2]) / 2)

print(data[['Parch', 'SibSp']].corr())
