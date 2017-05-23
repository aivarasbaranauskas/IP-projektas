from provider import Provider
from sklearn import tree

if __name__ == '__main__':
	provider = Provider()
	input = []
	target = []
	for d in provider.getLearnData():
		input.append(d[0])
		target.append(d[1][0])
	regressor = tree.DecisionTreeRegressor()
	regressor.fit(input,target)
	
	mult = provider.multiplier
	
	results = regressor.predict(input)
	print(results)
	w = open('output4_1.txt', 'w')
	for i, line in enumerate(results):
		w.write('%f;%f\n' % (target[i]*mult, line*mult))
	w.close()

	input = []
	target = []
	for d in provider.getTestData():
		input.append(d[0])
		target.append(d[1][0])
	results = regressor.predict(input)
	w = open('output4_2.txt', 'w')
	for i, line in enumerate(results):
		w.write('%f;%f\n' % (target[i]*mult, line*mult))
	w.close()