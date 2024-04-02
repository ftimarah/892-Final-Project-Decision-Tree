from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load the trained decision tree model
model = joblib.load('decision_tree_model.joblib')

# Load the column names used during training for reference
column_names = joblib.load('column_names.joblib')

# Define a function to preprocess input data and make predictions
def predict_transportation(data):
    # Convert the input JSON data into a DataFrame
    features = pd.DataFrame(data, index=[0])

    # Perform one-hot encoding for categorical variables
    features_encoded = pd.get_dummies(features)

    # Reorder columns to match those seen during training
    features_encoded = features_encoded.reindex(columns=column_names, fill_value=0)

    # Make prediction
    predicted_method = model.predict(features_encoded)

    # Calculate transportation cost based on distance and urgency
    distance = data['distance']
    urgency = data['urgency']
    distance = int(distance)
    
    if urgency == 'High':
        print("distance type int and value ", isinstance(distance, int), distance)
        transportation_cost = distance * 0.05
        
    elif urgency == 'Medium':
        transportation_cost = distance * 0.03
    else:
        transportation_cost = distance * 0.02

    return predicted_method[0], transportation_cost

# Function to estimate delivery dates
def estimate_delivery_date(distance, urgency):
    # Sample logic to estimate delivery dates based on distance and urgency
    distance = int(distance)
    days_per_km = 0.1  # Sample average delivery days per kilometer
    if urgency == 'High':
        days_per_km /= 2  # Urgent deliveries are faster
    elif urgency == 'Low':
        days_per_km *= 2  # Low urgency deliveries take longer
    estimated_days = distance * days_per_km
    return datetime.datetime.now() + datetime.timedelta(days=estimated_days)

# Function to optimize transportation means
def optimize_transportation_method(destination):
    # Sample logic to optimize transportation method based on destination
    if 'US' in destination:
        return 'Truck'
    elif 'JP' in destination:
        return 'Airplane'
    elif 'UK' in destination:
        return 'Ship'
    else:
        return 'Train'

# Define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from JSON request
    data = request.get_json()
    print("data is ", data)
    # Make prediction
    predicted_method, transportation_cost = predict_transportation(data)
    print("predicted method, transportation_cost ", predicted_method, transportation_cost)
    
    # Estimate delivery date
    estimated_date = estimate_delivery_date(data['distance'], data['urgency'])
    print("Estimated date ", estimated_date)
    
    # Optimize transportation method
    optimized_method = optimize_transportation_method(data['endLocation'])

    print("optimized method ", optimized_method)
    
    # Render the result.html template with prediction results
    render = render_template('result.html', 
                           predicted_method=predicted_method, 
                           transportation_cost=transportation_cost, 
                           estimated_date=estimated_date.strftime('%Y-%m-%d %H:%M:%S'),
                           optimized_method=optimized_method
                           )

    print("render", render)
    
    return render
# @app.route('/result')

# def result():
#     # This route is just a placeholder to render the result.html template
#     # The actual prediction results are passed from the '/predict' route
#     return render_template('result.html')


# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get input data from JSON request
#     data = request.get_json()
#     print("data is ", data)
#     # Make prediction
#     predicted_method, transportation_cost = predict_transportation(data)
#     print("predicted method, transportation_cost ", predicted_method, transportation_cost)
    
#     # Estimate delivery date
#     estimated_date = estimate_delivery_date(data['distance'], data['urgency'])
#     print("Estimated date ", estimated_date)
    
#     # Optimize transportation method
#     optimized_method = optimize_transportation_method(data['endLocation'])

#     print("optimized method ", optimized_method)
    
#     # Render the result.html template with prediction results
#     return render_template('result.html', 
#                            predicted_method=predicted_method, 
#                            transportation_cost=transportation_cost, 
#                            estimated_date=estimated_date.strftime('%Y-%m-%d %H:%M:%S'),
#                            optimized_method=optimized_method)

if __name__ == '__main__':
    app.run(debug=True, port=3000)