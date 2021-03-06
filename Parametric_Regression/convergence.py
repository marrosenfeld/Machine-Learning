#!/usr/bin/python
import numpy as np
import numpy.linalg as la
from sklearn import datasets, linear_model, preprocessing
import matplotlib.pyplot as plt
from data_utils import *
from regression import *
import  scipy.stats as stats

def main():

    X, data_Y = readData("data/CCPP/Folds.csv", delim=",", skipHeader=True, scale=False)
    col_mean = stats.nanmean(X,axis=0)
    inds = np.where(np.isnan(X))
    X[inds]=np.take(col_mean,inds[1])
    X = preprocessing.scale(X)

    z = mapFeatures(X,1)

    handles = np.empty([0,1])
    for lw in [0.000005,0.00001, 0.000015]:
        #perform gradient descent
        thetas, iterations, errors = gradient_descent(z,data_Y, threshold=0.0001, learning_weight=lw)
        print("Itearative Method Coefficients: {},Iterations:{}".format(thetas,iterations))
        handle = plt.plot(errors[0:50,0],errors[0:50,1], linewidth = 4, label="Learning Weight = {:.6f}".format(lw))
        handles = np.append(handles,handle)
    plt.legend(handles=[handles[0],handles[1],handles[2]])
    plt.ticklabel_format(useOffset=False)
    plt.xlabel("Iteration")
    plt.ylabel("Squared Mean Error")
    plt.show()

if __name__ == "__main__":
    main()