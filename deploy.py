#Import necessary libraries
from flask import Flask, render_template, request

import numpy as np
import os

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

filepath = 'Models/1'
model = load_model(filepath)
print(model)

def pred_disease(fruit):
    
    test_image = load_img(fruit, target_size = (256, 256))  # load image 
    print("@@ Got Image for prediction")
    
    img_array = img_to_array(test_image)  # convert image to np array and normalize
    img_array = np.expand_dims(img_array, axis = 0) # change dimention 3D to 4D
    
    result = model.predict(img_array) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    
    pred = np.argmax(result, axis=1)
    
    print(pred)
    
    if pred==0:
        return "Apple_Black_rot", '1.html'
    
    elif pred==1:
        return "Apple_Blotch_Apple", '2.html'
    
    elif pred==2:
        return "Apple_Cedar_Rust", '3.html'
    
    elif pred==3:
        return "Apple_Healthy", '4.html'
    
    elif pred==4:
        return "Apple_Rotten", '5.html'
    
    elif pred==5:
        return "Apple_Scab", '6.html'
    
    elif pred==6:
        return "Banana_Anthracnose", '7.html'
    
    elif pred==7:
        return "Banana_Aphids", '8.html'
    
    elif pred==8:
        return "Banana_Healthy_Banana", '9.html'
    
    elif pred==9:
        return "Banana_Panama_Disease", '10.html'
    
    elif pred==10:
        return "Banana_Pseudostem_Weevil", '11.html'
    
    elif pred==11:
        return "Banana_Rotten_Banana", '12.html'
    
    elif pred==12:
        return "Banana_Scarring_ Beetle", '13.html'
    
    elif pred==13:
        return "Citrus_Black_Spot", '14.html'
    
    elif pred==14:
        return "Citrus_Canker", '15.html'
    
    elif pred==15:
        return "Citrus_Greening", '16.html'
    
    elif pred==16:
        return "Citrus_Healthy", '17.html'
    
    elif pred==17:
        return "Citrus_Mellanose", '18.html'
    
    elif pred==18:
        return "Citrus_Scab", '19.html'
    
    elif pred==19:
        return "Cucumber_Anthracnose", '20.html'
    
    elif pred==20:
        return "Cucumber_Bacterial_Wilt", '21.html'
    
    elif pred==21:
        return "Cucumber_Belly_Rot", '22.html'
    
    elif pred==22:
        return "Cucumber_Downy_Mildew", '23.html'
    
    elif pred==23:
        return "Cucumber_Gummy_Stem_Blight", '24.html'
    
    elif pred==24:
        return "Cucumber_Heathy", '25.html'
    
    elif pred==25:
        return "Cucumber_Pythium_Fruit_Rot", '26.html'
    
    elif pred==26:
        return "Grape_Anthracnose", '27.html'
    
    elif pred==27:
        return "Grape_Black_rot", '28.html'
    
    elif pred==28:
        return "Grape_Esca_(Black_Measles)", '29.html'
    
    elif pred==29:
        return "Grape_Healthy", '30.html'
    
    elif pred==30:
        return "Grape_Leaf_blight_(Isariopsis_Leaf_Spot)", '31.html'
    
    elif pred==31:
        return "Guava_Healthy", '32.html'
    
    elif pred==32:
        return "Guava_Phytopthora", '33.html'
    
    elif pred==33:
        return "Guava_Red_Rust", '34.html'
    
    elif pred==34:
        return "Guava_Rotten", '35.html'
    
    elif pred==35:
        return "Guava_Scab", '36.html'
    
    elif pred==36:
        return "Guava_Stylar_end_Rot", '37.html'
    
    elif pred==37:
        return "Mango_Anthracnose", '38.html'
    
    elif pred==38:
        return "Mango_Bacterial_Canker", '39.html'
    
    elif pred==39:
        return "Mango_Healthy", '40.html'
    
    elif pred==40:
        return "Mango_Powdery_Mildew", '41.html'
    
    elif pred==41:
        return "Mango_Rotten", '42.html'
    
    elif pred==42:
        return "Mango_Sooty_Mould", '43.html'
    
    elif pred==43:
        return "Papaya_Anthracnose", '44.html'
    
    elif pred==44:
        return "Papaya_Black_Spot", '45.html'
    
    elif pred==45:
        return "Papaya_Healthy", '46.html'
    
    elif pred==46:
        return "Papaya_Phytophthora", '47.html'
    
    elif pred==47:
        return "Papaya_Powdery_Mildew", '48.html'
    
    elif pred==48:
        return "Papaya_Ring_Spot", '49.html'
    
    elif pred==49:
        return "Strawberry_Angular_Leafspot", '50.html'
    
    elif pred==50:
        return "Strawberry_Anthracnose_Fruit_Rot", '51.html'
    
    elif pred==51:
        return "Strawberry_Blossom_Blight", '52.html'
    
    elif pred==52:
        return "Strawberry_Gray_Mold", '53.html'
    
    elif pred==53:
        return "Strawberry_Leaf_Spot", '54.html'
    
    elif pred==54:
        return "Strawberry_Powdery_Mildew", '55.html'
    
    elif pred==55:
        return "Tomato___Bacterial_spot", '56.html'
    
    elif pred==56:
        return "Tomato___Early_blight ", '57.html'
    
    elif pred==57:
        return "Tomato___Late_blight", '58.html'
    
    elif pred==58:
        return "Tomato___Leaf_Mold", '59.html'
    
    elif pred==59:
        return "Tomato___Septoria_leaf_spot", '60.html'
    
    elif pred==60:
        return "Tomato___healthy", '61.html'




# Create flask instance
app = Flask(__name__)

# render index.html page
@app.route("/", methods=['GET', 'POST'])
def home():
        return render_template('index.html')
    
 
# get input image from client then predict class and render respective .html page for solution
@app.route("/predict", methods = ['GET','POST'])
def predict():
     if request.method == 'POST':
        file = request.files['image'] # fet input
        filename = file.filename        
        print("@@ Input posted = ", filename)
        
        file_path = os.path.join('static/upload/', filename)
        file.save(file_path)

        print("@@ Predicting class......")
        pred, output_page = pred_disease(fruit=file_path)
              
        return render_template(output_page, pred_output = pred, user_image = file_path)

# get back to homepage
@app.route("/back")
def back():
        return render_template('index.html')
    
# For local system & cloud
if __name__ == "__main__":
    app.run(threaded=False,port=8080) 
    
    




