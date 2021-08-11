import os
from flask import Flask,jsonify, request
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from PIL import Image
import io


app = Flask(__name__)
model = load_model('./model')

@app.route('/detect',methods =['POST'])
def detect():
    if request.method == 'POST':
        if request.files.get('image'):
            img = request.files['image'].read()
            img = Image.open(io.BytesIO(img))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = img.resize((224, 224))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0)
            inputs = preprocess_input(img)
            result = model.predict(inputs)
            res = "Truck" if result > 0.5 else "Ship"
            confidence = abs(result[0][0] - 0.5)/0.5
            return jsonify({"class" : res, "confidence" : confidence})


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
