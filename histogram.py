import numpy as np
import matplotlib.pyplot as plt

random_uniform = np.random.uniform(0, 7, 500)
random_normal = np.random.normal(0, 7, 500)

print("Random Uniform: ", random_uniform)
print("Random Normal: ", random_normal)

# plot uniform distribution
plt.hist(random_uniform, bins = 100, color = 'orange', edgecolor = 'black')

plt.title("Histogram of Random Floats")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()



# plot normal distribution 
#plt.hist(random_normal, bins = 100, color = 'orange', edgecolor = 'black')

#plt.title("Histogram of Random Floats")
#plt.xlabel("Value")
#plt.ylabel("Frequency")

#plt.show()

#them6 dong nay

#them them dong nay

#chi cho branch 2
