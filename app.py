from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

# Load the cleaned data CSV
data = pd.read_csv('Cleaned_GlobalWeather.csv')

# Define an endpoint to retrieve the whole dataset
@app.route('/api/data', methods=['GET'])
def get_data():
    # Optionally, filter data by query parameters (e.g., country, date)
    country = request.args.get('country')
    date = request.args.get('date')

    filtered_data = data
    if country:
        filtered_data = filtered_data[filtered_data['country'] == country]
    if date:
        filtered_data = filtered_data[filtered_data['last_updated'].str.contains(date)]

    return jsonify(filtered_data.to_dict(orient='records'))

# Run the Flask server
if __name__ == '__main__':
    app.run(debug=True)
