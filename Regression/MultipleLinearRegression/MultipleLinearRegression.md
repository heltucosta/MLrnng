# Multiple Linear Regression
* Linear regression where multiple variables influence the final result of the dependent variable;
* Equantion of the formulae: y = b0 + b1.x1 + b2.x2 + ... + bn.xn
* variable amount of Independent variables;
* Linear Regression models have some assumptions that should be checked for its validity before the models is developed for the given dataset. Those are:
  1. Linearity
  2. Homoscedasticity
  3. Multivariate normality
  4. Independence of errors
  5. Lack of multicollinearity
* Just as we did in the Simple Linear Regression session, when creating regression models where the rolls are represented by text (categorical columns), we have to use _dummy variables_ just as mentioned before;
* Dummy variables are a matrix representation of a column, where for every row on the matrix, only one column will have the number **1** which is representing the text before, the other columns will be **0**;
![Dummy Variables Exemplification](DummyVariables.jpg)
