import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
from matplotlib.ticker import PercentFormatter
plt.style.use('seaborn-pastel')

'''
0 indicates tails
1 indicates heads
'''

# Number of coin flips in each set, N
N = 50

# Number of trials
NUM_TRIALS = 1000

# Array to store outocmes
results = []


def main():
    pool = mp.Pool()
    for _ in range(NUM_TRIALS):
        pool.apply_async(number_of_heads, args=(N, ), callback=log_result)

    pool.close()
    pool.join()


    binwidth = 1
    plt.hist(results, bins=range(0, 100, binwidth), density=True)
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    axes = plt.gca()
    axes.set_xlim([0,100])
    axes.set_ylim([0,1])
    plt.ylabel('Percentage of Occurences')
    plt.xlabel('Percentage Heads')
    plt.title(str(N)+' coin flips')
    plt.savefig('coin-flips-'+str(N)+'.png')
    plt.show()


def number_of_heads(N):
    set = np.random.randint(2, size=N)
    return set.tolist().count(1)

def log_result(result):
    result = result / N * 100
    results.append(result)

if __name__ == "__main__":
    main()