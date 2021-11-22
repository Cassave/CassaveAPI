from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import numpy as np
from PIL import Image
from src import get_label

app = Flask(__name__)
CORS(app)

model = torch.jit.load('./models/model.pt')



@app.route("/predict", methods=['POST'])
def predict():
    if "file" not in request.files:
        resp = jsonify({"message": "No file found"})
        resp.status_code = 400
        return resp
    else:
        model.cpu()
        img = Image.open(request.files["file"].stream).convert(
            "RGB").resize((512, 512))
        img = np.array(img)
        img = torch.from_numpy(img).unsqueeze(0)
        label = model(img.cpu())[0].item()
        return jsonify(get_label(label))


if __name__ == "__main__":
    app.run(debug=True)
