import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class SimpleBayesClassifier:

    def __init__(self, n_pos, n_neg):
        
        """
        Initializes the SimpleBayesClassifier with prior probabilities.

        Parameters:
        n_pos (int): The number of positive samples.
        n_neg (int): The number of negative samples.
        
        Returns:
        None: This method does not return anything as it is a constructor.
        """

        self.n_pos =n_pos
        self.n_neg =n_neg
        self.prior_pos = n_pos/(n_pos+n_neg)
        self.prior_neg =n_neg/(n_pos+n_neg)

    def fit_params(self, x, y, n_bins = 10):

        """
        Computes histogram-based parameters for each feature in the dataset.

        Parameters:
        x (np.ndarray): The feature matrix, where rows are samples and columns are features.
        y (np.ndarray): The target array, where each element corresponds to the label of a sample.
        n_bins (int): Number of bins to use for histogram calculation.

        Returns:
        (stay_params, leave_params): A tuple containing two lists of tuples, 
        one for 'stay' parameters and one for 'leave' parameters.
        Each tuple in the list contains the bins and edges of the histogram for a feature.
        """        
        
        self.stay_params = [(None, None) for _ in range(x.shape[1])]
        self.leave_params = [(None, None) for _ in range(x.shape[1])]

        # INSERT CODE HERE
        for i in range(x.shape[1]):
            x_stay = x[y == 0, i]
            x_stay=x_stay[~np.isnan(x_stay)]
            x_leave = x[y == 1, i]
            x_leave=x_leave[~np.isnan(x_leave)]
            a,b=np.histogram(x_stay,n_bins)
            print(x_stay)
            print(x_stay.shape)
            # a=np.float(a)
            # a/=float(x.shape[0])
            # self.stay_params[i]=(a,b)
            # a,b=np.histogram(x_leave,n_bins)
            # a=np.float(a)
            # a/=float(x.shape[0])
            # self.leave_params[i]=(a,b)

        
        return self.stay_params, self.leave_params
    
    def H(self,x):
        result=(self.prior_pos/self.prior_neg)
        for i in range(len(x)):
            if x[i]<self.leave_params[i][1][0]:
                b=0
            elif x[i]>=self.leave_params[i][1][-1]:
                b=len(self.leave_params[i][1])-1
            else:
                for j in range(1,len(self.leave_params[i][1])-1,1):
                    if(self.leave_params[i][1][j-1]<x[i]<=self.leave_params[i][1][j+1]):
                        b=j
                        break
            
            result*=self.leave_params[i][0][b]
            result/=self.stay_params[i][0][b]         
        return result
    
    def predict(self, x, thresh = 0):

        """
        Predicts the class labels for the given samples using the non-parametric model.

        Parameters:
        x (np.ndarray): The feature matrix for which predictions are to be made.
        thresh (float): The threshold for log probability to decide between classes.

        Returns:
        result (list): A list of predicted class labels (0 or 1) for each sample in the feature matrix.
        """

        y_pred = []

        # INSERT CODE HERE
        for i in range(x.shape[0]):
            if self.H(x[i])>1 :
                y_pred.append(1)
            else:
                y_pred.append(0)

        return y_pred
    
    def fit_gaussian_params(self, x, y):

        """
        Computes mean and standard deviation for each feature in the dataset.

        Parameters:
        x (np.ndarray): The feature matrix, where rows are samples and columns are features.
        y (np.ndarray): The target array, where each element corresponds to the label of a sample.

        Returns:
        (gaussian_stay_params, gaussian_leave_params): A tuple containing two lists of tuples,
        one for 'stay' parameters and one for 'leave' parameters.
        Each tuple in the list contains the mean and standard deviation for a feature.
        """

        self.gaussian_stay_params = [(0, 0) for _ in range(x.shape[1])]
        self.gaussian_leave_params = [(0, 0) for _ in range(x.shape[1])]

        # INSERT CODE HERE
        for i in range(x.shape[1]):
            x_stay = x[y == 0, i]
            x_leave = x[y == 1, i]  
            self.gaussian_stay_params[i]=(np.mean(x_stay),np.var(x_stay))
            self.gaussian_leave_params[i]=(np.mean(x_leave),np.var(x_leave))
        
        
        return self.gaussian_stay_params, self.gaussian_leave_params
    
    def gaussian_predict(self, x, thresh = 0):

        """
        Predicts the class labels for the given samples using the parametric model.

        Parameters:
        x (np.ndarray): The feature matrix for which predictions are to be made.
        thresh (float): The threshold for log probability to decide between classes.

        Returns:
        result (list): A list of predicted class labels (0 or 1) for each sample in the feature matrix.
        """

        y_pred = []

        # INSERT CODE HERE

        return y_pred