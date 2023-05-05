import matplotlib.pyplot as plt;

input_values = range(1, 5000)
cubes = [x**3 for x in input_values]

fig, ax = plt.subplots()

ax.scatter(input_values, cubes, c=cubes, cmap=plt.cm.Reds, s=0.5)

plt.show()