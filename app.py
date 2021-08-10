# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'model.pkl'
classifier = pickle.load(open(filename, 'rb'))
classifier 
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        store = int(request.form['Store'])
        holiday_flag = int(request.form['Holiday_Flag'])
        temp = float(request.form['Temperature'])
        Fuel_Price = int(request.form['Fuel_Price'])
        CPI= int(request.form['CPI'])
        Unemployment = float(request.form['Unemployment'])
        Year = float(request.form['Year'])
        Month = int(request.form['Month'])
        
        data = np.array([[store,holiday_flag,temp,Fuel_Price,CPI,Unemployment,Year,Month]])
        prediction = classifier.predict(data)
        output = round(prediction[0],2)
    
        return render_template('index.html',prediction_text = 'Dmart sales preicator {} Rs'.format(output))

        
        
if __name__ == '__main__':
	app.run(debug=True)








