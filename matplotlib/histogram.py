import matplotlib.pyplot as plt

rainfall = [5, 10, 12, 8, 6, 15, 18, 7, 11, 9, 13, 14, 6, 10, 12]

plt.hist(rainfall, bins=6, color='blue', edgecolor='black')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Number of Days')
plt.title('Rainfall Distribution in a Month')
plt.show()
