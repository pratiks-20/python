import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y1 = [i**2 for i in x]
y2 = [i**3 for i in x]

plt.plot(x, y1, marker='o', label='y = x²')
plt.plot(x, y2, marker='s', label='y = x³')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of y = x² and y = x³')

plt.legend()

plt.show()
