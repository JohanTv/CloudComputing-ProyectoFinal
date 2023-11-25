import json
import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
import io
import base64
from PIL import Image

def valid_image(image_string):
    # Load Face Detection Model
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Load Anti-Spoofing Model graph
    json_file = open('antispoofing_model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load antispoofing model weights 
    model.load_weights('antispoofing_model.h5')
    print("Model loaded from disk")

    image_byte = image_string.encode('utf-8')
    converted_byte64 = base64.b64decode(image_byte)
    img = Image.open(io.BytesIO(converted_byte64))
    frame = np.asarray(img)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:  
        face = frame[y-5:y+h+5,x-5:x+w+5]
        resized_face = cv2.resize(face,(160,160))
        resized_face = resized_face.astype("float") / 255.0
        resized_face = np.expand_dims(resized_face, axis=0)
        # pass the face ROI through the trained liveness detector
        # model to determine if the face is "real" or "fake"
        preds = model.predict(resized_face)[0]
        print(preds)
        if preds > 0.0001:
            return False
        else:
            return True

def handler(event, context):
    label = valid_image(event['body'])
    
    response = {
        "statuscode": 200,
        "body": json.dumps({
            'label': 'real' if label else 'fake'
        })
    }
    
    return response