# Recommendation Sys using MovieLens Data set
Project on eCommerce recommender system using the Movie Lens data set. Using machine learning algorithms, the system should be able to recommend a list of items to the user based on the reviews provided by other users, product descriptions and user's own history. Python is used for this purpose.

[Exploratory Data Analysis](/EDA_and_Cleaning.ipynb) is done to understand the data set. Histograms, boxplots, scatterplots are created. Statistical analysis is performed and detailed descriptive analysis is performed.
Missing values & outliers are identified and dealt with appropriately.

The data set is splitted into trianing and test sets. User based collaborative filtering and content based collaborative filtering models are developed using 2 data sets : 100K and 1M Movie Lens data set.

The code is in various Python files to maintain the modularity and reusability of the code. The program is developed in such a way that integrating new approaches could be possible in short span of time.

These approaches are tested and evaluated against the test set. Precision, Recall and Coverage is used to measure the preformance of the system. This system is capable of recommending movies to a set of users based on the ratings given by these users and also the movies rated by other users.

There can be more advanced approaches to improve the efficiency of the recommendations such as Hybrid Approach, Sequence based approach etc.

