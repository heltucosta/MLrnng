# Importing libraties
* **numpy** for fast numerical operations with array;
* **pandas** for working with multiple datasets;
* **matplotlib** for data visualization.

# Importing Datasets
* set the working directory for the python environment, making sure the dataset file is accesible (when using flat-storage files);
* Can be accomplished by starting python on the wanted folder, or you can use python standard **os** library to change the working directory;
* When working with databases, you can connect to it using python's sql libraries and read the query into a pandas **DataFrame**
* In machine learing datasets, it is important to undersant which columns represent the **matrix of features** and which represent the **dependent variable vector**.
* **Matrix of features** are independent variables represented in the dataset, or the features that characterize the behavior we want to _learn_, the **dependent variable vector**;
* To separate the pandas DataFrame into the selected columns we can use the **iloc** method.

# Dealing with missing data
* Options: remove the lines, take the mean or median or take the most common value
* Remove the entire line of the missing data is error prone since it can remove critical data from the dataset;
* Taking the mean or median is one of the best and most accepted method of dealing with this data, not adding too much noise to the data;
* Using the most common value is an acceptable solution for low-end applications, whereas it can create significant skew when dealing with sensitive data.
* To replace the missing value with the mean/median, we can use the **Imputer** clas from the **Sci-kit learn** library for python;
* The imputer parameter are the missing values, the strategy that will be used and the axis at which it will be applied (the standard strategy is always 'mean');
* After that, we need to _fit_ our imputer object to the matrix of features of the dataset we want to fix the missing data issues;
* Finnaly, all we need to do is update our matrix of features with the transform from the imputter.
* The available strategies available in the 'Imputer' class are: 'mean', 'median' and 'most_frequent';

# Identifying/Encoding Categorical Data
* Machine learing models are based on mathematical equations, so columns that are represented by texts need to be categorized and represented as numbers;
* Can be achieved by utilizing the **LabelEncoder** class from the Sci-Kit learn library, fit it to the the column we want to encode;
"""
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
"""
* This process encodes the categorized data in a crescent fashion, giving us the ability of comparing them one to the other. When this process does not make sense, we can use a new process of encoding, called **Dummy Encoding**;
* **Dummy Encoding** is the process of creating an encoder matrix for each category available in the categorical column. The same amount of categories will be the amount of columns of the new matrix, where each column represents a category and only one of them for a dataset row will have a value;

* This process of Dummy Encoding can be achieved by using the **OneHotEncoder** class from the Sci-Kit learn library;
"""
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
"""

# Training and Testing Sets
* When creating machine learning models, we always want to separate the datasets in two parts, the **training set** and the **testing set**;
* Build the models in one set, and test the model on another set, making sure that the connections were created and evaluating the accuracy of our model;
* can be achieved by using the **train_test_split** of the **sklearn.croo_validation** library;
* X_train, X_test, y_train, y_set = train_test_split(X, y, test_size=0.2) # usually 0.2~0.5;
* Attribute **random_state** for random sampling. Good value is about 40;
* The machine learing model understands the correlation between the matrix of features and the dependent variables using the training set, and them we measure the accuracy of our model using the testing set;

# Feature Scaling
* Numerical variables are rarelly on the same size scale of the others;
* Machine learing models equations uses **Euclidean's distances**, and they will always become dominates by the numerical variables that are larger (because of the square's distance);
* Several ways to scale the data, but usually we will use **Standardization** or **Normalisation**;
* **Standardization** for each observation and feature, withdrawl the mean from them and divide the result by the standard deviation;
* **Normalisation** for each observation and feature, withdraw the minimun value from them, dividing this result by the difference from the minimun and the maximun value;
* No matter the process, the goal is to put all the variables on the same range and scale, making sure that no one will dominate the other;
* can be achieved by using the **StandardScaler** class from the **sklearn.preprocessing** library;
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train) # Fit and Transform for training
X_test = sc_X.transform(X_test) # Transform only for testing
'''
* We generally only fit the training set because the scaler is already fitted to the variables;

