# @app.route('/')
# def home():
#     return render_template('index.html')

# def render_this(predicted_method, transportation_cost, estimated_date, optimized_method):
#     test_value = "hello world"
#     return render_template('index.html', test_value=test_value,                            
#                            predicted_method=predicted_method, 
#                            transportation_cost=transportation_cost, 
#                            estimated_date=estimated_date,
#                            optimized_method=optimized_method)

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

#     pm = predicted_method
#     tc = transportation_cost
#     ed = estimated_date
#     om = optimized_method
#     print("the values are", pm, tc, ed, om)
#     print("are they strings?", isinstance(pm, int),isinstance(pm, int), isinstance(tc, int), isinstance(ed, int), isinstance(om, int) )
    
#     return render_this(predicted_method=pm,transportation_cost=tc, estimated_date=ed.strftime('%Y-%m-%d %H:%M:%S'), optimized_method=om)
