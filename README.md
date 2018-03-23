# FoodInspection
Project Work for MSiA 423


## Project Charter
Provide a Food Inspection outcome prediction to Chicago restaurateurs, based on their restaurant characteristics. Our data is pulled from the City of Chicago Data Portal.

Team 3: Wenjing Yang (QA) ; Jamie Chen (PM)

Link to PivotalTracker: <a href=“https://www.pivotaltracker.com/n/projects/2144206”></a>

Vision: Assist the decision process for Chicago restaurateurs in deciding how to best prepare for their upcoming Food Inspection. Mission: Use historical outcome data to build a classification model, which uses the most important characteristics of an inspection, to predict an outcome (pass or fail) for a restaurant. Success Criteria: Whether or not the model’s results are intuitive, and whether or not it performs better than the baseline.

To explore more about the Food Inspection data made available by the City of Chicago Data Portal’s API, visit this site: <a href=“https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5”></a>

## Steps to deploy app

1) Clone repo
2) Create an environment to run app from:
```
virtualenv -p python3 FoodApp
source FoodApp/bin/activate
```
Then install the requirements file:
```
pip install -r requirements.txt
```
3) Create config file with SQL database path:
```
SQLALCHEMY_DATABASE_URI  = '<URI for the database you will be using>'
```
4) Run prepare_app.py to pull data, create database, and train model. Run this every time you want to update the data and retrain the model.
5) Run FoodApp.py
