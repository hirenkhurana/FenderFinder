import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

imagenet_class_index = json.load(open('class_index.json')) # class id to name mapping 
model = models.resnet50(pretrained=True) # define our model here
# do any modification of the model we want here
model.fc = torch.nn.Linear(model.fc.in_features, 196)
model.load_state_dict(torch.load('carML.pt', map_location=torch.device('cpu'))) # load the saved model state here
model.eval()

def transform_image(image_bytes):  # modify the transform function to suit our model
    my_transforms = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return predicted_idx, imagenet_class_index[predicted_idx]

@app.route('/classify', methods=['POST'])
def classify():
    if request.method == 'POST':
        # we will get the file from the request
        file = request.files['file']
        # convert that to bytes
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name })

@app.route('/', methods=['GET'])
def testing():
    if request.method == 'GET':
        return 'Hello'

if __name__ == "__main__":
    app.run(debug=True)

