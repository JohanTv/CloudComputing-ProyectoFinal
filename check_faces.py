import cv2
import os
import numpy as np
from tqdm import tqdm
import time

from tensorflow import keras
from keras.models import model_from_json

root_dir = os.getcwd()
faces_dir = os.path.join(root_dir, 'faces')
# Load Face Detection Model
face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
# Load Anti-Spoofing Model graph
json_file = open('models/antispoofing_model.json','r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
# load antispoofing model weights 
model.load_weights('models/antispoofing_model.h5')
print("Model loaded from disk")

for img in tqdm(os.listdir(faces_dir)):
    t1 = time.time()
    image_path = os.path.join(faces_dir, img)
    img_arr = cv2.imread(image_path)
    resized_face = cv2.resize(img_arr,(160,160))
    resized_face = resized_face.astype("float") / 255.0
    resized_face = np.expand_dims(resized_face, axis=0)
    # pass the face ROI through the trained liveness detector
    # model to determine if the face is "real" or "fake"
    preds = model.predict(resized_face)[0]
    if preds> 0.5:
        label = 'spoof'
        t2 = time.time()
    else:
        label = 'real'
        t2 = time.time()
        
    print(f"The image={img} is ***{label}*** and time taken was {(t2 - t1):0.3f}")