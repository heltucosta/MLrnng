# Support Vector Regression
* Fast and accurate way of interpolating data sets;
* It is useful when you have an expensive functions you want to approximate over a known domain;
* It learns quickly and is systematically improvable;
* There are variants, like _Krigging_ and _Gaussian_;
* Generalization of the _Support vector machine_ to regression problems;
* Can be labelled as a supervised learning algorithm;
* Requires a training set in order to approximate the functions used to generate the training set;
* Vectors are used to perform linear regression;
* The closest vector to the test point is the one that will be used;
* Performs linear regression in a higher dimensional space
* When we evaluate our kernel through all points, we are representing the test point in a higher dimension;
* You can tell it's a linear regression by the existence of a inner product;
* Provides cheap surrogate for expensive calls;

## Steps
1. Collect training set (X and y);
  * Samples collected to train the machine;
  * Should span the domain we want to evaluate;(0~2pi for cosine)
  * When evaluating out of domain, results will vary depending on kernel and optimization routine;
2. Choose kernel and parameters, as well as any regularization;
  * Multiple choices: Gaussian, Laplacian, polynomial, sigmoid, radial basis, etc;
  * Each kernel will have its own set of parameters to be trained;
  * Training is the most expensive part of SVR technique;
  * The kernel choice will dictate how the model will behave for marginal cases (not on the training set). For gaussian it will be the average, for polynomials it can be a really large number;
  * For training sets with some noise, regularizers helps preventing wild fluctuations between data points by smoothing them out;
3. Create the correlation matrix;
  * Evaluate the kernel for each pair of points and then add the regularizer;
4. Train the machine, to get contraction coefficients;
  * All linear algebra;
  * the meat of the algorithm;
  * Solve matrixes to get coefficients;
5. Create the simulator from the coefficients;
  * With the coefficients and kernel defined, it's a straightforward proces;
  * Estimate value of a test point is the inner product of the coefficients vector with the correlation matrix;
  * Only add the mean value of the training set when the estimator is done; makes it easier for the algorithm to interpolate differences;


