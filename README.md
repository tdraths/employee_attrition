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

*Sales Reps have the highest rate of attrition, but also have one of the lowest overall counts in the data set*
![Attrition by Job Role](https://user-images.githubusercontent.com/64986521/123562315-f2eb1380-d7a5-11eb-8535-d1d37394511f.png)

*Single employees have a much higher rate of attrition than married or divorced employees*
![image](https://user-images.githubusercontent.com/64986521/123562520-1f535f80-d7a7-11eb-857d-58b770ed1075.png)

*Younger employees below the age of 30 tend to have a higher rate of attrition than employees over 30.*
![image](https://user-images.githubusercontent.com/64986521/123562565-5b86c000-d7a7-11eb-9d1d-27779189859b.png)

*Employees with a longer commute tended to have a higher rate of attrition than employees with a shorter commute*
![image](https://user-images.githubusercontent.com/64986521/123562577-79542500-d7a7-11eb-9c22-a36781786a63.png)

*Employees who lacked a stock option plan in their compensation tended to have a much higher attrition rate than those with a stock option plan*
![image](https://user-images.githubusercontent.com/64986521/123562597-9db00180-d7a7-11eb-8597-7efad0308ae5.png)


A good chunk of the features were designed to look like survey responses, e.g. rating one's job satisfaction on a 1 to 4 scale. Features with this characteristic had a predictable attrition rate distribution - the lower the 'survey response,' the higher the attrition rate.

For more of the visualizations, have a look at the notebook. If anything jumps out at you, let me know!

Finally, I looked at feature correlations with that ever-useful correlation map:
![image](https://user-images.githubusercontent.com/64986521/123562662-fa132100-d7a7-11eb-8848-742d5f159e38.png)


### Preprocessing & Algorithms
This is the second part of the project that I contributed a lot of focus toward. I have not done a classification project before, and I put focus on choosing the right algorithm for my project and on tuning parameters to improve my classification scores.

I used LabelEncoder from sklearn.preprocessing to encode my categorical data, and then split my data into training / test sets. I used the MinMax Scaler to scale the data, and then built a function to help me fit the data to the following algorithms:

Model Name | ROC AUC Mean | ROC AUC StDev | Accuracy Mean | Accuracy StDev
---------- | ------------ | ------------- | ------------- | --------------
SVM | 81.52 | 8.53 | 83.84 | 2.64
Logistic Regression | 80.06 | 8.47 | 73.73 | 4.15
XGBoost Classifier | 79.37 | 7.64 | 87.33 | 2.56
Random Forest Classifier | 78.51 | 8.57 | 86.05 | 2.76
Gaussian NB | 75.85 | 8.97 | 76.79 | 4.44
KNN | 71.00 | 6.38 | 84.10 | 1.70
Decision Tree Classifier | 60.25 | 4.16 | 78.31 | 2.25


I used the ROC AUC Mean score to assess each model. The area under the ROC curve is a good performance metric for binary classification. In the table above, a score of 100 would be a perfectly predictive model, while a score closer to 50 means the model is as good as a random classification. I moved ahead to the next stage of modelling with the three best AUC mean scores: **Support Vector Classification**, **Logistic Regression**, & **XGBoost Classifier**. 

**Note:** After doing some research into employee attrition and predictive modelling, I discovered that Logistic Regression is generally regarded as the wrong algorithm for employee attrition models. 

### Tuning Parameters
I went through tutorial after tutorial to learn how to tune algorithm parameters, and I'm happy with the progress in this project! The code I used is in the notebook, but here are the results:

#### ***Support Vector Machine Classifier***

![image](https://user-images.githubusercontent.com/64986521/123563200-4875ef00-d7ab-11eb-95e7-737b4e18f357.png)

#### ***Logistic Regression***

![image](https://user-images.githubusercontent.com/64986521/123563248-896e0380-d7ab-11eb-9592-82b9fb026309.png)

#### ***XGBoost Classifier***

![image](https://user-images.githubusercontent.com/64986521/123563295-dd78e800-d7ab-11eb-8c4f-83f183c1cac3.png)



### Feature Importances & SHAP Values
From the results above, I selected XGBoost as my optimal algorithm. It not only had the highest ROC AUC mean score, but it also showed the best improvement in score from baseline through parameter tuning. Onto exploring the features with SHAP values! [Here](https://towardsdatascience.com/shap-explained-the-way-i-wish-someone-explained-it-to-me-ab81cc69ef30) is a great explanation for what exactly SHAP values are, and [here](https://towardsdatascience.com/explain-your-model-with-the-shap-values-bc36aac4de3d) is a great example for how to use them! Super helpful stuff. If you want to do a bit of learning, here is the [documentation on github](https://github.com/slundberg/shap).

***Shap values***

![image](https://user-images.githubusercontent.com/64986521/123563582-7a885080-d7ad-11eb-997e-3361bfbfac4e.png)


***Impact of a higher or lower feature value on model output***
![image](https://user-images.githubusercontent.com/64986521/123563613-a277b400-d7ad-11eb-83fa-927f710e1f6e.png)


Overtime is a very important feature in this data set, and is one of the more predictive of employee attrition of all the features we have. I used SHAP values to isolate overtime into two cohorts, with values equal to or above .5 and values below .5 . The following image shows the impact of an overtime value within those two ranges:

***Overtime is highly predicitve of employee attrition***
![image](https://user-images.githubusercontent.com/64986521/123563731-35185300-d7ae-11eb-8f2f-8b4ffe308e0f.png)


### Conclusion & Next Steps
This is my second major machine learning project, and I am really happy with the results! I learned a lot taking on this problem; I did a lot of outside research to build some of the functions used in this notebook, and into using SHAP values to explain predictability. As I mentioned above, my former role involved strategies to minimize overhead costs in hiring and onboarding, and the results from this project would have been helpful to know!

**A few takeaways, lessons learned, and future steps:**
- Based on this dataset, overtime is highly predictive of employee attrition. In this dataset, employees either **had** overtime (1) or **did not** have overtime (0). In the real world, overtime is unlikely to be classified so easily. If I revisit this project, I'd examine data that has more realistic values, but in this case it is safe to say that employees with overtime are more likly to leave work for a new opportunity than those without overtime.
- There are seven feautures in this dataset that had feature importances within a good range of each other: job role, stock option level, number of companies worked, age, environment satisfaction, monthly income, and distance from home. Employers should be aware of these impactful factors in employee attrition, and manage both company and employee expectations given higher or lower values for each of these seven features. For instance, a younger employee with a low income level and longer commute is highly likely to leave a company, compared to other employees. This may seem like common sense, but it can be difficult for people managers to be aware of these factors when managing their employees and planning hiring strategies.
- SHAP values are an easy-to-use tool to explain predictability, and I'll continue to expand understanding of how to apply them to projects.
- I learn better by pinpointing one or two steps in a project, and building skills that help manage those steps. It doesn't mean doing the rest of the project halfway; it just helps me focus on skills I want to improve.
- Mentors are easily the most helpful 'skill.' I've worked with Rafa Castillo on two projects, and his encouragement, tips and overall positivity help me stay focused when I am stuck on a problem. Tip for other newbies like me: get a mentor.


I hope you enjoyed this project brief; I am happy to take on advice if you have any to share!
