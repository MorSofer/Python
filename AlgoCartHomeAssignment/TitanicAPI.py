from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import traceback
import pandas as pd
import numpy as np
import joblib

# initialize our Flask application and the Keras model
app = Flask(__name__)
model = None

@app.route('/predict', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():
	if model:
		try:
			json_ = request.json
			query = pd.get_dummies(pd.DataFrame(json_, index=[0]))
			query = query.reindex(columns=model_columns, fill_value=0)
			
			prediction = model.predict(query).astype('float32')
			
			
			if prediction >= 0.5:
				return jsonify({'survive': "YES"})
			else: 
				return jsonify({'survive': "NO"})
		except:
			return jsonify({'trace': traceback.format_exc()})
	else:
		print ('Train the model first')
		return ('No model here to use')

if __name__=='__main__':
	port = 8080 
	print("loading titanic NN model")
	model = load_model('titanic.h5')
	print("titanic NN model loaded")
	model_columns = joblib.load("model_columns.pkl")
	app.run(port=port, debug=True)
