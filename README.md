# Problem Statement
 
Backorders are unavoidable, but by anticipating which things will be backordered,
planning can be streamlined at several levels, preventing unexpected strain on
production, logistics, and transportation. ERP systems generate a lot of data (mainly
structured) and also contain a lot of historical data; if this data can be properly utilized, a
predictive model to forecast backorders and plan accordingly can be constructed.
Based on past data from inventories, supply chain, and sales, classify the products as
going into backorder (Yes or No).

# Process Flow
1.   First we cleaned our dataset properly by removing all null value and duplicate value present in dataset.
2.   Performed EDA on whole data set. Did type conversion of some columns .Tried to find the pattern
3.   Then I handled categorical variable by performing One-Hot encoding.
4.   With the help of Correlation plot we found that Sales(3,6,9 month), Forecast(3,6,9) and Performance(6,9) columns were heavily correlated.Hence dropped some columns from those
5.   Since data was highly imbalance, performed sampling on data
6.   Then I split the hole data set train-test split. After that I performed scaling on X_train and X_test
7.   After performing above step I was ready for model training. In this step, I trained my dataset on different algorithm(Logistic, Random-Forest, SVM,
     DecisionTreeRegression,Random-Forest and XGB). After training the dataset on different algorithms I got highest accuracy of 83% on XGB Classifier.
8.   After that I applied hyper-parameter tuning on all model which I have described above. 
9.   After that I saved my model in pickle file format for model deployment.
10.  After that my model was ready to deploy. I deployed this model on variouscloud storage( heroku)



# Technology Used
1. Python 
2. Sklearn
3. Flask
4. Html
5. Css
6. Pandas, Numpy 
7. Database 

# How to run this app    
1.  Code is written in Python 3.9. If you don't have python installed on your system, click here https://www.python.org/downloads/ to install.
2.  Create virtual environment - conda create -n myenv python=3.9
3.  Activate the environment - conda activate myenv
4.  Install the packages - pip install -r requirements.txt
5.  Run the app - python app.py


# Output
![op](https://user-images.githubusercontent.com/60249099/132537128-63f2fa51-cef1-4041-8bec-b831ffe40c04.PNG)

# Database(MongoDB)
![db](https://user-images.githubusercontent.com/60249099/132537356-fd9a07fe-40ef-4c3c-be38-96150532a8eb.PNG)


# Heroku Deployment Link:
https://backorder1.herokuapp.com/

# Linkedin
https://www.linkedin.com/feed/update/urn:li:activity:6841362356040278016/
