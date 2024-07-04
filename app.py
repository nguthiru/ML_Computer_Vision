from flask import Flask, request, jsonify
from PIL import Image
import tensorflow as tf
import numpy as np
from io import BytesIO
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


model_path = './model/CNN_Model.h5'
loaded_model = tf.keras.models.load_model(model_path, compile=False)
loaded_model.compile(optimizer=tf.keras.optimizers.Adamax(learning_rate=0.001), 
                     loss='categorical_crossentropy', 
                     metrics=['accuracy'])


class_labels = ['Colon Adenocarcinoma', 'Colon Benign Tissue', 'Irrelevant Image', 'Lung Adenocarcinoma', 'Lung Benign Tissue', 'Lung Squamous Cell Carcinoma']
@app.route('/predict', methods=['POST'])
@cross_origin()

def predict():

    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    
  
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No image file provided'}), 400

    try:

        image = Image.open(file.stream)

        img = image.resize((224, 224))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)


        predictions = loaded_model.predict(img_array)
        score = tf.nn.softmax(predictions[0])
        predicted_class = class_labels[np.argmax(score)]

        return jsonify({'predicted_class': predicted_class})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
