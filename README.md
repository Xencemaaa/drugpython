# Drug Consumption Data Analysis

Python for Data Analysis final project: Victoria Garnil, Adrien Foresier and Maxence Ferreira


This project was done on the Drug consumption (quantified) DataSet.


This set contains data on drug use in mutliple countries in world such as the UK, the US, Canada and more. The population studied in order to make this set regroups
people from different populations (education, age and sex). It is split evenly between Female and Male.
We also have informations about personnality mesurements like neuroticism, extraversion or impulsivity and sensation seeking. 


19 drugs are presented. For each, we get to know when the person used such drug last, it can be never, over a decade ago, last decade, last year, last month, last week or even the last day.
This data is represented by an output like 'CL0' for never used and 'CL6' for used the last day.
In these 19 drugs, we can find Cannabis, Cocaine, Kethamine, LSD, Meth or even chocolate and nicotine. There is also a fake drug called Sermon, created for the survey that made
this dataset. This drug was introduced to the survey in order to catch potential liars that would prejudice the machine learning models.


# Problem
How to predict drug use, and more specifically Cannabis use, according to different parameters (personal and environmental) ?

The focus is on the use or non-use of Cannabis. It is a binary problem and therefore a classification problem. 

For our study, we will consider that people that have never used or that have used drugs over a decade ago or last decade as non-user, others will be considered users.
We chose to focus on Cannabis, as there is almost the same number of people that have used it than people that have never used it. 
We would like to predict wheter or not a person consumes Cannabis. That is why we have trained multiple machine learning models with Sklearn:

	Support Vector Machine Learning
	Gradient Boosting
	XGBoost
	Bagging Classifier
	Extra Trees Classifier


# Conclusion
To conclude, we are able to predict with a best score of 0.8 that a personne consumes or not Cannabis. The best model will vary but, the score pretty much stays the same. By choosing the
best hyperparameters we are capable of maximizing the best score.


The dataset: https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29
