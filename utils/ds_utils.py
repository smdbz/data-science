# Utils file containing useful classes and functions to help with the data science lifecycle


# The iterative loop of the machine learning development process.

# 1. What is the overall architecture of your system?
    # Choose your machine learning problem type (classification, regression, clustering).
    # Pick hyperparameters for your model.
    # Pick the data/features the model should be trained on.

# 2. Train your model on the training set.

# 3. Diagnostics (bias, variance, error analysis)
#   Decide if your model has high bias or high variance, this will tell you what to focus on to improve your model the most

from abc import ABC, abstractmethod



class LinearExploratoryDataAnalysis:
    """
    Class for making sure all the EDA steps are followed for a linear problem


    """
    def __init__(self):
        self.data = None
        self.eda_results = None
