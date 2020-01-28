from flask import Flask,render_template,request,redirect,jsonify
import os
from keras.models import load_model
import tensorflow as tf
from keras_preprocessing.image import img_to_array
from PIL import Image
graph = tf.get_default_graph()

app = Flask(__name__)
modelData = load_model('/home/mubashir/deep_learning_with_python/vs_code/vscode/class8/cats_and_dogs_small_1.h5')

@app.route('/',methods=["POST","GET"])
def index ():
    data = request.files
    img = Image.open(data['image'])
    img=img_to_array(img)
    img=img.reshape((1,)+img.shape)
    img=img/255
    with graph.as_default():
        prediction=modelData.predict(img)
        if prediction  < .5:
            return jsonify({"success":True,"name":'cat'})
        else:
            return jsonify({"success":True,"name":'dog'})
    return jsonify({"success":False})

# @app.route('/form')
# def form():
#     return request.form

if __name__ == "__main__":
    app.run(debug=True)
