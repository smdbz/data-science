# Linear Algebra

Linear algebra is used to solve systems of linear equations.

1.1.1. Ordinary Least Squares
LinearRegression fits a linear model with coefficients

to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation. Mathematically it solves a problem of the form:
../_images/sphx_glr_plot_ols_ridge_001.png

LinearRegression takes in its fit method arguments X, y, sample_weight and stores the coefficients

of the linear model in its coef_ and intercept_ attributes:

from sklearn import linear_model