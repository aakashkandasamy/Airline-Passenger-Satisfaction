# Machine Learning Model for Airline Passenger Ratings
This is a machine learning model that is trained on data from airline passenger ratings. It can give accurate customer ratings depending on how good the amenities of the plane are. The model takes in a variety of factors such as seat comfort, in-flight entertainment, food and beverages, etc. to predict a rating. 

## Dataset
The dataset used to train this model is publicly available and was obtained from [Kaggle](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction). It includes more than ***100,000*** sets of data contains features such as the gender, age, type of travel, seat comfort and in-flight entertainment to name a few. This dataset was cleaned up for proper usage and was then used as a training for out machine learning model, to ensure only the most effective variables are taken into account. 

## Model
The machine learning model used in this project is a regression model trained on the dataset mentioned above. It uses a variety of features such as the in-flight amenities to predict a rating.

## Web App
Alongside this machine learning model, a web application has been developed to provide a user-friendly interface for users to interact with the model. The app allows users to input various factors to obtain a predicted rating. Additionally, the app provides comparisons to other flights' data, allowing users to make informed decisions about their flights.

## Installation and Usage
To use this machine learning model and web app, follow the steps below:

* Clone this repository  
* Install the required packages by running pip install -r requirements.txt  
* Make a folder called .streamlit to store the config.toml file (Note: This is only for the theme and can be ignored)
* Run the web app by executing streamlit run app.py in your terminal  
* Use the interface to input your flight details and obtain a predicted customer rating  

## Conclusion
This machine learning model and web app provide a useful tool for customers to make informed decisions about their flights. With accurate predictions and easy-to-use interface, it allows for a smooth user experience.

### Sample Video of the program:


https://user-images.githubusercontent.com/67540149/228393543-f2c7d1b6-f4b3-49ff-95d1-0404ecf41a4e.mov

