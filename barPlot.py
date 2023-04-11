
import matplotlib.pyplot as plt

stats = open('C:/Users/Nick Wong/Downloads/stats.txt', 'r')

x = []
y = []

for line in stats:
    if line.startswith('20'):
        line = line.rsplit()
        x.append(line[0])
        y.append(int(line[1]))

plt.figure(1)
plt.bar(x,y)

plt.title("Total Sales for Each Year") # Writing plot title
plt.xlabel("Year")      # Writing x-axis label
plt.ylabel("Total Sales")  # Writing y-axis label

plt.show()

stats.close()
