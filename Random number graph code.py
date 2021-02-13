#! /usr/bin/env python




# imports of external packages to use in our code

import numpy as np
import matplotlib.pyplot as plt

# main function for this Python code
if __name__ == "__main__":
    # Read random numbers from a file
    myx = []
    myx = np.loadtxt("random-numbers.txt")
    #print(rnd)

    # create histogram of our data
    n, bins, patches = plt.hist(myx, 50, density=True, facecolor='r', alpha=0.75)

    # plot formating options
    plt.xlabel('t')
    plt.ylabel('Probability')
    plt.title('Uniform random number')
    plt.grid(True)

    # show figure (program only ends once closed
    plt.show()
