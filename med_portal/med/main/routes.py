from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from  tensorflow.keras.applications.imagenet_utils import decode_predictions

from PIL import Image
import numpy as np

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template('home.html')

@main.route("/analysis", methods=['post'])
def analysis():
    data = request.get_data()

    if data == b'':
        return jsonify('Bad request.'), 400
    print(request.files['image'])
    image =request.files['image']

    if image.filename == '':
        return jsonify('No image provided.'), 400
    
    model = load_model('retinal.h5')
    img_1 = Image.open(image)
    img = img_1.resize((150,150))
    x_ = img_to_array(img)
    x = np.expand_dims(x_, axis=0) 
    preds = model.predict(x)
    result = preds[0][0]
    if preds[0][0] > 0.5:
        return jsonify(f'High risk with chance of {str(round(result * 100))}%'), 200
    else:
        return jsonify(f'Low risk with chance of {str((round((1 - result) * 100)))}%'), 200
     
       