import matplotlib.pyplot as plt

rainfall = [200, 300, 400, 500, 600, 700, 800]
productivity = [50, 60, 70, 80, 85, 90, 92]

plt.scatter(rainfall, productivity)
plt.xlabel('Rainfall (mm)')
plt.ylabel('Crop Productivity (quintals/acre)')
plt.title('Rainfall vs Agricultural Productivity')
plt.show()
