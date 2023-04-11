import matplotlib.pyplot as plt

stats = open('C:/Users/Nick Wong/Downloads/stats.txt', 'r')

x = ['July', 'August', 'September', 'October', 'November', 'December']
y = []

a = 7

for line in stats:
    if line.startswith('Estimated'):
        line = line.rsplit()
        while a <= 18:
            y.append(int(line[a]))
            a = a + 2

plt.figure(2)
plt.barh(x,y)

plt.title("Estimated Sales for the last Six Months of 2022")
plt.xlabel("Estimated Sales")
plt.ylabel("Month")
plt.grid()                  # Showing grids on the plot

plt.show()

stats.close()
