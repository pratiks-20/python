import matplotlib.pyplot as plt

sources = ['Coal', 'Natural Gas', 'Hydro', 'Solar', 'Wind']
contribution = [40, 25, 15, 10, 10]

plt.pie(contribution, labels=sources, autopct='%1.1f%%')
plt.title('Energy Source Contribution')
plt.show()
