import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
cubes = [x**3 for x in input_values]

fig, ax = plt.subplots()

ax.plot(input_values, cubes, linewidth=3)
ax.set_xticks(input_values)
ax.set_yticks(cubes)

plt.show()