import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
production = [120, 150, 100, 130]

plt.bar(regions, production)
plt.xlabel('Regions')
plt.ylabel('Rice Production (tons)')
plt.title('Rice Production in Different Regions')
plt.show()
