# Predicting Employee Attrition

In my previous work, I built and managed sales teams for a higher education tech firm. It was a fast-growing business, and my teams grew in both overall number and headcount per team as the company expanded. A big part of the role included partnering with Human Resources and Recruiting to plan, as best as we could, a strategy for managing my team headcounts. Hiring, onboarding and training new employees has high overhead costs, and with the rise in HR Analytics, firms are putting more resources into managing the data behind their employees. With all of this new data, can a firm build a model to predict employee attrition, and better distribute resources as a result?

### Problem:
Given a set of employee data, can I build a model to predict employee attrition?


### Data Sourcing & Cleaning
The data is sourced from [Kaggle](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset). It is a 'fictional' dataset, and while I do not know if there is a consensus on using fictional data sets, for this project, it suited my purposes well. It was created by the IBM Watson team for their HR Analytics function; it did not require much beyond basic cleaning, and I was able to focus more of my time on developing a model, which was the primary focus of this project.

The dataset has no missing values, and originally had 35 features which I reduced that number down to 28. One column was a unique identifier for each employee, so I dropped it from the dataset. Three columns had only one unique value through the column, so I removed them as well. Finally, there were four income-related columns, three of which lacked a clear definition. I decided to keep the well-defined column 'MonthlyIncome' and remove the rest. This left me with 28 features adn 1470 observations.

The target variable 'Attrition' contained 'Yes' and 'No' values, which I coded to be 'Yes' = 1 = employee left company and 'No' = 0 = employee stayed at company. Overtime was similarly coded to 'Yes' = 1 and 'No' = 0.

Of the 28 features, I had one target variable, five categorical features and 22 numerical features. Check the notebook for the full line-up.

### Visualizing the Data
I wanted to use this project to improve my EDA and modelling abilities. To visualize the data, I used functions created by Rafa Castillo and adapted them to my data. Check them out in the notebook. Some of the more interesting observations follow below:

![Attrition by Job Role](https://user-images.githubusercontent.com/64986521/123562315-f2eb1380-d7a5-11eb-8535-d1d37394511f.png)
*Sales Reps have the highest rate of attrition, but also have one of the lowest overall counts in the data set*
