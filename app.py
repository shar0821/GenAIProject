from flask import Flask,request,jsonify
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

app =Flask(__name__)
# 1. Load the model and corresponding processor (image feature extractor + tokenizer)
model_name = "nlpconnect/vit-gpt2-image-captioning"
model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Example usage
@app.route("/")
def hello_world()-> str:
    return "<p>Hello World</p>"

@app.route("/generate_caption",methods=["POST"])
def generate_caption()-> str:    # Try a sample image URL
    img=request.files["image"]
    pixel_values = feature_extractor(img, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    # 2. Generate caption
    output_ids = model.generate(pixel_values, max_length=16, num_beams=4)
    caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    status_code=200
    return jsonify({"caption":caption,"status_code":status_code})