import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]

y = [30, 40, 27, 42,32]


plt.figure()

plt.plot(x, y)

plt.title('Andamento temperature')

plt.xlabel('giorno')

plt.ylabel('temperatura')

plt.show()