import numpy as np
from matplotlib import pyplot as plt


number_count = np.array([10, 100, 1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])
time_count_er = np.array([0.0000186, 0.000704, 0.06636, 11.23, 51.27, 116.7,
                          211.3, 351.1, 484.1, 676.6, 878.2, 1114.7, 1397.0])
time_count_s = np.array([0.00002376, 0.002363, 0.4051, 80.29, 371.11, 897.4, 1675.1])
primes = np.array([29, 541, 7919, 104729, 224737, 350377, 479909, 611953, 746773, 882377, 1020379, 1159523, 1299709])

plt.plot(number_count, time_count_er, c='b', label='Eratosthenes')
plt.plot(number_count[:7], time_count_s, color='r', label='other')
plt.title('Primes counts',)
plt.legend(loc='lower right')
plt.tick_params(axis='x',)
plt.tick_params(axis='y',)
plt.grid()
plt.savefig('alg_graph.pdf', dpi=300,)
plt.show()
