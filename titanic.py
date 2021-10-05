from flask import Flask, jsonify, request
import numpy as np
from tensorflow.keras.models import load_model

# initialize our Flask application and the Keras model
app = Flask(__name__)
model = None

@app.route('/predict', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():
    if model:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)

            prediction = list(model.predict(query))

            return jsonify({'prediction': prediction})

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
	app.run(port=port, debug=True)