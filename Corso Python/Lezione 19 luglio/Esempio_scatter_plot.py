import numpy as np
import matplotlib.pyplot as plt

#x = np.random.rand(50)
#y = np.random.rand(50)
età = [18,19,20,21]
reddito = [10000, 10000, 12000, 13000]

plt.figure()
plt.scatter(età, reddito)
plt.title('Reddito in relazione all\'età ')
plt.xlabel('età')
plt.ylabel('reddito')
plt.show()